import numpy as np
import matplotlib.pyplot as plt


x0 = 0.98
g_min = 2.0
g_max = 3.0
n_points = 1000


def alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


def alpha_1(g):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.tanh(mu)
    else:
        mu = np.sqrt(g)
        return -mu*np.tan(mu)


gammas = np.linspace(g_min, g_max, n_points)
au, a1 = [], []
for g in gammas:
    au.append(alpha_u(g, x0))
    a1.append(alpha_1(g))
plt.figure('comparison_au_a1_x0={:.5},g[{:.5},{:.5}]'.format(x0, g_min, g_max))
plt.rcParams.update({'font.size': 13})
plt.rcParams['savefig.directory'] = '../Tracer/Results'
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.98, top=0.98)
plt.xlabel('$\gamma$')
plt.plot(gammas, au, label=r'$\alpha_u$' , color='b', linewidth=2)
plt.plot(gammas, a1, label=r'$\alpha_1$', color='y', linewidth=2)
plt.grid()
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,-500.0,500.0))
plt.legend()
plt.show()
