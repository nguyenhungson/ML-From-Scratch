"""Kiem tra bo khung: khong cham diem thuat toan chua implement."""
from pathlib import Path
import ast
import importlib.util
import json
import sys

BASE=Path(__file__).resolve().parent
idx=json.loads((BASE/'index.json').read_text(encoding='utf-8'))
errors=[]
for e in idx:
    p=BASE/'lessons'/e['id']
    source=p/'student.py'
    for doc in ['README.md','HINTS.md','tests/test_student.py']:
        if not (p/doc).exists(): errors.append(f'{e["id"]}: thieu {doc}')
    try:
        ast.parse(source.read_text(encoding='utf-8'))
        spec=importlib.util.spec_from_file_location('isolated_student',source)
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as exc:
        errors.append(f'{e["id"]}: {type(exc).__name__}: {exc}')
    text=source.read_text(encoding='utf-8')
    if 'from mlfromscratch' in text or 'import mlfromscratch' in text:
        errors.append(f'{e["id"]}: import repo goc')
    if 'from practice' in text or 'import practice' in text:
        errors.append(f'{e["id"]}: import lesson khac')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: {len(idx)} bai deu day du file, parse/import doc lap, khong phu thuoc code goc.')
print('Luu y: test hanh vi co chu y FAIL khi chua implement TODO.')
