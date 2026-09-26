"""Offline integrity checks. These checks do not establish historical or scientific truth."""
from project import validate, reference_records, question_records, timeline_records
if __name__=='__main__':
    errors=validate()
    if errors:raise SystemExit('\n'.join(errors))
    print(f'通过：{len(reference_records())} 项文献、{len(question_records())} 个问题、{len(timeline_records())} 个时间轴节点；文件、锚点、引用对应与推导标记一致。')
