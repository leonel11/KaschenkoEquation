import numpy as np
import matplotlib.pyplot as plt


x0 = 0.67
g_min = -4.1
g_max = 12.5
h = 0.01
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


plt.figure('PhiD.  Xo = {:.2}, gamma [{:.3}, {:.3}]'.format(x0, g_min, g_max))
plt.xlabel('gamma')
plt.ylabel('φ/d')
plt.grid(True)
alphas = []
phidivd = []
for g in gammas:
    alphas.append(alpha_u(g, x0))
for idx in range(len(gammas)):
    phi = phi_func(gammas[idx], alphas[idx], x0)
    d = d_func(gammas[idx], alphas[idx], x0)
    phidivd.append(phi/d)
    print('{:.2};{:.5}'.format(gammas[idx], phi/d))
plt.subplots_adjust(left=0.06, bottom=0.06, right=0.99, top=0.99)
plt.plot(gammas, phidivd, label='φ/d')
plt.legend()
plt.show()