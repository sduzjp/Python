# @description:对北京租房数据进行清洗
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/8/7 11:38
import numpy as np
import pandas as pd
# 前期采集到的数据，或多或少都会存在数据缺失、极端值、数据格式不统一等问题,因此，在分析数据之前需要对脏数据进行清洗操作
# pandas中常见的数据 清洗操作主要有空值或缺失值的处理、重复值的处理、异常值的处理、数据类型转换、统一数据格式等。

data=pd.read_csv('BeiJingZuFang.csv',encoding='gbk')
#查看DataFrame的完整摘要
# print(data.info())
# print("=================================")
#查看哪些列存在缺失或空值
# print(data.isnull().any())
# print("=================================")
# #查看“小区名称”中存在缺失或空值的数据
# con=data['小区名称'].isnull()
# print(data[con])
# print("=================================")
# #同样方法，查看“楼层”中存在缺失或空值的数据
# con=data['楼层'].isnull()
# print(data[con])
# print("=================================")
#删除含有空值或缺省值的行
bj_data2=data.dropna()
# #6、查看删除空值或缺省值后数组的维度
# print(bj_data2.shape)
# print("=================================")
#查看是否存在重复值
print(bj_data2.duplicated())
#2、删除重复值
bj_data3=bj_data2.drop_duplicates()
#3、查看删除重复值后数组的维度
print(bj_data3.shape)
# for i in range(bj_data3.shape[0]):
#     print(bj_data3[i])
#2、处理异常值
# bj_data3['租金'][con]=np.NaN
# bj_data4=bj_data3.dropna()
# for i in range(bj_data3.shape[0]):
#     if bj_data3['租金'][i]<400000:
#         bj_data3.drop(bj_data3.index[i])
        # bj_data3['租金'][i]=np.NaN
# # bj_data4=bj_data3.dropna()
# print(bj_data3.shape)
#1、处理“面积(㎡)”列中的中文字符和数据类型的转换
bj_data3['面积(㎡)'] = bj_data3['面积(㎡)'].astype(str).map(lambda x: x.rstrip('㎡'))
mj_data=bj_data3['面积(㎡)'].astype(np.float64)
bj_data3.loc[:,'面积(㎡)']=mj_data