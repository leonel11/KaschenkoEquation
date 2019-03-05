import cmath
import numpy as np
import matplotlib.pyplot as plt


g_min = -4.0
g_max = 0.0
h = 0.01
x0 = 0.00


def alpha_u(g, x0):
    if g < 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


gammas = list(np.arange(g_min, g_max, h))
alphas = []
for g in gammas:
    alphas.append(alpha_u(g, x0))
plt.figure()
plt.xlabel('γ')
plt.ylabel('α')
plt.grid(True)
plt.plot(gammas, alphas)
plt.show()