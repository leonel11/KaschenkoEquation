import cmath
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x0 = 0.67
g_min = 10.4
g_max = 25.7
h = 0.001
gammas= list(np.arange(g_min, g_max, h))


def alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)

def denom(g, a, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0)
    else:
        mu = np.sqrt(g)
        return mu*np.cos(mu) + np.sin(mu) - a*x0*np.sin(mu*x0)


plt.figure('Denominator.  Xo = {:.2}, gamma [{:.3}, {:.3}]'.format(x0, g_min, g_max))
mpl.rc('font', size=13)
plt.xlabel('gamma')
plt.ylabel('Denominator')
plt.grid(True)
alphas = []
denoms = []
for g in gammas:
    alphas.append(alpha_u(g, x0))
for idx in range(len(gammas)):
    denoms.append(denom(gammas[idx], alphas[idx], x0))
plt.subplots_adjust(left=0.06, bottom=0.06, right=0.99, top=0.99)
plt.plot(gammas, denoms)
plt.show()