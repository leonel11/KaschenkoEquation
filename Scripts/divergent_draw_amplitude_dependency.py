import numpy as np
import matplotlib.pyplot as plt


x0 = 0.49
g_min = 6.21
g_max = 7.78
h = 0.001


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


def amplitude_func(g, a, x0):
    return np.sqrt(abs(phi_func(g, a, x0)/d_func(g, a, x0)))


gammas = list(np.arange(g_min, g_max, h))
amps = []
for g in gammas:
    a = alpha_u(g, x0)
    amps.append(amplitude_func(g, a, x0))
plt.figure('divergent_amplitude_x0={:.5},g[{:.5},{:.5}]'.format(x0, g_min, g_max))
plt.rcParams.update({'font.size': 13})
plt.rcParams['savefig.directory'] = '../Tracer/Results'
plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.98)
plt.xlabel('$\gamma$')
plt.ylabel('$A_u$', rotation='horizontal', position=(0.0, 0.55))
plt.grid()
plt.plot(gammas, amps, color='crimson', linewidth=2)
#x1,x2,y1,y2 = plt.axis()
#plt.axis((x1,4.902,y1,y2))
plt.show()