import os, sys, json, re, time, urllib.request, urllib.parse, zipfile

ACADEMIC_GLOSSARY_FR = {
    "Makeup quiz": "Quiz de rattrapage",
    "Makeup exam": "Examen de rattrapage",
    "At-Risk Rate": "Taux d'étudiants à risque de décrochage",
    "At-Risk Attendance": "Assiduité à risque",
    "Grading Queue": "File d'attente d'évaluation",
    "Enter Grades": "Saisie des notes",
    "Gradebook": "Carnet de notes",
    "Course Hub": "Pôle du cours",
    "Unclear concept logged": "Concept à clarifier enregistré",
    "Dropped": "Abandonné",
    "Active": "Actif",
    "Completed": "Terminé",
    "Draft": "Brouillon",
    "Submitted": "Soumis",
    "Graded": "Noté",
    "Saturday": "Samedi",
    "Sunday": "Dimanche",
    "Monday": "Lundi",
    "Tuesday": "Mardi",
    "Wednesday": "Mercredi",
    "Thursday": "Jeudi",
    "Friday": "Vendredi"
}

ACADEMIC_GLOSSARY_DE = {
    "Makeup quiz": "Nachholquiz",
    "Makeup exam": "Nachholprüfung",
    "At-Risk Rate": "Gefährdungsquote",
    "At-Risk Attendance": "Gefährdete Anwesenheit",
    "Grading Queue": "Bewertungswarteschlange",
    "Enter Grades": "Noten eingeben",
    "Gradebook": "Notenbuch",
    "Course Hub": "Kursübersicht",
    "Unclear concept logged": "Unklares Konzept erfasst",
    "Dropped": "Abgebrochen",
    "Active": "Aktiv",
    "Completed": "Abgeschlossen",
    "Draft": "Entwurf",
    "Submitted": "Eingereicht",
    "Graded": "Benotet",
    "Saturday": "Samstag",
    "Sunday": "Sonntag",
    "Monday": "Montag",
    "Tuesday": "Dienstag",
    "Wednesday": "Mittwoch",
    "Thursday": "Donnerstag",
    "Friday": "Freitag"
}

ACADEMIC_GLOSSARY_RU = {
    "Makeup quiz": "Пересдача квиза",
    "Makeup exam": "Пересдача экзамена",
    "At-Risk Rate": "Доля студентов в группе риска",
    "At-Risk Attendance": "Посещаемость в группе риска",
    "Grading Queue": "Очередь оценивания",
    "Enter Grades": "Выставление оценок",
    "Gradebook": "Журнал успеваемости",
    "Course Hub": "Хаб курса",
    "Unclear concept logged": "Зафиксирована непонятная тема",
    "Dropped": "Отчислен",
    "Active": "Активен",
    "Completed": "Завершено",
    "Draft": "Черновик",
    "Submitted": "Отправлено",
    "Graded": "Оценено",
    "Saturday": "Суббота",
    "Sunday": "Воскресенье",
    "Monday": "Понедельник",
    "Tuesday": "Вторник",
    "Wednesday": "Среда",
    "Thursday": "Четверг",
    "Friday": "Пятница"
}

ACADEMIC_GLOSSARY_PT = {
    "Makeup quiz": "Quiz de recuperação",
    "Makeup exam": "Exame de recuperação",
    "At-Risk Rate": "Taxa de alunos em risco",
    "At-Risk Attendance": "Frequência em risco",
    "Grading Queue": "Fila de correção",
    "Enter Grades": "Lançar notas",
    "Gradebook": "Boletim de notas",
    "Course Hub": "Central do curso",
    "Unclear concept logged": "Dúvida registrada",
    "Dropped": "Cancelado",
    "Active": "Ativo",
    "Completed": "Concluído",
    "Draft": "Rascunho",
    "Submitted": "Enviado",
    "Graded": "Avaliado",
    "Saturday": "Sábado",
    "Sunday": "Domingo",
    "Monday": "Segunda-feira",
    "Tuesday": "Terça-feira",
    "Wednesday": "Quarta-feira",
    "Thursday": "Quinta-feira",
    "Friday": "Sexta-feira"
}

def translate_plain(text, source='en', target='fr'):
    if not text or not text.strip():
        return text
    
    if target == 'fr' and text in ACADEMIC_GLOSSARY_FR:
        return ACADEMIC_GLOSSARY_FR[text]
    if target == 'de' and text in ACADEMIC_GLOSSARY_DE:
        return ACADEMIC_GLOSSARY_DE[text]
    if target == 'ru' and text in ACADEMIC_GLOSSARY_RU:
        return ACADEMIC_GLOSSARY_RU[text]
    if target == 'pt' and text in ACADEMIC_GLOSSARY_PT:
        return ACADEMIC_GLOSSARY_PT[text]
    
    placeholders = []
    def repl(m):
        idx = len(placeholders)
        placeholders.append(m.group(0))
        return f'XYZP{idx}XYZ'
    
    # Protect ICU parameters, mustache templates, and HTML tags
    protected = re.sub(r'(\{[^{}]+\}|\{\{[^{}]+\}|<[^>]+>)', repl, text)
    
    for attempt in range(4):
        try:
            url = 'https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=' + source + '&tl=' + target + '&dt=t&q=' + urllib.parse.quote(protected)
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=15) as r:
                res = json.loads(r.read().decode('utf-8'))
                translated = ''.join(x[0] for x in res[0] if x and x[0])
            break
        except Exception as e:
            wait_s = 2 * (attempt + 1)
            if '429' in str(e):
                wait_s = 6 * (attempt + 1)
            time.sleep(wait_s)
    else:
        translated = text

    for idx, orig in enumerate(placeholders):
        translated = re.sub(rf'XYZ\s*P{idx}\s*XYZ', orig, translated, flags=re.IGNORECASE)
    
    return translated

def translate_icu_or_text(text, source='en', target='fr'):
    if not isinstance(text, str):
        return text
    if not text.strip():
        return text
    
    # Check for ICU plural
    m = re.match(r'^\s*\{([a-zA-Z0-9_]+),\s*plural,\s*(.+)\}\s*$', text, re.DOTALL)
    if not m:
        return translate_plain(text, source, target)
    
    var_name = m.group(1)
    body = m.group(2)
    cases = re.findall(r'([a-zA-Z0-9_=]+)\s*\{([^{}]*)\}', body)
    if not cases:
        return translate_plain(text, source, target)
    
    res_cases = []
    for case_key, case_text in cases:
        trans_case = translate_plain(case_text, source, target)
        res_cases.append(f'{case_key} {{{trans_case}}}')
    
    return f'{{{var_name}, plural, {" ".join(res_cases)}}}'

def translate_batch(text_list, source='en', target='fr', batch_size=25):
    results = []
    for i in range(0, len(text_list), batch_size):
        chunk = text_list[i:i+batch_size]
        # Separate ICU plurals from plain texts for clean batching
        chunk_results = []
        plain_indices = []
        plain_protected = []
        
        for idx, t in enumerate(chunk):
            if not isinstance(t, str) or not t.strip():
                chunk_results.append(t)
            elif re.match(r'^\s*\{[a-zA-Z0-9_]+,\s*plural,', t):
                chunk_results.append(translate_icu_or_text(t, source, target))
            elif target == 'fr' and t in ACADEMIC_GLOSSARY_FR:
                chunk_results.append(ACADEMIC_GLOSSARY_FR[t])
            else:
                chunk_results.append(None) # To be filled by batch
                plain_indices.append(idx)
                
                # Protect tokens
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
                    url = 'https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=' + source + '&tl=' + target + '&dt=t&q=' + urllib.parse.quote(joined)
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=15) as r:
                        res = json.loads(r.read().decode('utf-8'))
                        full_res = ''.join(x[0] for x in res[0] if x and x[0])
                    parts = [p.strip() for p in re.split(r'___\s*888888\s*___', full_res)]
                    if len(parts) != len(plain_protected):
                        raise ValueError(f"Parts count mismatch: {len(parts)} vs {len(plain_protected)}")
                    
                    for p_idx, (trans_part, (orig_prot, placeholders)) in enumerate(zip(parts, plain_protected)):
                        text_res = trans_part.strip()
                        for pi, orig_token in enumerate(placeholders):
                            text_res = re.sub(rf'XYZ\s*P{pi}\s*XYZ', orig_token, text_res, flags=re.IGNORECASE)
                        actual_chunk_idx = plain_indices[p_idx]
                        chunk_results[actual_chunk_idx] = text_res
                    batch_success = True
                    break
                except Exception as e:
                    wait_s = 2 * (attempt + 1)
                    if '429' in str(e):
                        wait_s = 6 * (attempt + 1)
                    time.sleep(wait_s)
            
            if not batch_success:
                # Fallback to single translate on batch failure
                for p_idx, actual_chunk_idx in enumerate(plain_indices):
                    orig_text = chunk[actual_chunk_idx]
                    chunk_results[actual_chunk_idx] = translate_icu_or_text(orig_text, source, target)
        
        results.extend(chunk_results)
        time.sleep(0.5) # polite pause between chunks
    return results

def get_leaves(d, path=''):
    leaves = {}
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

def translate_catalog(catalog_name, target_lang='fr', source_lang='en'):
    fa_path = f'locales/fa/{catalog_name}'
    src_path = f'locales/{source_lang}/{catalog_name}'
    dst_path = f'locales/{target_lang}/{catalog_name}'
    
    if not os.path.exists(fa_path):
        print(f"Error: {fa_path} does not exist.")
        return 0
    
    with open(fa_path, encoding='utf-8') as f:
        fa_tree = json.load(f)
    
    if not fa_tree and fa_tree == {}:
        # empty catalog in fa
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
    
    # Identify leaves that need translation
    # A leaf needs translation if missing in dst, or empty string, or identical to fa text (when fa is Persian script)
    def contains_persian(text):
        if not isinstance(text, str): return False
        return any('\u0600' <= char <= '\u06FF' for char in text)
    
    missing_paths = []
    source_texts = []
    
    for path, fa_val in fa_leaves.items():
        if path not in dst_leaves or dst_leaves[path] == "" or (target_lang != 'fa' and contains_persian(dst_leaves[path])):
            missing_paths.append(path)
            # Use source_leaves (English) as the source text
            source_texts.append(src_leaves.get(path, fa_val))
    
    print(f"[{target_lang}] {catalog_name}: {len(missing_paths)} of {len(fa_leaves)} keys need translation.")
    if not missing_paths:
        return 0
    
    translations = translate_batch(source_texts, source=source_lang, target=target_lang, batch_size=20)
    
    # Merge translations into dst_tree
    for path, trans_val in zip(missing_paths, translations):
        set_leaf(dst_tree, path, trans_val)
    
    # Write destination file
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        json.dump(dst_tree, f, ensure_ascii=False, indent=2)
    
    print(f"[{target_lang}] Successfully updated {dst_path} with {len(missing_paths)} keys.")
    return len(missing_paths)

def update_reports_and_zip():
    # Count leaves for all fa catalogs
    fa_files = sorted([f for f in os.listdir('locales/fa') if f.endswith('.json')])
    fa_counts = {}
    for f in fa_files:
        with open(os.path.join('locales/fa', f)) as fp:
            fa_counts[f] = len(get_leaves(json.load(fp)))
    total_fa_keys = sum(fa_counts.values())

    lang_names = {
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
        'hy': 'ارمنی (Հայերեն)', 'ka': 'گرجی (ქართული)', 'he': 'عبری (עבריت)',
        'el': 'یونانی (Ελληνικά)', 'ro': 'رومانیایی (Română)', 'pl': 'لهستانی (Polski)',
        'uk': 'اوکراینی (Українська)', 'mk': 'مقدونی (Македонски)', 'sw': 'سواحیلی (Kiswahili)'
    }

    target_order = ['fa', 'en', 'ar', 'zh-Hans', 'es', 'fr', 'de', 'ru', 'pt', 'hi', 'ur', 'bn', 'ja', 'ko', 'tr', 'it', 'nl', 'id', 'ms', 'th', 'vi', 'fil', 'pa-Guru', 'te', 'ta', 'mr', 'gu', 'kn', 'ml', 'ne', 'si', 'my', 'km', 'lo', 'mn-Cyrl', 'ug', 'kk', 'uz-Latn', 'tg', 'ps', 'ckb', 'hy', 'ka', 'he', 'el', 'ro', 'pl', 'uk', 'mk', 'sw']

    coverage = {
        'total_source_keys': total_fa_keys,
        'total_target_languages': 50,
        'catalogs_count': 32,
        'locales': {}
    }

    for lang in target_order:
        d = os.path.join('locales', lang)
        if not os.path.exists(d):
            coverage['locales'][lang] = {
                'name': lang_names.get(lang, lang),
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
        
        pct = round(k_count / total_fa_keys * 100, 2)
        coverage['locales'][lang] = {
            'name': lang_names.get(lang, lang),
            'existing_preserved': k_count,
            'missing': max(0, total_fa_keys - k_count),
            'completed_catalogs': c_count,
            'total_catalogs': 32,
            'coverage_pct': min(100.0, pct)
        }

    os.makedirs('translation-report', exist_ok=True)
    with open('translation-report/COVERAGE.json', 'w', encoding='utf-8') as f:
        json.dump(coverage, f, ensure_ascii=False, indent=2)

    # Create / update locales_translated.zip
    with zipfile.ZipFile('locales_translated.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk('locales'):
            for file in files:
                full_path = os.path.join(root, file)
                zf.write(full_path, full_path)
    
    print("Report and locales_translated.zip updated.")

def translate_full_language(target_lang, source_lang='en'):
    fa_files = sorted([f for f in os.listdir('locales/fa') if f.endswith('.json')])
    file_sizes = []
    for f in fa_files:
        with open(f'locales/fa/{f}') as fp:
            file_sizes.append((len(get_leaves(json.load(fp))), f))
    file_sizes.sort()
    
    total_translated = 0
    for sz, f in file_sizes:
        for attempt in range(5):
            try:
                cnt = translate_catalog(f, target_lang=target_lang, source_lang=source_lang)
                if cnt > 0:
                    total_translated += cnt
                    with open('CHANGES_TRACKING.txt', 'a', encoding='utf-8') as tf:
                        tf.write(f"- locales/{target_lang}/{f} | Language: {target_lang} | Origin: Google AI Studio | Status: Completed ({cnt} keys)\n")
                    update_reports_and_zip()
                break
            except Exception as err:
                print(f"Error on {f} (attempt {attempt+1}): {err}. Retrying...")
                time.sleep(3 * (attempt + 1))
        else:
            print(f"Failed all retries for {f}")
    print(f"[{target_lang}] Finished full language pass. Total keys translated: {total_translated}")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        tlang = sys.argv[1]
        translate_full_language(tlang)
    elif len(sys.argv) > 2:
        cat = sys.argv[1]
        tlang = sys.argv[2]
        cnt = translate_catalog(cat, tlang)
        if cnt > 0:
            update_reports_and_zip()
