'''
Script for building and visualization special sign function, which helps to find
alpha_c values (critical values of alpha, when zero solution of
LINEARIZED BOUNDARY-VALUE PROBLEM loses its stability in OSCILLATING way) and
corresponding omega values (imaginary part of purely imaginary eigenvalues)
in visual way by means of intersection sign function with Ox axis
'''

import numpy as np
import math
import drawer
import utils


x0 = 0.67
gamma = 15.98864
w_start = 75.4
w_end = 75.6
n_points = 100000


def get_sign_func_val(w):
    '''
    Calculate and return the value of sign function for visual search of alpha_c
    (oscillating case) for fixed gamma and x0
    :param w: omega value
    :return: value of sign function
    '''
    r = np.sqrt(np.sqrt(gamma*gamma+w*w))
    if gamma <= 0.0:
        t = np.arctan(-w/gamma)/2.0
    else:
        t = (math.pi - np.arctan(w/gamma)) / 2.0
    hi = r*np.cos(t)
    teta = r*np.sin(t)
    return (teta*np.sinh(hi)*np.cos(teta)+hi*np.cosh(hi)*np.sin(teta))/\
           (hi*np.sinh(hi)*np.cos(teta)-teta*np.cosh(hi)*np.sin(teta)) - \
           np.tanh(hi*x0)*np.tan(teta*x0)


def get_dict_roots(ws, ys):
    '''
    Form and return dictionary of roots, where sign function changes its sign
    (dict_key - omega value, dict_value - alpha_c (oscillating case) value)
    :param ws:
    :param ys:
    :return:
    '''
    res = {}
    for idx in range(1,len(ws)):
        if ys[idx-1]*ys[idx] < 0:
            w_star = (ws[idx-1]+ws[idx])/2.0
            res[str(w_star)] = utils.get_alpha_c(gamma, w_star, x0)
    return res


if __name__ == '__main__':
    print(f'gamma = {gamma}\n')
    ws = np.linspace(w_start, w_end, n_points)
    ys = [get_sign_func_val(w) for w in ws]
    # find roots
    star = get_dict_roots(ws, ys)
    print('w_star\talpha_c')
    for w, a in star.items():
        print('{:.9} {:.9}'.format(gamma, float(w), a))
    # draw function
    dr = drawer.Drawer(x_label=r'$\omega$')
    dr.drawAxis(show_Ox=True)
    dr.drawCurve(ws, ys, curve_color='k')