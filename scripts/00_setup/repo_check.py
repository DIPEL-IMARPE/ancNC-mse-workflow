from pathlib import Path

root = Path(__file__).resolve().parents[2]
missing = []

for d in [p for p in root.rglob('*') if p.is_dir() and '.git' not in p.parts]:
    rel = d.relative_to(root)

    # `.github/` is a deliberate exception: a README there can override the
    # repository landing-page README. It is documented with ABOUT files instead.
    if rel == Path('.github'):
        for f in ('ABOUT.md', 'ABOUT.en.md'):
            if not (d / f).exists():
                missing.append(str((d / f).relative_to(root)))
        continue

    for f in ('README.md', 'README.en.md'):
        if not (d / f).exists():
            missing.append(str((d / f).relative_to(root)))

required = [
    'README.md',
    'README.en.md',
    'species_profile.yml',
    'publication.yml',
    'config/operating_model.yml',
    'config/observation_model.yml',
    'config/estimation_model.yml',
    'config/implementation_model.yml',
]

for f in required:
    if not (root / f).exists():
        missing.append(f)

if missing:
    print('Repository check: FAIL')
    print('\n'.join(missing))
    raise SystemExit(1)

print('Repository check: PASS')
