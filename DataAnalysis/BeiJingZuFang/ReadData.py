# @description:北京租房表格数据的读取
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/8/7 11:02
import pandas as pd

# 读取北京租房的数据表，csv格式
data=pd.read_csv('BeiJingZuFang.csv',encoding='gbk')
# 查看数据的维度
print(data.shape)
# 查看数据表中的前十条数据
print(data.head(10))