'''
Script for building and visualization dependencies of Lyapunov exponents
(PHI and D values) and Amplitude of oscillations, when zero solution loses
its stability in the OSCILLATING way for LINEAR BOUNDARY-VALUE PROBLEM
WITH CUBIC DEVIATION in boundary conditions
'''

import pandas as pd
import numpy as np
import os
import drawer
import utils


beta = -1.0
x0 = 0.49
AFTER_TANGENT = True

SKIP_VALUES = 9 # for more handsome visualization
SUFFIX_NAME = '_after_tangent' if AFTER_TANGENT else ''
SAVE_DIRECTORY = '../Tracer/Variations/Cubic Boundary Condition' + f'/x0={x0:.2f}'
CSV_FILE = f'x0={x0:.2f}' + '_analytical' + SUFFIX_NAME + '.csv'


def read_params():
    '''
    Read params for calculating of Lyapunov exponents
    :return list of gamma values, list of omega values, list of alpha values
    '''
    df = pd.read_csv(os.path.join(SAVE_DIRECTORY, CSV_FILE), sep=';')
    gammas, omegas = list(df['gamma']), list(df['w'])
    if AFTER_TANGENT:
        alphas = list(df['alpha_f'])
    else:
        alphas = list(df['alpha_c'])
    if AFTER_TANGENT:
        return gammas[:-SKIP_VALUES], omegas[:-SKIP_VALUES], alphas[:-SKIP_VALUES]
    else:
        return gammas[SKIP_VALUES:], omegas[SKIP_VALUES:], alphas[SKIP_VALUES:]


def get_phi(g, w, a, x0):
    mu = np.sqrt(-g + w*1.0j)
    phi = -2.0*mu*np.cosh(mu*x0) / (mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
    if AFTER_TANGENT:
        phi = -phi
    return phi.real


def get_d(g, w, a, x0):
    mu = np.sqrt(-g + w*1.0j)
    mu_conj = np.conj(mu)
    nu = mu + 2.0*1.0j*mu.imag
    kappa = mu + 2.0*mu.real
    d = 1.5*beta*mu*(np.cosh(kappa*x0) + np.cosh(nu*x0) + 2.0*np.cosh(mu_conj*x0)) / \
        (mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
    return d.real


def get_Lyapunov_exps(gs, ws, alphas):
    '''
    Calculate and return lists of Lyapunov exponents
    :param gammas: list of gamma values
    :param ws: list of omega values
    :param alphas: list of alpha values
    :return: list of phi values, list of d values, list of amplitude values
    '''
    phis, ds, amps = [], [], []
    for g, w, a in zip(gs, ws, alphas):
        phi0, d0 = get_phi(g, w, a, x0), get_d(g, w, a, x0)
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
    phid_figure_name = 'cubic_oscillating_phi0d0{}_x0={:.5},beta={:.5}'.format(SUFFIX_NAME, x0, beta)
    drawer_phid = drawer.Drawer(x_label=r'$\gamma$', figure_name=phid_figure_name, save_dir=SAVE_DIRECTORY)
    drawer_phid.drawAxis(show_Ox=True)
    drawer_phid.drawTwoCurves(gammas, phis, ds, r'$\varphi_0$', r'$d_0$', 'darkcyan', 'darkorange')
    # draw amplitude dependency
    amp_figure_name = 'cubic_oscillating_pho_star{}_x0={:.5},beta={:.5}'.format(SUFFIX_NAME, x0, beta)
    drawer_amp = drawer.Drawer(x_label=r'$\gamma$', y_label=r'$\rho_*$',
                               figure_name=amp_figure_name, save_dir=SAVE_DIRECTORY)
    drawer_amp.drawAxis(show_Ox=True)
    drawer_amp.drawCurve(gammas, amps, curve_color='crimson')


if __name__ == '__main__':
    gammas, omegas, alphas = read_params()
    phis, ds, amps = get_Lyapunov_exps(gammas, omegas, alphas)
    draw_dependencies(gammas, phis, ds, amps)