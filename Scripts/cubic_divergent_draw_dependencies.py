import numpy as np
import matplotlib.pyplot as plt


beta = -0.5
x0 = 0.91
g_min = -4.0
g_max = 2.7
h = 0.001


plt.rcParams.update({'font.size': 13})
plt.rcParams['savefig.directory'] = '../Tracer/Variations/Cubic Boundary Condition'


def alpha_u(g, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return -mu*np.sin(mu)/np.cos(mu*x0)


def Q(g, a, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return 2.0*mu / (mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
    else:
        mu = np.sqrt(g)
        return 2.0*mu / (mu*np.cos(mu) + np.sin(mu) - a*x0*np.sin(mu*x0))


def phi_d_A(g, a, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        phi = Q(g, a, x0)*np.cosh(mu*x0)
        d = Q(g, a, x0)*beta*np.cosh(mu*x0)*np.cosh(mu*x0)*np.cosh(mu*x0)
        A = np.sqrt(abs(1.0/(beta*np.cosh(mu*x0)**2)))
    else:
        mu = np.sqrt(g)
        phi = Q(g, a, x0)*np.cos(mu*x0)
        d = Q(g, a, x0)*beta*np.cos(mu*x0)*np.cos(mu*x0)*np.cos(mu*x0)
        A = np.sqrt(abs(1.0/(beta*np.cos(mu*x0)**2)))
    return phi, d, A


def calc_Lyapunov_exps(gammas):
    alphas, phis, ds, amps = [], [], [], []
    for g in gammas:
        alphas.append(alpha_u(g, x0))
    for idx in range(len(gammas)):
        phi, d, A = phi_d_A(gammas[idx], alphas[idx], x0)
        phis.append(phi)
        ds.append(d)
        amps.append(A)
    return phis, ds, amps


def prepare_plot():
    plt.xlabel('$\gamma$')
    plt.grid(True)
    plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.98)
    plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)


def draw_phid_dependencies(gammas, phis, ds):
    plt.figure('divergent_phi0d0_x0={:.5},g[{:.5},{:.5}],beta={:.5}'.format(x0, g_min, g_max, beta))
    prepare_plot()
    plt.plot(gammas, phis, label=r'$\varphi_0$', color='darkcyan', linewidth=2)
    plt.plot(gammas, ds, label='$d_0$', color='darkorange', linewidth=2, zorder=3)
    # x1,x2,y1,y2 = plt.axis()
    # plt.axis((x1,4.902,y1,y2))
    plt.legend()
    plt.show()


def draw_amplitude_dependency(gammas, amps):
    plt.figure('divergent_A_x0={:.5},beta={:.5}'.format(x0, beta))
    prepare_plot()
    plt.plot(gammas, amps, label='$A_u$', color='crimson', linewidth=2)
    plt.legend()
    plt.show()


gammas = list(np.arange(g_min, g_max, h))
phis, ds, amps = calc_Lyapunov_exps(gammas)
draw_phid_dependencies(gammas, phis, ds)
draw_amplitude_dependency(gammas, amps)