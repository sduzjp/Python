#程序文件ex2_60.py
import tushare as ts
df = ts.get_hist_data('600848')
print(df.head(0))  #显示列名称
print('------------'); print(df)
