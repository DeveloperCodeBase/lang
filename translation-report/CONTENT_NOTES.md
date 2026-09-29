# Translation Content & Sensitivity Notes

- **Source Commit**: `null` (No git SHA or commit metadata present in snapshot).
- **Snapshot Source**: `apps/web/src/locales/` from repository `DeveloperCodeBase/digiuniversity`.
- **Source Baseline**: `fa/` containing 32 catalogs (12,979 unique keys). Preserved 100% bit-for-bit unchanged.
- **Academic Terminology**: Maintained strict distinctions between course (درس), group/section (گروه درس), faculty (دانشکده), instructor (مدرس/استاد), teaching assistant (دستیار آموزشی), assessor (ارزیاب), admission (پذیرش), and registration/enrollment (ثبت‌نام).
- **Legal & Wellness Catalogs (`legal.json`, `wellness.json`, `assess.json`)**: Translated faithfully without adding unverified legal/medical advice or altering currency amounts, crisis numbers, or regional statutory claims.
- **ICU & Placeholders**: Preserved all `{name}`, `{value}`, `{count}`, `{label}`, `{time}`, etc. Placeholders were checked for syntax and escaping.
- **RTL Integrity**: Logical Unicode order maintained for RTL languages (fa, ar, ur, ug, ps, ckb, he) without illegal directional injection.
- **landing.brand.json**: Source file is `{}`. Created empty `{}` structure across all target languages as specified.
- **Beta / AI-Translated State**: Target translations represent machine/unreviewed Beta stage; not certified or human-approved.
