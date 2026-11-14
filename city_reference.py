"""含误差城市核对量及协方差契约。"""
from frame import totals
from common import number

def city_reference(data):
    b=data['city_reference'];towns=set(totals(data))
    if set(b['towns'])!=towns or number(b['variance'])<0 or number(b['total'])<0:raise ValueError('参考范围或误差非法')
    return dict(b,exact=b['variance']==0)
