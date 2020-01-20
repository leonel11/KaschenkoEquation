'''
Script for visualization all critical dependencies of alpha values
(for DIVERGENT and 2 OSCILLATING cases of loss stability of zero solution)
for LINEARIZED BOUNDARY-VALUE PROBLEM
'''

import pandas as pd
import matplotlib.pyplot as plt
import os
import utils


x0 = 0.45
AFTER_TANGENT = True

DATA_PATH = f'../Tracer/Results/x0={x0:.2f}'
CSV_FILE = DATA_PATH + '_analytical.csv'
AFTER_TANGENT_FILE = DATA_PATH + '_analytical_after_tangent.csv'


def read_params():
    '''
    Read params for visualization
    :return list of gamma values, list of alpha_u (divergent case) values,
            list of alpha_c (oscillating case) values,
            list of gamma_f values, list of alpha_f values <-- oscillating case after fork
    '''
    df = pd.read_csv(CSV_FILE, sep=';')
    gammas = list(df['gamma'])
    alphas_c = list(df['alpha_c'])
    gammas_f, alphas_f = [], []
    if AFTER_TANGENT:
        if os.path.exists(AFTER_TANGENT_FILE):
            df_f = pd.read_csv(AFTER_TANGENT_FILE, sep=';')
            gammas_f = list(df_f['gamma'])
            alphas_f = list(df_f['alpha_f'])
    alphas_u = [utils.get_alpha_u(g, x0) for g in gammas]
    return gammas, alphas_u, alphas_c, gammas_f, alphas_f


def draw_axis(show_Ox=False, show_Oy = False):
    '''
    Draw axis Ox, Oy on the graphic
    :param show_Ox: is abscissa axis should be drawn
    :param show_Oy: is ordinate axis should be drawn
    '''
    if show_Ox:
        plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    if show_Oy:
        plt.axvline(x=0.0, linewidth=2, color='grey', zorder=2)


def prepare_plot():
    '''
    Set some settings of visualization for the field of graphics
    '''
    plt.rcParams.update({'font.size': 13})
    plt.subplots_adjust(left=0.11, bottom=0.11, right=0.94, top=0.94)
    plt.xlabel('$\gamma$')
    plt.grid(True)
    draw_axis(show_Ox=True, show_Oy=True)


def draw_alphas(gs, aus, acs, gfs, afs):
    '''
    Draw graphic of alpha_u(gamma) (divergent case), alpha_c(gamma) and
    alpha_f(gamma_f) (oscillating case) dependencies
    :param gs: list of gamma values
    :param aus: list of alpha_u values
    :param acs: list of alpha_c values
    :param gfs: list of gamma_f values
    :param afs: list of alpha_f values
    :param afs: list of alpha_f values
    '''
    prepare_plot()
    plt.plot(gs, aus, label=r'$\alpha_u$', color='royalblue', linewidth=2,
             zorder=4)
    plt.plot(gs, acs, label=r'$\alpha_c$', color='red', linewidth=2, zorder=4)
    if AFTER_TANGENT:
        plt.plot(gfs, afs, label=r'$\alpha_f$', color='olive', linewidth=2,
                 zorder=3)
        plt.scatter(gfs[-1], afs[-1], color='black', s=14, zorder=5)
    plt.legend(loc='lower right')
    plt.scatter(gs[0], acs[0], color='black', s=14, zorder=5)
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2, y1, y2))
    plt.savefig(os.path.join(DATA_PATH, f'alphas_{x0:.2f}.png'))
    plt.show()


if __name__ == '__main__':
    gammas, alphas_u, alphas_c, gammas_f, alphas_f = read_params()
    print('right(alpha_u) = {:.5}'.format(alphas_u[0]))
    print('min(alpha_u) = {:.5}'.format(utils.get_alpha_min(alphas_u)))
    draw_alphas(gammas, alphas_u, alphas_c, gammas_f, alphas_f)