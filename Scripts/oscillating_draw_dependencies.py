'''
Script for building and visualization dependencies of Lyapunov exponents
(PHI and D values) and Amplitude of oscillations, when zero solution loses
its stability in the OSCILLATING way for BOUNDARY-VALUE PROBLEM
WITH LINEAR DEVIATION in boundary conditions
'''

import pandas as pd
import numpy as np
import drawer


x0 = 0.33
AFTER_TANGENT = False

SKIP_VALUES = 3 # for more handsome visualization
SUFFIX_NAME = '_after_tangent' if AFTER_TANGENT else ''
SAVE_DIRECTORY = f'../Tracer/Results/x0={x0:.2f}'
CSV_FILE = SAVE_DIRECTORY + f'/x0={x0:.2f}' +'_analytical.csv'
AFTER_TANGENT_FILE = SAVE_DIRECTORY + f'/x0={x0:.2f}' +'_analytical_after_tangent.csv'


def read_params():
    '''
    Read params for calculating of Lyapunov exponents
    :return list of gamma values, list of omega values, list of alpha values
    '''
    if AFTER_TANGENT:
        df = pd.read_csv(AFTER_TANGENT_FILE, sep=';')
        alphas = list(df['alpha_f'])
    else:
        df = pd.read_csv(CSV_FILE, sep=';')
        alphas = list(df['alpha_c'])
    gammas, omegas = list(df['gamma']), list(df['w'])
    if AFTER_TANGENT:
        return gammas[:-SKIP_VALUES], omegas[:-SKIP_VALUES], alphas[:-SKIP_VALUES]
    else:
        return gammas[SKIP_VALUES:], omegas[SKIP_VALUES:], alphas[SKIP_VALUES:]


def G(y, a, mu, x0):
    return (a*np.cosh(y*x0)-y*np.sinh(y))/(y*y-mu*mu)


def get_phi(g, a, w, x0):
    mu = np.sqrt(-g + w*1.0j)
    phi = -(2.0*mu*np.cosh(mu*x0))/(mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
    if AFTER_TANGENT:
        phi = -phi
    return phi.real


def get_d(g, a, w, x0):
    mu = np.sqrt(-g + w*1.0j)
    mu_conj = np.conj(mu)
    nu = mu + 2.0*1.0j*mu.imag
    kappa = mu + 2*mu.real
    B = 3*mu*(G(kappa, a, mu, x0) + G(nu, a, mu, x0) + 2*G(mu_conj, a, mu, x0))
    A = 2*(np.sinh(mu)+mu*np.cosh(mu)-a*x0*np.sinh(mu*x0))
    d = B/A
    return d.real


def get_Lyapunov_exps(gs, ws, alphs):
    '''
    Calculate and return lists of Lyapunov exponents
    :param gammas: list of gamma values
    :param ws: list of omega values
    :param alphas: list of alpha values
    :return: list of phi values, list of d values, list of amplitude values
    '''
    phis, ds, amps = [], [], []
    for idx in range(len(gammas)):
        g, w, a = gs[idx], ws[idx], alphs[idx]
        phis.append(get_phi(g, a, w, x0))
        ds.append(get_d(g, a, w, x0))
        amps.append(np.sqrt(abs(phis[-1]/ds[-1])))
    return phis, ds, amps


def draw_dependencies(gammas, phis, ds, amps):
    '''
    Draw 3 graphics: phi(gamma) dependency, d(gamma) dependency and amplitude(gamma) dependency
    :param gammas: list of gamma values
    :param phis: list of phis values
    :param ds: list of d values
    :param amps: list of amplitude values
    '''
    # draw phi dependency
    phi_pict = 'oscillating_phi0{}_x0={:.5}'.format(SUFFIX_NAME, x0)
    drawer_phi = drawer.Drawer(x_label=r'$\gamma$', y_label=r'$\varphi_0$',
                               figure_name=phi_pict, save_dir=SAVE_DIRECTORY)
    drawer_phi.drawAxis(show_Ox=True)
    drawer_phi.drawCurve(gammas, phis, curve_color='darkcyan')
    # draw d dependency
    d_pict = 'oscillating_d0{}_x0={:.5}'.format(SUFFIX_NAME, x0)
    drawer_d = drawer.Drawer(x_label=r'$\gamma$', y_label='$d_0$', figure_name=d_pict, save_dir=SAVE_DIRECTORY)
    drawer_d.drawAxis(show_Ox=True)
    drawer_d.drawCurve(gammas, ds, curve_color='orange')
    # draw amplitude dependency
    amp_pict = 'oscillating_pho_star_{}_x0={:.5}'.format(SUFFIX_NAME, x0)
    drawer_amp = drawer.Drawer(x_label=r'$\gamma$', y_label=r'$\rho_*$', figure_name=amp_pict, save_dir=SAVE_DIRECTORY)
    drawer_amp.drawAxis(show_Ox=True)
    drawer_amp.drawCurve(gammas, amps, curve_color='crimson')


if __name__ == '__main__':
    gammas, omegas, alphas = read_params()
    phis, ds, amps = get_Lyapunov_exps(gammas, omegas, alphas)
    draw_dependencies(gammas, phis, ds, amps)