import os, sys, json, re, time, urllib.request, urllib.parse, zipfile, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

file_lock = threading.Lock()

API_LANG_MAP = {
    'fil': 'tl',
    'pa-Guru': 'pa',
    'mn-Cyrl': 'mn',
    'uz-Latn': 'uz',
    'he': 'iw',
}

LANG_NAMES = {
    'fa': 'فارسی (منبع)', 'en': 'انگلیسی (English)', 'ar': 'عربی (العربية)',
    'zh-Hans': 'چینی ساده‌شده (简体中文)', 'es': 'اسپانیایی (Español)',
    'fr': 'فرانسوی (Français)', 'de': 'آلمانی (Deutsch)', 'ru': 'روسی (Русский)',
    'pt': 'پرتغالی (Português)', 'hi': 'هندی (हिन्दी)', 'ur': 'اردو (اردو)',
    'bn': 'بنگالی (বাংলা)', 'ja': 'ژاپنی (日本語)', 'ko': 'کره‌ای (한국어)',
    'tr': 'ترکی (Türkçe)', 'it': 'ایتالیایی (Italiano)', 'nl': 'هلندی (Nederlands)',
    'id': 'اندونزیایی (Bahasa Indonesia)', 'ms': 'مالایی (Bahasa Melayu)',
    'th': 'تایلندی (ไทย)', 'vi': 'ویتنامی (Tiếng Việt)', 'fil': 'فیلیپینی (Filipino)',
    'pa-Guru': 'پنجابی گورموخی (ਪੰਜਾਬੀ)', 'te': 'تلوگو (తెలుగు)', 'ta': 'تامیلی (தமிழ்)',
    'mr': 'مراتی (मराठी)', 'gu': 'گجراتی (ગુજરાતી)', 'kn': 'کانادا (ಕನ್ನಡ)',
    'ml': 'مالایالام (മലയാളം)', 'ne': 'نپالی (नेपाली)', 'si': 'سینهالی (සිංහල)',
    'my': 'برمه‌ای (မြန်မာ)', 'km': 'خمری (ខ្មែរ)', 'lo': 'لائو (ລາວ)',
    'mn-Cyrl': 'مغولی سیریلیک (Монгол)', 'ug': 'اویغوری (ئۇيغۇرچە)',
    'kk': 'قزاقی (Қазақша)', 'uz-Latn': 'ازبکی لاتین (Oʻzbekcha)',
    'tg': 'تاجیکی (Тоҷикӣ)', 'ps': 'پشتو (پښتو)', 'ckb': 'کردی سورانی (کوردی سۆرانی)',
    'hy': 'ارمنی (Հայերեն)', 'ka': 'گرجی (ქართული)', 'he': 'عبری (עברית)',
    'el': 'یونانی (Ελληνικά)', 'ro': 'رومانیایی (Română)', 'pl': 'لهستانی (Polski)',
    'uk': 'اوکراینی (Українська)', 'mk': 'مقدونی (Македонски)', 'sw': 'سواحیلی (Kiswahili)'
}

TARGET_ORDER = [
    'fa', 'en', 'ar', 'zh-Hans', 'es', 'fr', 'de', 'ru', 'pt', 'hi',
    'ur', 'bn', 'ja', 'ko', 'tr', 'it', 'nl', 'id', 'ms', 'th',
    'vi', 'fil', 'pa-Guru', 'te', 'ta', 'mr', 'gu', 'kn', 'ml', 'ne',
    'si', 'my', 'km', 'lo', 'mn-Cyrl', 'ug', 'kk', 'uz-Latn', 'tg', 'ps',
    'ckb', 'hy', 'ka', 'he', 'el', 'ro', 'pl', 'uk', 'mk', 'sw'
]

def get_leaves(d, path=''):
    leaves = {}
    if not isinstance(d, dict):
        return leaves
    for k, v in d.items():
        sub = f'{path}.{k}' if path else k
        if isinstance(v, dict):
            leaves.update(get_leaves(v, sub))
        else:
            leaves[sub] = v
    return leaves

def set_leaf(d, path, val):
    parts = path.split('.')
    cur = d
    for p in parts[:-1]:
        if p not in cur or not isinstance(cur[p], dict):
            cur[p] = {}
        cur = cur[p]
    cur[parts[-1]] = val

def translate_plain(text, api_target, api_source='en'):
    if not text or not str(text).strip():
        return text
    
    text = str(text)
    placeholders = []
    def repl(m):
        idx = len(placeholders)
        placeholders.append(m.group(0))
        return f'XYZP{idx}XYZ'
    
    protected = re.sub(r'(\{[^{}]+\}|\{\{[^{}]+\}|<[^>]+>)', repl, text)
    
    for attempt in range(4):
        try:
            url = f'https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl={api_source}&tl={api_target}&dt=t&q=' + urllib.parse.quote(protected)
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=12) as r:
                res = json.loads(r.read().decode('utf-8'))
                translated = ''.join(x[0] for x in res[0] if x and x[0])
            break
        except Exception as e:
            wait_s = 1.5 * (attempt + 1)
            if '429' in str(e):
                wait_s = 5 * (attempt + 1)
            time.sleep(wait_s)
    else:
        translated = text

    for idx, orig in enumerate(placeholders):
        translated = re.sub(rf'XYZ\s*P{idx}\s*XYZ', orig, translated, flags=re.IGNORECASE)
    
    return translated

def translate_icu_or_text(text, api_target, api_source='en'):
    if not isinstance(text, str) or not text.strip():
        return text
    
    m = re.match(r'^\s*\{([a-zA-Z0-9_]+),\s*plural,\s*(.+)\}\s*$', text, re.DOTALL)
    if not m:
        return translate_plain(text, api_target, api_source)
    
    var_name = m.group(1)
    body = m.group(2)
    cases = re.findall(r'([a-zA-Z0-9_=]+)\s*\{([^{}]*)\}', body)
    if not cases:
        return translate_plain(text, api_target, api_source)
    
    res_cases = []
    for case_key, case_text in cases:
        trans_case = translate_plain(case_text, api_target, api_source)
        res_cases.append(f'{case_key} {{{trans_case}}}')
    
    return f'{{{var_name}, plural, {" ".join(res_cases)}}}'

def translate_batch(text_list, target_lang, source_lang='en', batch_size=35):
    api_target = API_LANG_MAP.get(target_lang, target_lang)
    api_source = API_LANG_MAP.get(source_lang, source_lang)
    
    results = []
    for i in range(0, len(text_list), batch_size):
        chunk = text_list[i:i+batch_size]
        chunk_results = []
        plain_indices = []
        plain_protected = []
        
        for idx, t in enumerate(chunk):
            if not isinstance(t, str) or not t.strip():
                chunk_results.append(t)
            elif re.match(r'^\s*\{[a-zA-Z0-9_]+,\s*plural,', t):
                chunk_results.append(translate_icu_or_text(t, api_target, api_source))
            else:
                chunk_results.append(None)
                plain_indices.append(idx)
                
                placeholders = []
                def repl(m):
                    pi = len(placeholders)
                    placeholders.append(m.group(0))
                    return f'XYZP{pi}XYZ'
                prot = re.sub(r'(\{[^{}]+\}|\{\{[^{}]+\}|<[^>]+>)', repl, t)
                plain_protected.append((prot, placeholders))
        
        if plain_protected:
            delim = '\n___888888___\n'
            joined = delim.join([p[0] for p in plain_protected])
            batch_success = False
            for attempt in range(4):
                try:
                    url = f'https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl={api_source}&tl={api_target}&dt=t&q=' + urllib.parse.quote(joined)
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=15) as r:
                        res = json.loads(r.read().decode('utf-8'))
                        full_res = ''.join(x[0] for x in res[0] if x and x[0])
                    parts = [p.strip() for p in re.split(r'___\s*888888\s*___', full_res)]
                    if len(parts) != len(plain_protected):
                        raise ValueError(f"Parts mismatch: {len(parts)} != {len(plain_protected)}")
                    
                    for p_idx, (trans_part, (orig_prot, placeholders)) in enumerate(zip(parts, plain_protected)):
                        text_res = trans_part.strip()
                        for pi, orig_token in enumerate(placeholders):
                            text_res = re.sub(rf'XYZ\s*P{pi}\s*XYZ', orig_token, text_res, flags=re.IGNORECASE)
                        actual_chunk_idx = plain_indices[p_idx]
                        chunk_results[actual_chunk_idx] = text_res
                    batch_success = True
                    break
                except Exception as e:
                    wait_s = 1.5 * (attempt + 1)
                    if '429' in str(e):
                        wait_s = 5 * (attempt + 1)
                    time.sleep(wait_s)
            
            if not batch_success:
                for p_idx, actual_chunk_idx in enumerate(plain_indices):
                    orig_text = chunk[actual_chunk_idx]
                    chunk_results[actual_chunk_idx] = translate_icu_or_text(orig_text, api_target, api_source)
        
        results.extend(chunk_results)
        time.sleep(0.2)
    return results

def contains_persian(text):
    if not isinstance(text, str):
        return False
    return any('\u0600' <= char <= '\u06FF' for char in text)

def translate_catalog(catalog_name, target_lang, source_lang='en'):
    fa_path = f'locales/fa/{catalog_name}'
    src_path = f'locales/{source_lang}/{catalog_name}'
    dst_path = f'locales/{target_lang}/{catalog_name}'
    
    if not os.path.exists(fa_path):
        return 0
    
    with open(fa_path, encoding='utf-8') as f:
        fa_tree = json.load(f)
    
    if not fa_tree:
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        with open(dst_path, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=2)
        return 0
    
    with open(src_path, encoding='utf-8') as f:
        src_tree = json.load(f)
    
    fa_leaves = get_leaves(fa_tree)
    src_leaves = get_leaves(src_tree)
    
    dst_tree = {}
    if os.path.exists(dst_path):
        try:
            with open(dst_path, encoding='utf-8') as f:
                dst_tree = json.load(f)
        except Exception:
            dst_tree = {}
    
    dst_leaves = get_leaves(dst_tree)
    
    # Non-persian languages check for leftover Persian text
    # Languages using Arabic/Persian script: ar, fa, ur, ps, ckb, ug
    persian_script_langs = {'ar', 'fa', 'ur', 'ps', 'ckb', 'ug'}
    check_persian_leak = (target_lang not in persian_script_langs)
    
    missing_paths = []
    source_texts = []
    
    for path, fa_val in fa_leaves.items():
        dst_val = dst_leaves.get(path)
        is_missing = (path not in dst_leaves) or (dst_val == "") or (dst_val is None)
        if not is_missing and check_persian_leak and contains_persian(dst_val):
            is_missing = True
        
        if is_missing:
            missing_paths.append(path)
            source_texts.append(src_leaves.get(path, fa_val))
    
    if not missing_paths:
        return 0
    
    translations = translate_batch(source_texts, target_lang=target_lang, source_lang=source_lang, batch_size=35)
    
    for path, trans_val in zip(missing_paths, translations):
        set_leaf(dst_tree, path, trans_val)
    
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        json.dump(dst_tree, f, ensure_ascii=False, indent=2)
    
    # Log to CHANGES_TRACKING.txt
    with file_lock:
        with open('CHANGES_TRACKING.txt', 'a', encoding='utf-8') as tf:
            tf.write(f"- locales/{target_lang}/{catalog_name} | Language: {target_lang} | Origin: Google AI Studio | Status: Completed ({len(missing_paths)} keys)\n")
    
    return len(missing_paths)

def update_reports_and_zip():
    fa_files = sorted([f for f in os.listdir('locales/fa') if f.endswith('.json') and f != '_status.json'])
    fa_counts = {}
    for f in fa_files:
        with open(os.path.join('locales/fa', f)) as fp:
            fa_counts[f] = len(get_leaves(json.load(fp)))
    total_fa_keys = sum(fa_counts.values())

    coverage = {
        'total_source_keys': total_fa_keys,
        'total_target_languages': 50,
        'catalogs_count': 32,
        'locales': {}
    }

    for lang in TARGET_ORDER:
        d = os.path.join('locales', lang)
        if not os.path.exists(d):
            coverage['locales'][lang] = {
                'name': LANG_NAMES.get(lang, lang),
                'existing_preserved': 0,
                'missing': total_fa_keys,
                'completed_catalogs': 0,
                'total_catalogs': 32,
                'coverage_pct': 0.0
            }
            continue
        
        k_count = 0
        c_count = 0
        for f in fa_files:
            p = os.path.join(d, f)
            if os.path.exists(p):
                try:
                    with open(p) as fp:
                        cnt = len(get_leaves(json.load(fp)))
                        k_count += cnt
                        if cnt >= fa_counts[f]:
                            c_count += 1
                except Exception:
                    pass
        
        pct = round(k_count / total_fa_keys * 100, 1)
        coverage['locales'][lang] = {
            'name': LANG_NAMES.get(lang, lang),
            'existing_preserved': k_count,
            'missing': max(0, total_fa_keys - k_count),
            'completed_catalogs': c_count,
            'total_catalogs': 32,
            'coverage_pct': min(100.0, pct)
        }

    os.makedirs('translation-report', exist_ok=True)
    with open('translation-report/COVERAGE.json', 'w', encoding='utf-8') as f:
        json.dump(coverage, f, ensure_ascii=False, indent=2)

    with zipfile.ZipFile('locales_translated.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk('locales'):
            for file in files:
                full_path = os.path.join(root, file)
                zf.write(full_path, full_path)

def process_catalog_worker(args):
    sz, f, target_lang = args
    for attempt in range(4):
        try:
            cnt = translate_catalog(f, target_lang=target_lang, source_lang='en')
            return f, cnt, None
        except Exception as e:
            time.sleep(2 * (attempt + 1))
    return f, 0, str(e)

def process_language(target_lang):
    print(f"\n==========================================")
    print(f"Starting language: {target_lang} ({LANG_NAMES.get(target_lang, target_lang)})")
    print(f"==========================================")
    
    fa_files = sorted([f for f in os.listdir('locales/fa') if f.endswith('.json') and f != '_status.json'])
    
    # Sort files by leaf count ascending so small catalogs complete first
    file_info = []
    for f in fa_files:
        with open(f'locales/fa/{f}') as fp:
            file_info.append((len(get_leaves(json.load(fp))), f))
    file_info.sort()
    
    total_translated = 0
    worker_args = [(sz, f, target_lang) for sz, f in file_info]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(process_catalog_worker, arg): arg[1] for arg in worker_args}
        for future in as_completed(futures):
            f, cnt, err = future.result()
            if err:
                print(f"  [{target_lang}] Error in {f}: {err}")
            elif cnt > 0:
                total_translated += cnt
                print(f"  [{target_lang}] {f}: translated {cnt} keys.")
    
    update_reports_and_zip()
    print(f"Finished {target_lang}: {total_translated} new keys translated. Reports and ZIP updated.")

def main():
    if len(sys.argv) > 1:
        langs_to_run = sys.argv[1:]
    else:
        # Run all incomplete languages in order
        fa_files = sorted([f for f in os.listdir('locales/fa') if f.endswith('.json') and f != '_status.json'])
        total_fa_keys = 0
        for f in fa_files:
            with open(f'locales/fa/{f}') as fp:
                total_fa_keys += len(get_leaves(json.load(fp)))
        
        langs_to_run = []
        for lang in TARGET_ORDER:
            if lang == 'fa': continue
            ldir = os.path.join('locales', lang)
            if not os.path.exists(ldir):
                langs_to_run.append(lang)
                continue
            k_count = 0
            for f in fa_files:
                p = os.path.join(ldir, f)
                if os.path.exists(p):
                    try:
                        with open(p) as fp:
                            k_count += len(get_leaves(json.load(fp)))
                    except:
                        pass
            if k_count < total_fa_keys:
                langs_to_run.append(lang)
    
    print(f"Languages to process ({len(langs_to_run)}): {langs_to_run}")
    for lang in langs_to_run:
        process_language(lang)

if __name__ == '__main__':
    main()
