import cmath
import numpy as np
import matplotlib.pyplot as plt


x0 = 0.0
alpha = -4.2
g_min = -1.1
g_max = -0.9
h = 0.001
gammas= list(np.arange(g_min, g_max, h))


def re_phi(g, a, x0):
    if g < 0:
        mu = np.sqrt(-g)
        #A = mu*np.sinh(mu) + a*np.cosh(mu*x0) + 2*mu*(mu*np.cosh(mu) - a*x0*np.sinh(mu*x0))
        #B = 4*mu*mu*np.cosh(mu*x0)
        A = mu*np.cosh(mu) + a*np.sinh(mu*x0) + 2*mu*(mu*np.sinh(mu) - a*x0*np.cosh(mu*x0))
        B = 4*mu*mu*np.sinh(mu*x0)
    else:
        mu = np.sqrt(g)
        #A = -mu*np.sin(mu) + a*np.cos(mu*x0) + 2*mu*(-mu*np.cos(mu) + a*x0*np.sin(mu*x0))
        #B = -4*mu*mu*np.cos(mu*x0)
        A = mu*np.cos(mu) + a*np.sin(mu*x0) + 2*mu*(-mu*np.sin(mu) - a*x0*np.cos(mu*x0))
        B = -4*mu*mu*np.sin(mu*x0)
    return B/A


def re_d(g, a, x0):
    if g < 0:
        mu = np.sqrt(-g)
        #A = 8*(mu*np.sinh(mu) + a*np.cosh(mu*x0) + 2*mu*(mu*np.cosh(mu) - a*x0*np.sinh(mu*x0)))
        #B = 3*mu*np.sinh(3*mu) - a*np.cosh(3*mu*x0) + 6*mu*np.sinh(mu) + 6*a*np.cosh(mu*x0) + 12*mu*mu*np.cosh(mu) - 12*a*x0*mu*np.sinh(mu*x0)
        A = 8*(mu*np.cosh(mu) + a*np.sinh(mu*x0) + 2*mu*(mu*np.sinh(mu) - a*x0*np.cosh(mu*x0)))
        B = 9*mu*mu*np.cosh(3*mu) - 3*a*np.sinh(mu*x0) + 6*mu*np.cosh(mu) + 6*a*np.sinh(mu*x0) + 12*mu*mu*np.sinh(mu) - 12*a*x0*mu*np.sinh(mu*x0)
        return B/A
    else:
        mu = np.sqrt(g)
        #A = 8*(-mu*np.sin(mu) + a*np.cos(mu*x0) + 2*mu*(-mu*np.cos(mu) + a*x0*np.sin(mu*x0)))
        #B = -3*mu*np.sinh(3*mu) - a*np.cosh(3*mu*x0) - 6*mu*np.sinh(mu) + 6*a*np.cosh(mu*x0) - 12*mu*mu*np.cosh(mu) + 12*a*x0*mu*np.sinh(mu*x0)
        A = 8*(mu*np.cosh(mu) + a*np.sinh(mu*x0) + 2*mu*(-mu*np.sinh(mu) - a*x0*np.cosh(mu*x0)))
        B = -9*mu*mu*np.cosh(3*mu) - 3*a*np.sinh(mu*x0) + 6*mu*np.cosh(mu) + 6*a*np.sinh(mu*x0) - 12*mu*mu*np.sinh(mu) - 12*a*x0*mu*np.sinh(mu*x0)
        return B/A


phi = []
d = []
for g in gammas:
    phi.append(re_phi(g, alpha, x0))
    d.append(re_d(g, alpha, x0))
plt.figure()
plt.xlabel('a')
plt.ylabel('Re')
plt.grid(True)
plt.plot(gammas, phi, label='Re φ')
plt.plot(gammas, d, label = 'Re d')
plt.legend()
plt.show()