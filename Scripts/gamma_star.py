import cmath
import numpy as np
import matplotlib.pyplot as plt


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