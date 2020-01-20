'''
Script for building and visualization dependencies of Lyapunov exponents
(PHI and D values) and Amplitude of oscillations, when zero solution loses
its stability in the DIVERGENT way for LINEAR BOUNDARY-VALUE PROBLEM
WITH INTEGRAL DEVIATION in boundary conditions
'''

import numpy as np
import drawer
import utils


g_min = -4.0
g_max = 120.0
h = 0.001

SAVE_DIRECTORY = '../Tracer/Variations/Integral Boundary Condition'


def get_d(g):
    if g < 0:
        return -5.0*g*np.sinh(3.0*np.sqrt(-g))/(48.0*np.sinh(np.sqrt(-g))) - 0.75
    else:
        return -5.0*g*np.sin(3.0*np.sqrt(g))/(48.0*np.sin(np.sqrt(g))) - 0.75


def draw_dependencies(gammas, ds, amps):
    '''
    Draw 2 graphics: d(gamma) dependency and amplitude(gamma) dependency
    :param gammas: list of gamma values
    :param ds: list of d values
    :param amps: list of amplitude values
    '''
    # draw d dependency
    d_figure_name = 'integral_divergent_d0_g[{:.5},{:.5}]'.format(g_min, g_max)
    drawer_d = drawer.Drawer(x_label=r'$\gamma$', y_label='d',
                             figure_name=d_figure_name, save_dir=SAVE_DIRECTORY)
    drawer_d.drawAxis(show_Ox=True)
    drawer_d.drawCurve(gammas, ds, curve_color='darkorange')
    # draw amplitude dependency
    amp_figure_name = 'divergent_A_g[{:.5},{:.5}]'.format(g_min, g_max)
    drawer_amp = drawer.Drawer(x_label=r'$\gamma$', y_label='$A_u$',
                               figure_name=amp_figure_name,
                               save_dir=SAVE_DIRECTORY)
    drawer_amp.drawAxis(show_Ox=True)
    drawer_amp.drawCurve(gammas, amps, curve_color='crimson')


if __name__ =='__main__':
    gammas = list(np.arange(g_min, g_max, h))
    ds = [get_d(g) for g in gammas]
    amps = [np.sqrt(1.0/abs(d)) for d in ds]
    utils.print_change_sign_d_points(gammas, ds)
    draw_dependencies(gammas, ds, amps)