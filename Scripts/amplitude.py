import numpy as np

a = 0.0
b = 1.0
P = 0.0
D = 0.0

eps = 0.001
gamma = 4.1
N = 50

def A_func():
    pass

h = 1.0/N
y = list(np.loadtxt('point.txt'))
x = np.arange(a+h/2.0, b, h)
if gamma <= 0.0:
    for i in range(50):
        P += y[i]*np.cosh(np.sqrt(-gamma)*x[i])
        D += np.cosh(np.sqrt(-gamma)*x[i])*np.cosh(np.sqrt(-gamma)*x[i])
else:
    for i in range(50):
        P += y[i]*np.cos(np.sqrt(gamma)*x[i])
        D += np.cos(np.sqrt(gamma)*x[i])*np.cos(np.sqrt(gamma)*x[i])
A = P/(D*np.sqrt(eps))
print('A = {:.4}'.format(A))
print('φ/d = {:.4}'.format(-A*A))
