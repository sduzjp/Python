#程序文件ex2_2.py
#统计五行字符串中字符a,c,g,t出现的频数
import numpy as np
a=[]
with open('data2_2.txt') as f:
    for (i, s) in enumerate(f):
        a.append([s.count('a'), s.count('c'),
                  s.count('g'),s.count('t')])
b=np.array(a)
print(b)
