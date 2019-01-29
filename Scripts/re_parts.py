import cmath
import numpy as np
import matplotlib.pyplot as plt


crit_values_file = ''
g_min = -4.0
g_max = 4.0
h = 0.01
x0 = 0.0
alpha = -17.818


def func(g, a, x0):
    if g < 0:
        mu = np.sqrt(-g)
        return mu*mu*np.cosh(mu) + a*(np.cosh(mu*x0) - mu*x0*np.sinh(mu*x0))
    else:
        mu = np.sqrt(g)
        return -mu*mu*np.cos(mu) + a*(np.cos(mu*x0) + mu*x0*np.sin(mu*x0))


def re_phi(g, a, x0):
    if g < 0:
        mu = np.sqrt(-g)
        A = mu*np.sinh(mu) + a*np.cosh(mu*x0) + 2*mu*(mu*np.cosh(mu) - a*x0*np.sinh(mu*x0))
        B = 4*mu*mu*np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        A = -mu*np.sin(mu) + a*np.cos(mu*x0) + 2*mu*(mu*np.cos(mu) + a*x0*np.sin(mu*x0))
        B = 4*mu*mu*np.cos(mu*x0)
    return B/A


def re_d(g, a, x0):
    if g < 0:
        mu = np.sqrt(-g)
        A = 8*(mu*np.sinh(mu) + a*np.cosh(mu*x0) + 2*mu*(mu*np.cosh(mu) - a*x0*np.sinh(mu*x0)))
        B = 4*mu*mu*np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        A = 8*(-mu*np.sin(mu) + a*np.cos(mu*x0) + 2*mu*(mu*np.cos(mu) + a*x0*np.sin(mu*x0)))
        B = 4*mu*mu*np.cos(mu*x0)
    return B/A


gammas = list(np.arange(g_min, g_max, h))
f = []
for g in gammas:
    f.append(func(g, alpha, x0))
plt.figure()
plt.xlabel('γ')
plt.ylabel('f')
plt.grid(True)
plt.plot(gammas, f)
plt.show()