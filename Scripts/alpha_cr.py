import cmath
import numpy as np
import matplotlib.pyplot as plt


x0 = 0.0
gamma = -1.0
a_min = -4.262
a_max = -4.261
h = 0.00001
alphas= list(np.arange(a_min, a_max, h))


def re_phi(g, a, x0):
    if g < 0:
        mu = np.sqrt(-g)
        A = mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0)
        B = 2*mu*np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        A = mu*np.cos(mu) + np.sin(mu) - a*x0*np.sin(mu*x0)
        B = 2*mu*np.cos(mu*x0)
    return B/A


def re_d(g, a, x0):
    if g < 0:
        mu = np.sqrt(-g)
        A = 16*mu*(mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
        B = 3*mu*np.sinh(3*mu) + 24*mu*np.sinh(mu) - a*np.cosh(3*mu*x0) - 12*a*mu*x0*np.sinh(mu*x0)
    else:
        mu = np.sqrt(g)
        A = 16*mu*(mu*np.cos(mu) + np.sin(mu) - a*x0*np.sin(mu*x0))
        B = 3*mu*np.sin(3*mu) + 24*mu*np.sin(mu) - a*np.cos(3*mu*x0) - 12*a*mu*x0*np.sin(mu*x0)
    return B/A


phi = []
d = []
for a in alphas:
    phi.append(re_phi(gamma, a, x0))
    d.append(re_d(gamma, a, x0))
plt.figure(figsize=(22, 12))
plt.xlabel('a')
plt.ylabel('Re')
plt.grid(True)
plt.plot(alphas, phi, label='Re φ')
plt.plot(alphas, d, label = 'Re d')
plt.legend()
plt.show()