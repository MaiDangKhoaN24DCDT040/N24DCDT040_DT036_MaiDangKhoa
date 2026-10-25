import json
from src.phan_tich import phan_tich_so
rows=[]
for n in (5,10,20):
 r=phan_tich_so(n);rows.append({'n':n,'so_cach':r['so_cach'],**r['dem']})
print(json.dumps(rows,ensure_ascii=False,indent=2))
