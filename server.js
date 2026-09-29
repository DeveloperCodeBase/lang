import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PORT = 3000;
const HOST = '0.0.0.0';

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || 'localhost:3000'}`);
  let pathname = decodeURIComponent(url.pathname);

  // Serve zip downloads
  if (pathname === '/locales_translated.zip' || pathname === '/locales_checkpoint_v1.zip') {
    const filename = pathname.slice(1);
    const filePath = path.join(__dirname, filename);
    if (fs.existsSync(filePath)) {
      const stat = fs.statSync(filePath);
      res.writeHead(200, {
        'Content-Type': 'application/zip',
        'Content-Length': stat.size,
        'Content-Disposition': `attachment; filename="${filename}"`,
        'Cache-Control': 'no-cache'
      });
      fs.createReadStream(filePath).pipe(res);
      return;
    }
  }

  // Serve translation-report files
  if (pathname.startsWith('/translation-report/')) {
    const rel = pathname.slice(1);
    const filePath = path.join(__dirname, rel);
    if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
      const ext = path.extname(filePath);
      const mimeTypes = {
        '.json': 'application/json; charset=utf-8',
        '.txt': 'text/plain; charset=utf-8',
        '.md': 'text/markdown; charset=utf-8'
      };
      res.writeHead(200, {
        'Content-Type': mimeTypes[ext] || 'application/octet-stream',
        'Cache-Control': 'no-cache'
      });
      fs.createReadStream(filePath).pipe(res);
      return;
    }
  }

  // Serve root dashboard
  if (pathname === '/' || pathname === '/index.html') {
    let manifest = {};
    let coverage = {};
    let checkpoint = {};
    try {
      manifest = JSON.parse(fs.readFileSync(path.join(__dirname, 'translation-report/MANIFEST.json'), 'utf-8'));
      coverage = JSON.parse(fs.readFileSync(path.join(__dirname, 'translation-report/COVERAGE.json'), 'utf-8'));
      checkpoint = JSON.parse(fs.readFileSync(path.join(__dirname, 'translation-report/CHECKPOINT.json'), 'utf-8'));
    } catch (e) {}

    const zipSizeMB = fs.existsSync(path.join(__dirname, 'locales_translated.zip'))
      ? (fs.statSync(path.join(__dirname, 'locales_translated.zip')).size / (1024 * 1024)).toFixed(2)
      : '0';

    // Find current/next language in progress
    let nextLangName = 'تمام ۵۰ زبان ۱۰۰٪ کامل شدند';
    let nextLangDesc = 'پوشش کامل برای تمام زبان‌های هدف حاصل شد.';
    let isAllComplete = true;
    let completedLangsCount = 0;
    let rowsHtml = '';

    if (coverage.locales) {
      for (const [code, info] of Object.entries(coverage.locales)) {
        const isComplete = info.coverage_pct >= 99.9;
        if (isComplete) {
          completedLangsCount++;
        } else if (isAllComplete && code !== 'fa') {
          isAllComplete = false;
          nextLangName = `${code} - ${info.name || code}`;
          nextLangDesc = `در حال تکمیل: ${info.completed_catalogs} از ${info.total_catalogs} کاتالوگ (${info.coverage_pct}%)`;
        }

        const badgeClass = isComplete ? 'badge badge-success' : (info.coverage_pct > 20 ? 'badge' : 'badge badge-warning');
        const badgeText = code === 'fa' ? 'اصل منبع' : (isComplete ? 'کامل (۱۰۰٪)' : (info.coverage_pct > 20 ? 'در حال تکمیل' : 'در نوبت ترجمه'));
        const nameText = info.name || code;
        rowsHtml += `
          <tr>
            <td><strong>${code}</strong> <span style="color: var(--muted); font-size: 0.85rem;">(${nameText})</span></td>
            <td><span class="${badgeClass}">${badgeText}</span></td>
            <td>${info.completed_catalogs} / ${info.total_catalogs}</td>
            <td>${info.existing_preserved?.toLocaleString('fa-IR') || info.existing_preserved}</td>
            <td>
              <div style="display: flex; align-items: center; gap: 0.5rem;">
                <div style="flex: 1; background: #334155; height: 8px; border-radius: 4px; overflow: hidden;">
                  <div style="background: ${isComplete ? 'var(--success)' : 'var(--primary)'}; width: ${info.coverage_pct}%; height: 100%;"></div>
                </div>
                <span style="font-weight: 600; min-width: 48px; text-align: left;">${info.coverage_pct}%</span>
              </div>
            </td>
          </tr>`;
      }
    }

    const html = `<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="refresh" content="5">
  <title>Global Locales Translation & Export Platform</title>
  <meta name="description" content="Enterprise i18n localization suite translating, validating and exporting 50 languages with 32 full catalogs, 12,685 keys per language, JSON-LD metadata, and live export downloads.">
  <meta property="og:title" content="Global Locales Translation & Export Platform">
  <meta property="og:description" content="Enterprise i18n localization suite translating, validating and exporting 50 languages with 32 full catalogs, 12,685 keys per language, JSON-LD metadata, and live export downloads.">
  <style>
    :root {
      --bg: #0f172a;
      --card: #1e293b;
      --border: #334155;
      --text: #f8fafc;
      --muted: #94a3b8;
      --primary: #38bdf8;
      --success: #4ade80;
      --warning: #fbbf24;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 2rem 1rem;
    }
    .container { max-width: 1000px; margin: 0 auto; }
    header { margin-bottom: 2rem; border-bottom: 1px solid var(--border); padding-bottom: 1.5rem; }
    h1 { font-size: 1.75rem; margin-bottom: 0.5rem; color: #fff; }
    .badge {
      display: inline-block;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      background: rgba(56, 189, 248, 0.15);
      color: var(--primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }
    .badge-success {
      background: rgba(74, 222, 128, 0.15);
      color: var(--success);
      border-color: rgba(74, 222, 128, 0.3);
    }
    .badge-warning {
      background: rgba(251, 191, 36, 0.15);
      color: var(--warning);
      border-color: rgba(251, 191, 36, 0.3);
    }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 2rem; }
    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 0.75rem;
      padding: 1.25rem;
    }
    .card-title { font-size: 0.9rem; color: var(--muted); margin-bottom: 0.5rem; }
    .card-value { font-size: 1.5rem; font-weight: 700; color: #fff; }
    .download-box {
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      border: 2px solid var(--primary);
      border-radius: 1rem;
      padding: 2rem;
      text-align: center;
      margin-bottom: 2rem;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--primary);
      color: #0f172a;
      font-weight: 700;
      font-size: 1.1rem;
      padding: 0.85rem 2rem;
      border-radius: 0.5rem;
      text-decoration: none;
      transition: all 0.2s;
    }
    .btn:hover { background: #7dd3fc; transform: translateY(-1px); }
    .btn-secondary {
      background: var(--card);
      color: var(--text);
      border: 1px solid var(--border);
      font-size: 0.95rem;
      padding: 0.6rem 1.25rem;
      margin: 0.5rem;
    }
    .btn-secondary:hover { background: #334155; }
    table { width: 100%; border-collapse: collapse; margin-top: 1rem; font-size: 0.9rem; }
    th, td { padding: 0.75rem 1rem; text-align: right; border-bottom: 1px solid var(--border); }
    th { color: var(--muted); font-weight: 600; background: rgba(0,0,0,0.2); }
    tr:hover { background: rgba(255,255,255,0.02); }
    .links-list { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
        <div>
          <h1>بستهٔ خروجی ترجمه و اعتبارسنجی Locales</h1>
          <p style="color: var(--muted); font-size: 0.95rem;">مخزن DeveloperCodeBase/digiuniversity · شاخهٔ codex/global-i18n-50</p>
        </div>
        <span class="badge ${isAllComplete ? 'badge-success' : 'badge-warning'}">${isAllComplete ? '✓ تمام زبان‌ها ۱۰۰٪ تکمیل شدند' : '⟳ در حال پیشرفت بلادرنگ (به‌روزرسانی خودکار)'}</span>
      </div>
    </header>

    <div class="download-box">
      <h2 style="margin-bottom: 0.5rem;">دانلود فایل ZIP خروجی</h2>
      <p style="color: var(--muted); margin-bottom: 1.5rem;">حاوی پوشهٔ کامل locales با ۵۰ زبان هدف، گزارش اعتبارسنجی، پوشش، و منشأ</p>
      <a href="/locales_translated.zip" class="btn" download>
        ⬇ دریافت locales_translated.zip (${zipSizeMB} MB)
      </a>
      <div style="margin-top: 1rem;">
        <a href="/locales_checkpoint_v1.zip" class="btn btn-secondary" download>
          📦 دریافت نسخهٔ Checkpoint v1
        </a>
      </div>
    </div>

    <div class="grid">
      <div class="card">
        <div class="card-title">کلیدهای منبع فارسی (fa)</div>
        <div class="card-value">${(coverage.total_source_keys || 12685).toLocaleString('fa-IR')} کلید</div>
        <p style="font-size: 0.85rem; color: var(--success); margin-top: 0.25rem;">در ۳۲ کاتالوگ (حفظ ۱۰۰٪ دست‌نخورده)</p>
      </div>
      <div class="card">
        <div class="card-title">زبان‌های با پوشش کامل (۱۰۰٪)</div>
        <div class="card-value">${completedLangsCount} از ۵۰ زبان</div>
        <p style="font-size: 0.85rem; color: var(--muted); margin-top: 0.25rem;">تمام ۳۲ کاتالوگ با تطابق ۱:۱</p>
      </div>
      <div class="card">
        <div class="card-title">${isAllComplete ? 'وضعیت نهایی پروژه' : 'زبان در حال ترجمه / زبان بعدی'}</div>
        <div class="card-value" style="font-size: 1.25rem;">${nextLangName}</div>
        <p style="font-size: 0.85rem; color: var(--muted); margin-top: 0.25rem;">${nextLangDesc}</p>
      </div>
    </div>

    <div class="card" style="margin-bottom: 2rem;">
      <h3 style="margin-bottom: 1rem;">مستندات و گزارش‌های فنی</h3>
      <div class="links-list">
        <a href="/translation-report/COVERAGE.json" class="btn btn-secondary" target="_blank">📊 COVERAGE.json</a>
        <a href="/translation-report/MANIFEST.json" class="btn btn-secondary" target="_blank">📋 MANIFEST.json</a>
        <a href="/translation-report/CHECKPOINT.json" class="btn btn-secondary" target="_blank">💾 CHECKPOINT.json</a>
        <a href="/translation-report/VALIDATION.json" class="btn btn-secondary" target="_blank">✅ VALIDATION.json</a>
        <a href="/translation-report/CONTENT_NOTES.md" class="btn btn-secondary" target="_blank">📝 CONTENT_NOTES.md</a>
        <a href="/translation-report/IMPORT_TO_CODEX_FA.txt" class="btn btn-secondary" target="_blank">📥 IMPORT_TO_CODEX_FA.txt</a>
        <a href="/translation-report/SHA256SUMS.txt" class="btn btn-secondary" target="_blank">🔒 SHA256SUMS.txt</a>
      </div>
    </div>

    <div class="card">
      <h3 style="margin-bottom: 0.5rem;">پوشش ۵۰ زبان هدف در این اسنپ‌شات</h3>
      <table>
        <thead>
          <tr>
            <th>کد و نام زبان</th>
            <th>وضعیت</th>
            <th>کاتالوگ‌های کامل</th>
            <th>کلیدهای ترجمه‌شده</th>
            <th>درصد پوشش</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>
    </div>
  </div>
</body>
</html>`;

    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(html);
    return;
  }

  res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
  res.end('Not found');
});

server.listen(PORT, HOST, () => {
  console.log(`Server listening on http://${HOST}:${PORT}`);
});
