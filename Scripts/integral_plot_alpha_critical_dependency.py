'''
Script for building and visualization alpha_u dependency (critical values of alpha,
when zero solution of LINEARIZED BOUNDARY-VALUE PROBLEM with INTEGRAL DEVIATION
in boundary conditions loses its stability in DIVERGENT way)
'''

import numpy as np
import drawer


g_min = -4.1
g_max = 4.1
n_gammas = 8201

SAVE_DIRECTORY = '../Tracer/Variations/Integral Boundary Condition'


if __name__ == '__main__':
    gammas = list(np.linspace(g_min, g_max, n_gammas))
    alphas_u = list(map(lambda x: -x, gammas))
    drawer_alphau = drawer.Drawer(x_label=r'$\gamma$', y_label=r'$\alpha_u$',
                                  save_dir=SAVE_DIRECTORY)
    drawer_alphau.drawAxis(show_Ox=True, show_Oy=True)
    drawer_alphau.drawCurve(gammas, alphas_u, curve_color='b')