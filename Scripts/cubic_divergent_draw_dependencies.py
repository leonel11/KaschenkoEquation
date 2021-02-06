'''
Script for building and visualization dependencies of Lyapunov exponents
(PHI and D values) and Amplitude of oscillations, when zero solution loses
its stability in the DIVERGENT way for LINEAR BOUNDARY-VALUE PROBLEM
WITH CUBIC DEVIATION in boundary conditions
'''

import numpy as np
import drawer
import utils


beta = -1.0
x0 = 0.49
g_min = 10.3
g_max = 17.5

SAVE_DIRECTORY = '../Tracer/Variations/Cubic Boundary Condition' + f'/x0={x0:.2f}'


def Q(g, a, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return 2.0*mu / (mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
    else:
        mu = np.sqrt(g)
        return 2.0*mu / (mu*np.cos(mu) + np.sin(mu) - a*x0*np.sin(mu*x0))


def get_phi(g, a, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return Q(g, a, x0)*np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return Q(g, a, x0)*np.cos(mu*x0)


def get_d(g, a, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        return Q(g, a, x0)*beta*np.cosh(mu*x0)*np.cosh(mu*x0)*np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        return Q(g, a, x0)*beta*np.cos(mu*x0)*np.cos(mu*x0)*np.cos(mu*x0)


def get_Lyapunov_exps(gammas):
    '''
    Calculate and return lists of Lyapunov exponents
    :param gammas: list of gamma values
    :return: list of phi values, list of d values, list of amplitude values
    '''
    alphas, phis, ds, amps = [], [], [], []
    for g in gammas:
        alphas.append(utils.get_alpha_u(g, x0))
    for g, a in zip(gammas, alphas):
        phi0, d0 = get_phi(g, a, x0), get_d(g, a, x0)
        phis.append(-phi0)
        ds.append(d0)
        amps.append(utils.get_amplitude(phi0, d0))
    return phis, ds, amps


def draw_dependencies(gammas, phis, ds, amps):
    '''
    Draw 2 graphics: phi(gamma), d(gamma) dependencies and amplitude(gamma)
    dependency
    :param gammas: list of gamma values
    :param phis: list of phis values
    :param ds: list of d values
    :param amps: list of amplitude values
    '''
    # draw phi, d dependencies
    phid_figure_name = 'cubic_divergent_phi0d0_x0={:.5},g[{:.5},{:.5}],beta={:.5}'.format(x0, g_min, g_max, beta)
    drawer_phid = drawer.Drawer(x_label=r'$\gamma$', figure_name=phid_figure_name, save_dir=SAVE_DIRECTORY)
    drawer_phid.drawAxis(show_Ox=True)
    drawer_phid.drawTwoCurves(gammas, phis, ds, curve1_lbl=r'$\varphi_0$', curve2_lbl=r'$d_0$',
                              curve1_color='darkcyan', curve2_color='darkorange')
    # draw amplitude dependency
    amp_figure_name = 'cubic_divergent_Au_x0={:.5},beta={:.5}'.format(x0, beta)
    drawer_amp = drawer.Drawer(x_label=r'$\gamma$', y_label='$A_u$',
                               figure_name=amp_figure_name, save_dir=SAVE_DIRECTORY)
    drawer_amp.drawAxis(show_Ox=True)
    drawer_amp.drawCurve(gammas, amps, curve_color='crimson')


if __name__ == '__main__':
    gammas = list(np.arange(g_min, g_max, utils.H))
    phis, ds, amps = get_Lyapunov_exps(gammas)
    draw_dependencies(gammas, phis, ds, amps)