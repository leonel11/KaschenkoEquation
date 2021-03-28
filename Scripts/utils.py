'''
Some functions for common usage
'''

import numpy as np
import math
import drawer

from contextlib import contextmanager
from time import time


EPS = 1e-6
H = 1e-5 #1e-3
MAX = 1e6
PI = math.pi


@contextmanager
def time_measure():
    start_time = time()
    yield
    print(f'Elapsed time: {int(time() - start_time)} sec')


def get_alpha_u(gamma, x0):
    '''
    Calculate and return alpha_u(gamma) (divergent case) values for fixed x0
    :param gamma: gamma value
    :param x0: x0 value
    :return: alpha_u(gamma) value for fixed x0
    '''
    if gamma <= 0:
        mu = np.sqrt(-gamma)
        return mu*np.sinh(mu)/np.cosh(mu*x0)
    else:
        mu = np.sqrt(gamma)
        return -mu*np.sin(mu)/np.cos(mu*x0)


def get_alpha_c(gamma, w, x0):
    '''
    Calculate and return alpha_c(gamma) (oscillating case) values for fixed x0
    :param gamma: gamma value
    :param w: omega value
    :param x0: x0 value
    :return: alpha_c(gamma) for fixed x0
    '''
    r = np.sqrt(np.sqrt(gamma*gamma + w*w))
    if gamma <= 0.0:
        t = np.arctan(-w/gamma) / 2.0
    else:
        t = (math.pi - np.arctan(w/gamma)) / 2.0
    hi = r*np.cos(t)
    teta = r*np.sin(t)
    return (hi*np.sinh(hi)*np.cos(teta) - teta*np.cosh(hi)*np.sin(teta)) / (np.cosh(hi*x0)*np.cos(teta*x0))


def get_alpha_c_origin(y, x0):
    '''
    Calculate and return origin alpha_c (oscillating case) value for gamma=0
    :param y: y_value
    :param x0: x0 value
    :return: origin alpha_c value
    '''
    return (y*np.sinh(y)*np.cos(y)-y*np.cosh(y)*np.sin(y))/(np.cosh(y*x0)*np.cos(y*x0))


def get_gamma_local_min(gammas, alphas):
    '''
    Return gamma value for local minimum of alpha values
    :param gammas: list of gamma values
    :param alphas: list of alpha values
    :return: gamma value for local minimum of alpha values
    '''
    g_idx = alphas.index(get_alpha_min(alphas))
    return gammas[g_idx]


def get_alpha_min(alphas):
    '''
    Return minimum of alpha values
    :param alphas: list of alpha values
    :return: minimum of alpha values
    '''
    return min(alphas)


def get_amplitude(phi, d):
    '''
    Calculate and return the value of amplitude
    :param phi: phi value
    :param d: d value
    :return: value of amplitude
    '''
    return np.sqrt(abs(phi/d))


def print_change_sign_d_points(gammas, ds):
    '''
    Print gamma values, where d(gamma) change its sign
    :param gammas: list of gamma values
    :param ds: list of d values
    :return: gamma values, where d(gamma) change its sign
    '''
    d0_prev = 0.0
    print('Gammas, where d0 changes the sign:')
    for g, d0 in zip(gammas, ds):
        if d0_prev*d0 < 0:
            print(g)
        d0_prev = d0


def bisection_root_search(left_border, right_border, func, **kwargs):
    '''
    Algorithm of root search (bisection method)
    (URL: https://en.wikipedia.org/wiki/Bisection_method)
    :param left_border: left value of segment for search of root
    :param right_border: right value of segment for search of root
    :param func: sign function
    :param kwargs: arguments of sign function
    :return: root
    '''
    y = (left_border + right_border) / 2.0
    f = func(y, **kwargs)
    if (f > EPS):
        return bisection_root_search(left_border, y, func, **kwargs)
    elif (f < -EPS):
        return bisection_root_search(y, right_border, func, **kwargs)
    else:
        return y


def dichotonomy_root_search(left_border, right_border, func, **kwargs):
    '''
    Algorithm of root search (dichotonomy method)
    (URL: https://www.encyclopediaofmath.org/index.php/Dichotomy_method)
    :param left_border: left value of segment for search of root
    :param right_border: right value of segment for search of root
    :param func: sign function
    :param kwargs: arguments of sign function
    :return: root
    '''
    if func(left_border, **kwargs)*func(right_border, **kwargs) > 0:
        raise Exception('No roots')
    while True:
        y = (left_border+right_border)/2.0
        f = func(y, **kwargs)
        f_left = func(left_border, **kwargs)
        f_right = func(right_border, **kwargs)
        if abs(f_left) > MAX and abs(f_right) > MAX:
            return y
        if (f > EPS):
            if f_left < 0 and f_right > 0:
                return dichotonomy_root_search(left_border, y, func, **kwargs)
            else:
                return dichotonomy_root_search(y, right_border, func, **kwargs)
        elif (f < -EPS):
            if f_left < 0 and f_right > 0:
                return dichotonomy_root_search(y, right_border, func, **kwargs)
            else:
                return dichotonomy_root_search(left_border, y, func, **kwargs)
        else:
            return y


# variables only for inner usage
_x0 = 0.45
_g_min = 6.8
_g_max = 6.9
_points = 11

# only for inner usage
if __name__ == '__main__':
    _gammas = np.linspace(_g_min, _g_max, _points)
    _alphas_u = [get_alpha_u(g, _x0) for g in _gammas]
    print('\tgamma\talpha')
    for idx in range(len(_gammas)):
        print('{:>9.6} {:>9.6}'.format(_gammas[idx], _alphas_u[idx]))
    _g_loc = get_gamma_local_min(_gammas, _alphas_u)
    _a_loc = get_alpha_min(_alphas_u)
    if _g_loc != _gammas[-1]:
        print('\na_loc_min = {:.12}'.format(_a_loc))
        print('g_loc = {:.12}'.format(_g_loc))
    drawer_alphau = drawer.Drawer(x_label=r'$\gamma$', y_label=r'$\alpha_u$')
    drawer_alphau.drawCurve(_gammas, _alphas_u, curve_color='b')