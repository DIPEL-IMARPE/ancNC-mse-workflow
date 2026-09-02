from pathlib import Path
import csv
root=Path(__file__).resolve().parents[2]
out=root/'registry/file_manifest.csv'
rows=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and '.git' not in p.parts and p!=out:
        rows.append([str(p.relative_to(root)).replace('\\','/'),p.suffix,p.stat().st_size])
with out.open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['path','extension','bytes']); w.writerows(rows)
print(f'Wrote {len(rows)} files')
