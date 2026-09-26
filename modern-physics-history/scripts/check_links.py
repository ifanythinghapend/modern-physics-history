"""Optional HTTP availability probe. Reachability is not a content or citation audit."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import argparse
import json
from project import ROOT, reference_records


def classify(status):
    if 200 <= status < 400:return 'reachable'
    if status in (404,410):return 'missing'
    return 'inconclusive'


def probe(url, timeout=12):
    headers={'User-Agent':'PhysicsHistory-LinkCheck/0.2','Accept':'*/*'}
    for method in ('HEAD','GET'):
        try:
            with urlopen(Request(url,headers=headers,method=method),timeout=timeout) as response:
                return {'status':classify(response.status),'http_status':response.status,'final_url':response.url}
        except HTTPError as e:
            if e.code==405 and method=='HEAD':continue
            return {'status':classify(e.code),'http_status':e.code,'final_url':e.url}
        except (URLError,TimeoutError,OSError) as e:
            return {'status':'inconclusive','error':str(e)}
    return {'status':'inconclusive','error':'未得到可判定的响应'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit',type=int,help='Only check the first N bibliography records')
    parser.add_argument('--workers',type=int,default=4)
    parser.add_argument('--timeout',type=float,default=12)
    parser.add_argument('--report',type=Path,default=ROOT/'build/link-report.json')
    args=parser.parse_args()
    refs=reference_records()
    if args.limit is not None:refs=refs[:max(args.limit,0)]
    def check(r):return {'id':r['id'],'url':r['url'],**probe(r['url'],args.timeout)}
    with ThreadPoolExecutor(max_workers=max(1,min(args.workers,8))) as pool:
        results=list(pool.map(check,refs))
    report={'checked_at':datetime.now(timezone.utc).isoformat(),'meaning':'HTTP availability only; 403/429/timeouts remain inconclusive.','results':results}
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    totals={k:sum(r['status']==k for r in results) for k in ('reachable','missing','inconclusive')}
    print(json.dumps(totals,ensure_ascii=False));print(args.report)
    raise SystemExit(1 if totals['missing'] else 0)
if __name__=='__main__':main()
