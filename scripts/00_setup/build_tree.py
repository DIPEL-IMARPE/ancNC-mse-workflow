from pathlib import Path
root=Path(__file__).resolve().parents[2]
lines=[]
def walk(d,prefix=''):
    items=sorted([x for x in d.iterdir() if x.name not in {'.git','releases'}], key=lambda x:(not x.is_dir(),x.name.lower()))
    for i,x in enumerate(items):
        last=i==len(items)-1; lines.append(prefix+('└── ' if last else '├── ')+x.name)
        if x.is_dir(): walk(x,prefix+('    ' if last else '│   '))
lines.append(root.name); walk(root)
(root/'TREE.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
