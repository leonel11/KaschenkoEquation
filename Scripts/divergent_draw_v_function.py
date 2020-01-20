'''
Script for building and visualization of v(x) function for fixed x0 and gamma
(DIVERGENT case of eigenfunction)
'''

import numpy as np
import drawer


x0 = 0.0
gamma = 5.1


def get_v_func_val(g, x):
    '''
    Calculate and return value of v(x) for fixed gamma
    :param g: fixed gamma value
    :param x: x value
    :return: v(x) for fixed gamma
    '''
    if g <= 0:
        mu = np.sqrt(-g)
        return np.cosh(mu*x)
    else:
        mu = np.sqrt(g)
        return np.cos(mu*x)


if __name__ == '__main__':
    xs = np.linspace(0, 1, 10000)
    vs = [get_v_func_val(gamma, x) for x in xs]
    # draw v function
    v_figure_name = 'x0={:.2}__g={:.4}'.format(x0, gamma)
    drawer_v = drawer.Drawer(x_label='x', y_label='v', figure_name=v_figure_name)
    drawer_v.drawCurve(xs, vs, curve_color='slateblue')