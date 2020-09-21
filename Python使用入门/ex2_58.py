#程序文件ex2_58.py
import tushare as ts
df = ts.get_money_supply()
print(df.head())  #显示前5行数据
