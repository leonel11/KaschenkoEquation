import numpy as np
import matplotlib.pyplot as plt


g_min = -4.1
g_max = 4.1
n_gammas = 8201


def get_alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


def visualise_alphas(gs, alps):
    plt.rcParams.update({'font.size': 13})
    plt.subplots_adjust(left=0.13, bottom=0.11, right=0.98, top=0.98)
    plt.xlabel('$\gamma$')
    plt.ylabel(r'$\alpha$', rotation='horizontal', position=(0.0, 0.55))
    plt.grid()
    plt.plot(gs, alps, label=r'$\alpha_u$', color='b', linewidth=2, zorder=4)
    plt.legend(loc='upper right')
    plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    plt.axvline(x=0.0, linewidth=2, color='grey', zorder=2)
    plt.show()


gammas = list(np.linspace(g_min, g_max, n_gammas))
alphas = list(map(lambda x: -x, gammas))
visualise_alphas(gammas, alphas)