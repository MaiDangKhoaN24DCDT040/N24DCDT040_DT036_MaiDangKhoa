import argparse, json, sys
from src.phan_tich import phan_tich_so
p=argparse.ArgumentParser();p.add_argument('--n',type=int);p.add_argument('--k',type=int)
p.add_argument('--trace',action='store_true');p.add_argument('--case');p.add_argument('--summary',action='store_true')
a=p.parse_args()
if a.case:
    from test.run_tests import run
    r=run(a.case);sys.exit(0 if r['passed']==r['total'] else 1)
try:
    n=a.n if a.n is not None else int(input('Nhap n (1..20): '))
    r=phan_tich_so(n,k=a.k,lan_vet=a.trace)
    print('DT036 | n=',n,'| k=',a.k)
    if not a.summary:
        for b in r['nghiem']:print(' + '.join(map(str,b)))
    print('so_cach =',r['so_cach']);print('Bo dem:',r['dem'])
    if a.trace:print('\n'.join(r['vet']))
except ValueError as e:print('INPUT KHONG HOP LE:',e);sys.exit(2)
