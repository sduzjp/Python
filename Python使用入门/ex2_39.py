#程序文件ex_39.py
import pandas as pd
a=pd.read_csv("data2_38_2.csv", usecols=list(range(1,5)))
b=pd.read_excel("data2_38_3.xlsx", "Sheet2", usecols=list(range(1,5)))
