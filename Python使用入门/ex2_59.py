#程序文件ex2_59.py
import tushare as ts
pro = ts.pro_api('***************************') #用户token码
df = pro.shibor(start_date = '20180601', end_date = '20190729')
print(df)
