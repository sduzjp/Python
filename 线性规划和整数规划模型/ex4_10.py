#程序文件ex4_10.py
import cvxpy as cp
from numpy import array
c = array([[15, 13.8, 12.5, 11, 14.3],
           [14.5, 14, 13.2, 10.5, 15],
           [13.8, 13, 12.8, 11.3, 14.6],
           [14.7, 13.6, 13, 11.6, 14]])
x = cp.Variable((4,5), integer=True)  #定义3个决策变量
obj = cp.Minimize(cp.sum(cp.multiply(c,x)))    #构造目标函数
cons = [0<=x, x<=1, cp.sum(x, axis=0)==1,
        cp.sum(x, axis=1)<=2]     #构造约束条件
prob = cp.Problem(obj, cons)
prob.solve(solver='GLPK_MI')   #求解问题
print('最优解为：', x.value)
print('最优值为：', prob.value)
