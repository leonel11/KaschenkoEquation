import numpy as np
import matplotlib.pyplot as plt


x0 = 0.00
g_min = -3.0
g_max = 3.1
h = 0.001

gammas = list(np.arange(g_min, g_max, h))


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


plt.figure('divergent_phi0d0_x0={:.5},g[{:.5},{:.5}]'.format(x0, g_min, g_max))
plt.rcParams.update({'font.size': 13})
plt.rcParams['savefig.directory'] = '../Tracer/Results'
plt.xlabel('$\gamma$')
#plt.ylabel(r'$d_0$', rotation='horizontal')
plt.grid(True)
alphas, phis, ds, amps = [], [], [], []
for g in gammas:
    alphas.append(alpha_u(g, x0))
for idx in range(len(gammas)):
    phis.append(phi_func(gammas[idx], alphas[idx], x0))
    ds.append(d_func(gammas[idx], alphas[idx], x0))
for idx in range(len(gammas)-1, 0, -1):
    if ds[idx]*ds[idx-1] < 0.0:
        print('gamma_l = {:.6}'.format(gammas[idx]))
        break
plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.98)
plt.plot(gammas, phis, label=r'$\varphi_0$', color='darkcyan', linewidth=2)
plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
plt.plot(gammas, ds, label='$d_0$', color='darkorange', linewidth=2, zorder=3)
#x1,x2,y1,y2 = plt.axis()
#plt.axis((x1,4.902,y1,y2))
plt.legend()
plt.show()