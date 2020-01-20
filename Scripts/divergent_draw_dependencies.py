'''
Script for building and visualization dependencies of Lyapunov exponents
(PHI and D values) and Amplitude of oscillations, when zero solution loses
its stability in the DIVERGENT way for BOUNDARY-VALUE PROBLEM
WITH LINEAR DEVIATION in boundary conditions
'''

import numpy as np
import drawer
import utils


x0 = 0.5
g_min = 5.0
g_max = 16.0

SAVE_DIRECTORY = '../Tracer/Results' + f'/x0={x0:.2f}'


def get_phi(g, a, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        A = mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0)
        B = 2*mu*np.cosh(mu*x0)
    else:
        mu = np.sqrt(g)
        A = mu*np.cos(mu) + np.sin(mu) - a*x0*np.sin(mu*x0)
        B = 2*mu*np.cos(mu*x0)
    return B/A


def get_d(g, a, x0):
    if g <= 0:
        mu = np.sqrt(-g)
        A = 16*(mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
        B = -3*mu*mu*np.sinh(3*mu) - 12*np.sinh(mu) - 12*mu*np.cosh(mu) - \
            a*mu*np.cosh(3*mu*x0) + 12*a*x0*np.sinh(mu*x0)
    else:
        mu = np.sqrt(g)
        A = 16*(mu*np.cos(mu) + np.sin(mu) - a*x0*np.sin(mu*x0))
        B = 3*mu*mu*np.sin(3*mu) - 12*np.sin(mu) - 12*mu*np.cos(mu) - \
            a*mu*np.cos(3*mu*x0) + 12*a*x0*np.sin(mu*x0)
    return B/A


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
        phis.append(phi0)
        ds.append(d0)
        amps.append(utils.get_amplitude(phi0, d0))
    return phis, ds, amps


def draw_dependencies(gammas, phis, ds, amps):
    '''
    Draw 2 graphics: phi(gamma), d(gamma) dependencies and amplitude(gamma) dependency
    :param gammas: list of gamma values
    :param phis: list of phis values
    :param ds: list of d values
    :param amps: list of amplitude values
    '''
    # draw phi, d dependencies
    phid_figure_name = 'divergent_phi0d0_x0={:.5},g[{:.5},{:.5}]'.format(x0, g_min, g_max)
    drawer_phid = drawer.Drawer(x_label=r'$\gamma$',
                                figure_name=phid_figure_name,
                                save_dir=SAVE_DIRECTORY)
    drawer_phid.drawAxis(show_Ox=True)
    drawer_phid.drawTwoCurves(gammas, phis, ds, curve1_lbl=r'$\varphi_0$',
                              curve2_lbl=r'$d_0$', curve1_color='darkcyan',
                              curve2_color='darkorange')
    # draw amplitude dependency
    amp_figure_name = 'divergent_amplitude_x0={:.5},g[{:.5},{:.5}]'.format(x0, g_min, g_max)
    drawer_amp = drawer.Drawer(x_label=r'$\gamma$', y_label='$A_u$',
                               figure_name=amp_figure_name,
                               save_dir=SAVE_DIRECTORY)
    drawer_amp.drawAxis(show_Ox=True)
    drawer_amp.drawCurve(gammas, amps, curve_color='crimson')


if __name__ == '__main__':
    gammas = list(np.arange(g_min, g_max, utils.H))
    phis, ds, amps = get_Lyapunov_exps(gammas)
    utils.print_change_sign_d_points(gammas, ds)
    draw_dependencies(gammas, phis, ds, amps)