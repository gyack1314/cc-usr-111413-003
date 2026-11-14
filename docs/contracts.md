# 来源接口及口径

frame.py给固定总体household/town/psu/members/floor_area，不含未访家庭真实用水。survey.py提供pi_psu与pi_within，乘积是户入样概率，water是共同月份用水；重复家庭拒绝，同PSU一阶段概率须一致。direct是HT型点总量参考，不提供方差估计。设计为分层PSU及户抽样，town不必是抽样层，PSU身份用stratum字段解释。city_reference.py提供同月全市总量及已给variance，independent_of_sample=true表示外部测算与户样本误差独立，不把方差静默设为0。

输入为UTF-8 JSON，金额用十进制字符串，时间为样例约定的整数日/周/月。行内null是明确状态，不自行推断为数值0。样例范围不限制实际数据规模。
