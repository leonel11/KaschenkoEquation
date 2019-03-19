import numpy as np
import matplotlib.pyplot as plt


x0 = 0.17
g_min = -4.1
g_max = 4.224
h = 0.001

gammas = list(np.arange(g_min, g_max, h))


def alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


aus = []
for g in gammas:
    aus.append(alpha_u(g, x0))
    print('{:.5};{:.6}'.format(g, aus[-1]))
for idx in range(len(aus) - 1, 0, -1):
    if aus[idx] * aus[idx - 1] < 0.0:
        print('gamma_^ = {:.6}'.format(gammas[idx]))
        break
plt.rcParams.update({'font.size': 13})
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.98, top=0.98)
plt.xlabel('$\gamma$')
plt.grid()
plt.plot(gammas, aus, label=r'$\alpha_u$', color='b', linewidth=2)
plt.legend()
plt.show()