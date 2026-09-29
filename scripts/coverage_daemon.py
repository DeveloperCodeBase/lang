import os
import json
import time

def get_leaves(d, p=''):
    r = {}
    if isinstance(d, dict):
        for k, v in d.items():
            sub = f'{p}.{k}' if p else k
            if isinstance(v, dict):
                r.update(get_leaves(v, sub))
            else:
                r[sub] = v
    return r

def main():
    fa_files = sorted([f for f in os.listdir('locales/fa') if f.endswith('.json') and f != '_status.json'])
    fa_counts = {}
    for f in fa_files:
        with open(f'locales/fa/{f}', encoding='utf-8') as fp:
            fa_counts[f] = len(get_leaves(json.load(fp)))
    total_fa = sum(fa_counts.values())

    while True:
        try:
            cov_path = 'translation-report/COVERAGE.json'
            if os.path.exists(cov_path):
                with open(cov_path, encoding='utf-8') as f:
                    cov = json.load(f)
                
                cov['total_source_keys'] = total_fa
                cov['catalogs_count'] = len(fa_files)
                
                for l, info in cov['locales'].items():
                    d = f'locales/{l}'
                    if not os.path.exists(d):
                        continue
                    k_cnt = 0
                    c_cnt = 0
                    for f in fa_files:
                        p = f'{d}/{f}'
                        if os.path.exists(p):
                            try:
                                with open(p, encoding='utf-8') as fp:
                                    cnt = len(get_leaves(json.load(fp)))
                                    k_cnt += cnt
                                    if cnt >= fa_counts[f]:
                                        c_cnt += 1
                            except Exception:
                                pass
                    pct = round(k_cnt / total_fa * 100, 1)
                    info['existing_preserved'] = k_cnt
                    info['missing'] = max(0, total_fa - k_cnt)
                    info['completed_catalogs'] = c_cnt
                    info['total_catalogs'] = len(fa_files)
                    info['coverage_pct'] = min(100.0, pct)

                tmp_path = 'translation-report/COVERAGE.json.tmp'
                with open(tmp_path, 'w', encoding='utf-8') as f:
                    json.dump(cov, f, ensure_ascii=False, indent=2)
                os.replace(tmp_path, cov_path)
        except Exception:
            pass
        time.sleep(5)

if __name__ == '__main__':
    main()
