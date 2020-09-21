#程序文件ex2_61.py
import tushare as ts
df = ts.get_stock_basics()
print(df.loc['000001'])
