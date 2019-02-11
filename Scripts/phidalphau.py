import cmath
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x0 = 0.0
g_min = 4.03
g_max = 4.05
h = 0.0001

gammas= list(np.arange(g_min, g_max, h))


def alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


def phi_func(g, a, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        A = mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0)
        B = 2*mu*np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        A = mu*np.cos(mu) + np.sin(mu) - a*x0*np.sin(mu*x0)
        B = 2*mu*np.cos(mu*x0)
    return B/A


def d_func(g, a, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        A = 16*(mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
        B = -3*mu*mu*np.sinh(3*mu) - 12*np.sinh(mu) - 12*mu*np.cosh(mu) - a*mu*np.cosh(3*mu*x0) + 12*a*x0*np.sinh(mu*x0)
    else:
        mu = np.sqrt(g)
        A = 16*(mu*np.cos(mu) + np.sin(mu) - a*x0*np.sin(mu*x0))
        B = 3*mu*mu*np.sin(3*mu) - 12*np.sin(mu) - 12*mu*np.cos(mu) - a*mu*np.cos(3*mu*x0) + 12*a*x0*np.sin(mu*x0)
    return B/A


plt.figure('Phi, d.  Xo = {:.2}, gamma [{:.3}, {:.3}]'.format(x0, g_min, g_max))
mpl.rc('font', size=13)
plt.xlabel('gamma')
plt.ylabel('Re')
plt.grid(True)
alphas = []
phis = []
ds = []
for g in gammas:
    alphas.append(alpha_u(g, x0))
for idx in range(len(gammas)):
    phis.append(phi_func(gammas[idx], alphas[idx], x0))
    ds.append(d_func(gammas[idx], alphas[idx], x0))
print(gammas[-1], phis[-1])
plt.subplots_adjust(left=0.06, bottom=0.06, right=0.99, top=0.99)
#plt.plot(gammas, phis, label='φ')
plt.plot(gammas, ds, label='d', color = 'orange')
plt.legend()
plt.show()