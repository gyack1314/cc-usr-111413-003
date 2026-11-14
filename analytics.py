"""当前来源准备入口。"""
import json
from common import read
from frame import totals
from survey import direct
from city_reference import city_reference
def prepare_sources():
    data=read()
    return {'frame_totals':totals(data),'direct':direct(data),'city_reference':city_reference(data)}
if __name__=="__main__":print(json.dumps(prepare_sources(),ensure_ascii=False,indent=2))
