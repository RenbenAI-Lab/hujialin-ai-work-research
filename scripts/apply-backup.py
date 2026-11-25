"""Validate an exported full backup. Dry-run by default; --write applies it locally."""
import argparse, csv, json
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('backup',type=Path)
parser.add_argument('--write',action='store_true',help='Back up existing data and replace local files')
a=parser.parse_args()
root=Path(__file__).resolve().parents[1]
keys=['papers','themes','tasks','mindmaps','notes','discussions']
columns=['id','title','authors','year','journal','doi','url','theme','status','importance','rating','updatedAt']
data=json.loads(a.backup.read_text(encoding='utf-8-sig'))
for key in keys:
    if not isinstance(data.get(key),list):raise ValueError(f'{key}: expected array')
    ids=set()
    for record in data[key]:
        if not isinstance(record,dict) or not record.get('id'):raise ValueError(f'{key}: missing id')
        if record['id'] in ids:raise ValueError(f'{key}: duplicate id')
        ids.add(record['id'])
        if not record.get('name' if key=='themes' else 'title'):raise ValueError(f'{key}: missing title/name')
    print(f'{key}: {len(data[key])} records')
if not a.write:
    print('Validation passed. No files changed. Review backup, then pass --write to apply locally.')
else:
    from datetime import datetime
    import shutil
    backup=root/'backups'/datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    shutil.copytree(root/'data',backup)
    for key in keys:
        if key=='papers':
            with (root/'data/papers.csv').open('w',encoding='utf-8-sig',newline='') as f:
                writer=csv.DictWriter(f,fieldnames=columns,extrasaction='ignore');writer.writeheader();writer.writerows(data[key])
        else:(root/f'data/{key}.json').write_text(json.dumps(data[key],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Local data updated. Previous files preserved at {backup}. Review git diff before committing.')
