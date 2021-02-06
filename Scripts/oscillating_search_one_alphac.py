'''
Script for automatic search of one alpha_c value (critical value of alpha, when
zero solution of LINEARIZED BOUNDARY-VALUE PROBLEM loses its stability
in OSCILLATING way) and corresponding omega values (imaginary part of
purely imaginary eigenvalues). Search is implemented for segment of omega values
and fixed gamma and x0
'''

import numpy as np
import math
import utils


x0 = 0.39
gamma = 6.41
w_pred = 10.014
w_start = 0.7*w_pred
w_end = 1.3*w_pred


def get_sign_func_val(w, x0):
    '''
    Calculate and return the value of sign function to search alpha_c
    (oscillating case) for fixed gamma and x0
    :param w: omega value
    :param x0: x0 value
    :return: value of sign function
    '''
    r = np.sqrt(np.sqrt(gamma*gamma+w*w))
    if gamma <= 0.0:
        t = np.arctan(-w/gamma)/2.0
    else:
        t = (math.pi - np.arctan(w/gamma)) / 2.0
    hi = r*np.cos(t)
    teta = r*np.sin(t)
    return (teta*np.sinh(hi)*np.cos(teta)+hi*np.cosh(hi)*np.sin(teta)) / \
           (hi*np.sinh(hi)*np.cos(teta)-teta*np.cosh(hi)*np.sin(teta)) - np.tanh(hi*x0)*np.tan(teta*x0)


if __name__ == '__main__':
    w = utils.dichotonomy_root_search(w_start, w_end, get_sign_func_val, x0=x0)
    print('{};{:.6};{:.6}'.format(gamma, w, utils.get_alpha_c(gamma, w, x0)))