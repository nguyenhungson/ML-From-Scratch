"""CLI cho toàn bộ bài tự implement. Chạy tại project root hoặc từ folder khác."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

BASE=Path(__file__).resolve().parent
INDEX=json.loads((BASE/'index.json').read_text(encoding='utf-8'))

def resolve(query):
    matches=[e for e in INDEX if e['id']==query or e['id'].split('/')[-1]==query]
    if len(matches)==1:return matches[0]
    if not matches:raise SystemExit(f'Không thấy lesson: {query}. Xem: python practice/run.py list')
    raise SystemExit('Tên bị trùng, cần id đầy đủ: '+', '.join(e['id'] for e in matches))

def status():
    print('TIẾN ĐỘ (đếm số dấu TODO / NotImplementedError còn lại; KHÔNG phải điểm chấm)')
    for e in INDEX:
        file=BASE/'lessons'/e['id']/'student.py'
        n=file.read_text(encoding='utf-8').count('raise NotImplementedError(')
        completed=e['todo']-n
        print(f"  {e['id']:56s} {completed:3d}/{e['todo']:3d} methods")

def main():
    p=argparse.ArgumentParser(description='ML From Scratch - tự implement độc lập')
    p.add_argument('action',choices=['list','show','test','status','test-all'])
    p.add_argument('module',nargs='?',help='module id, vd k_means hoặc supervised_learning/logistic_regression')
    args=p.parse_args()
    if args.action=='list':
        for e in INDEX:print(f"{e['id']:54s} | {e['level']:18s} | {e['todo']} TODO | {e['title']}")
    elif args.action=='status':status()
    elif args.action=='show':
        if not args.module:p.error('show yêu cầu module')
        f=BASE/'lessons'/resolve(args.module)['id']/'README.md'
        print(f.read_text(encoding='utf-8'))
    elif args.action=='test':
        if not args.module:p.error('test yêu cầu module')
        folder=BASE/'lessons'/resolve(args.module)['id']
        print(f'\nTesting {folder.relative_to(BASE)}\n',flush=True)
        cmd=[sys.executable,'-m','unittest','discover','-s',str(folder/'tests'),'-p','test_*.py','-v']
        raise SystemExit(subprocess.call(cmd,cwd=folder))
    elif args.action=='test-all':
        failures=[]
        for e in INDEX:
            folder=BASE/'lessons'/e['id']
            rc=subprocess.call([sys.executable,'-m','unittest','discover','-s',str(folder/'tests'),'-v'],cwd=folder)
            if rc:failures.append(e['id'])
        print('Chưa pass:',', '.join(failures) if failures else 'Không có')
        raise SystemExit(bool(failures))
if __name__=='__main__':main()
