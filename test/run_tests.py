"""Run independent named cases; each check is counted separately from case count."""
import argparse, hashlib, json, platform, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
CASES = json.loads((ROOT/'test/cases.json').read_text(encoding='utf-8'))

class Checks:
    def __init__(self): self.count = 0
    def equal(self, actual, expected):
        self.count += 1
        if actual != expected:
            raise AssertionError(f'actual={actual!r}; expected={expected!r}')
    def true(self, value): self.equal(bool(value), True)


from src.phan_tich import phan_tich_so, kiem_tra_phan_tich

def count_oracle(n, k=None):
    # Đối chứng chỉ trong test: DP đếm theo tổng và số số hạng, không liệt kê quay lui.
    dp=[[0]*(n+1) for _ in range(n+1)]; dp[0][0]=1
    for v in range(1,n+1):
        for total in range(v,n+1):
            for length in range(1,n+1):
                dp[total][length] += dp[total-v][length-1]
    return sum(dp[n]) if k is None else dp[n][k]

def evaluate(c, t):
    n=c['n']
    if c['op']=='validator':
        actual=kiem_tra_phan_tich(c['b'],n);t.equal(actual,c['expected']);return actual
    if c.get('error'):
        try: phan_tich_so(n,k=c.get('k'))
        except ValueError as e: t.true(True);return f'ValueError: {e}'
        raise AssertionError('Không từ chối input sai')
    r=phan_tich_so(n,k=c.get('k')); a=r['nghiem']
    if c['op']=='alias':
        before=[x.copy() for x in a]; a[0].append(999)
        t.equal(a[1:],before[1:]);t.equal(phan_tich_so(n)['nghiem'],before)
        return 'Sửa nghiệm đầu không làm đổi các nghiệm khác; lần chạy sau độc lập'
    t.equal(r['so_cach'],c['count'])
    t.equal(len(a),count_oracle(n,c.get('k')))
    t.equal(a,sorted(a,reverse=True))
    t.equal(len(a),len(set(tuple(x) for x in a)))
    t.true(all(kiem_tra_phan_tich(x,n) for x in a))
    if c.get('k') is not None:t.true(all(len(x)==c['k'] for x in a))
    if 'expected' in c:t.equal(a,c['expected'])
    return {'so_cach':len(a),'nghiem':a if len(a)<=22 else '627 nghiệm; xem demo --n 20'}


def run(case_id=None):
    selected = [c for c in CASES if case_id is None or c['id'] == case_id]
    if not selected: raise ValueError('Không tìm thấy mã ca')
    rows = []
    for c in selected:
        checks = Checks()
        try:
            actual = evaluate(c, checks)
            row = dict(id=c['id'], goal=c['goal'], actual=actual,
                       status='PASS', assertions=checks.count)
        except Exception as exc:
            row = dict(id=c['id'], goal=c['goal'], actual=str(exc),
                       status='FAIL', assertions=checks.count)
        rows.append(row)
        print(f"{row['id']}: {row['status']} | {row['goal']} | actual={row['actual']}")
    report = {'environment': platform.platform(), 'python':sys.version,
              'time_utc':datetime.now(timezone.utc).isoformat(),
              'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in sorted((ROOT/'src').glob('*.py'))},
              'cases':rows, 'passed':sum(r['status']=='PASS' for r in rows),
              'total':len(rows), 'assertions':sum(r['assertions'] for r in rows)}
    print(f"TONG: {report['passed']}/{report['total']} ca PASS; {report['assertions']} phep kiem")
    return report

if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--case');p.add_argument('--out')
    a=p.parse_args();report=run(a.case)
    if a.out:
        dest=Path(a.out);dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    sys.exit(0 if report['passed']==report['total'] else 1)
