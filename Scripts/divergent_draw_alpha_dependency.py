import numpy as np
import matplotlib.pyplot as plt


x0 = 0.45
g_min = 5.0
g_max = 8.0
n_points = 3001


def get_alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


def get_gamma_local_min(gammas, alphas):
    return gammas[alphas.index(min(alphas))]

def visualise_alphas(gs, aus):
    plt.rcParams.update({'font.size': 13})
    plt.rcParams['savefig.directory'] = '../Tracer/Results/Dynamics of alpha_u'
    plt.figure().canvas.set_window_title('x0={:.2}__g[{:.5},{:.5}]'.format(x0, g_min, g_max)) # change window title
    plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.98)
    plt.xlabel('$\gamma$')
    plt.ylabel(r'$\alpha_u$', rotation='horizontal', position=(0.0, 0.55))
    plt.grid()
    plt.plot(gs, aus, color='b', linewidth=2, zorder=3)
    #plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    #plt.axvline(x=0.0, linewidth=2, color='grey', zorder=2)
    g_loc = get_gamma_local_min(gammas, alpha_u)
    if g_loc != gs[-1]:
        plt.axvline(x=g_loc, linewidth=2, color='grey', linestyle='--', zorder=2)
        print('g_loc = = {:.5}'.format(g_loc))
    #x1,x2,y1,y2 = plt.axis()
    #plt.axis((x1,x2,-50.0,50.0))
    plt.show()


gammas = np.linspace(g_min, g_max, n_points)
alpha_u = [get_alpha_u(g, x0) for g in gammas]
visualise_alphas(gammas, alpha_u)