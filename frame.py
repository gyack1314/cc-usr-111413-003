"""调查前固定的有限家庭总体。"""
from common import digest,number

def frame(data):
    rows={}
    for r in data['frame']:
        if r['household'] in rows or r['members']<1 or number(r['floor_area'])<=0:raise ValueError('总体框非法')
        rows[r['household']]=r
    return {'rows':rows,'digest':digest(data['frame'])}

def totals(data):
    out={}
    for r in frame(data)['rows'].values():
        x=out.setdefault(r['town'],{'households':0,'members':0,'floor_area':0});x['households']+=1;x['members']+=r['members'];x['floor_area']+=r['floor_area']
    return out
