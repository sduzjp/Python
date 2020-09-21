#程序文件ex4_12_1.py
import cvxpy as cp
import pylab as plt

c = plt.array([0.05, 0.27, 0.19, 0.185, 0.185])
x = cp.Variable(5, pos=True)
aeq = plt.array([1, 1.01, 1.02, 1.045, 1.065])
obj = cp.Maximize( c @ x)
a = 0; aa = []; Q = []; X = []; M = 10000;             
while a < 0.05:
    con = [aeq @ x == M,
           0.025 * x[1] <= a * M,
           0.015 * x[2] <= a * M,
           0.055 * x[3] <= a * M,
           0.026 * x[4] <= a * M]
    prob = cp.Problem(obj, con)
    prob.solve(solver='GLPK_MI')
    aa.append(a); Q.append(prob.value)
    X.append(x.value)
    a = a + 0.001
plt.rc('text', usetex=True); plt.rc('font', size=15)
plt.plot(aa, Q, 'r*'); plt.xlabel('$a$')
plt.ylabel('$Q$', rotation=0); plt.show()


