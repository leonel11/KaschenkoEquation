import numpy as np
import matplotlib.pyplot as plt


x0 = 0.99
g_min = -4.1
g_max = 160.1
n_points = 10000


def get_alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


def visualise_alphas(gs, aus):
    plt.rcParams.update({'font.size': 13})
    plt.rcParams['savefig.directory'] = '../Tracer/Results/Dynamics of alpha_u'
    plt.figure().canvas.set_window_title('x0={:.2}__g[{:.5},{:.5}]'.format(x0, g_min, g_max)) # change window title
    plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.98)
    plt.xlabel('$\gamma$')
    plt.ylabel(r'$\alpha_u$', rotation='horizontal', position=(0.0, 0.55))
    plt.grid()
    plt.plot(gs, aus, color='b', linewidth=2, zorder=3)
    plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    plt.axvline(x=0.0, linewidth=2, color='grey', zorder=2)
    x1,x2,y1,y2 = plt.axis()
    plt.axis((x1,x2,-50.0,50.0))
    plt.show()


gammas = np.linspace(g_min, g_max, n_points)
alpha_u = [get_alpha_u(g, x0) for g in gammas]
visualise_alphas(gammas, alpha_u)