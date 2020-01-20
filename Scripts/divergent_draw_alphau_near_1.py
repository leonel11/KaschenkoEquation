'''
Script for building and visualization alpha_u dependency (critical values of alpha,
when zero solution of LINEARIZED BOUNDARY-VALUE PROBLEM loses its stability
in DIVERGENT way) and alpha_1 dependency (LINEARIZED BOUNDARY-VALUE PROBLEM for x0=1)
'''

import numpy as np
import matplotlib.pyplot as plt
import utils


plt.rcParams['savefig.directory'] = '../Tracer/Results'

x0 = 0.98
g_min = 2.0
g_max = 3.0
n_points = 1000


def get_alpha_1(g):
    '''
    Calculate and return critical value of alpha in the case x0=1
    :param g: gamma value
    :return: alpha_1 value
    '''
    if g <= 0:
        mu = np.sqrt(-g)
        return mu*np.tanh(mu)
    else:
        mu = np.sqrt(g)
        return -mu*np.tan(mu)


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
    draw_axis()


def draw_alphas(gammas, au, a1):
    '''
    Draw graphic of alpha_u(gamma) (divergent case) and  alpha_1(gamma) (x0=1)
    dependencies
    :param gammas: list of gamma values
    :param au: list of alpha_u values
    :param a1: list of alpha_1 values
    '''
    plt.figure('comparison_au_a1_x0={:.5},g[{:.5},{:.5}]'.format(x0, g_min, g_max))
    prepare_plot()
    plt.plot(gammas, au, label=r'$\alpha_u$', color='b', linewidth=2)
    plt.plot(gammas, a1, label=r'$\alpha_1$', color='y', linewidth=2)
    x1, x2, y1, y2 = plt.axis()
    y1, y2 = -50.0, 50.0
    plt.axis((x1, x2, y1, y2))
    plt.legend()
    plt.show()


if __name__ == '__main__':
    gammas = np.linspace(g_min, g_max, n_points)
    au, a1 = [], []
    for g in gammas:
        au.append(utils.get_alpha_u(g, x0))
        a1.append(get_alpha_1(g))
    prepare_plot()
    draw_alphas(gammas, au, a1)