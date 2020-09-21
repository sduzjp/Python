#程序文件ex2_62.py
import tushare as ts
pro = ts.pro_api()
df = pro.index_basic(market = 'SSE')
print(df)
