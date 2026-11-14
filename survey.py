"""PSU和户两阶段概率样本，直接总量只作参考。"""
from frame import frame
from common import number

def sample(data):
    population=frame(data)['rows'];seen=set();out=[];psu_rates={}
    for r in data['sample']:
        h=r['household']
        if h not in population or h in seen:raise ValueError('样本身份非法')
        seen.add(h);a,b=number(r['pi_psu']),number(r['pi_within'])
        if not 0<a<=1 or not 0<b<=1 or number(r['water'])<0:raise ValueError('概率或用水量非法')
        unit=population[h];p=unit['psu']
        if p in psu_rates and psu_rates[p]!=a:raise ValueError('同PSU入样概率冲突')
        psu_rates[p]=a;out.append(dict(unit,water=r['water'],pi=a*b,weight=1/(a*b)))
    return out

def direct(data):
    out={}
    for r in sample(data):
        x=out.setdefault(r['town'],{'total':0,'n':0,'psus':set()});x['total']+=r['water']*r['weight'];x['n']+=1;x['psus'].add(r['psu'])
    return {k:dict(v,psus=sorted(v['psus'])) for k,v in out.items()}
