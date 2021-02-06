'''
Script for automatic search of alpha_c values (critical values of alpha, when
zero solution of LINEARIZED BOUNDARY-VALUE PROBLEM loses its stability
in OSCILLATING way) and corresponding omega values (imaginary part of
purely imaginary eigenvalues). Step-by-step search is implemented by gamma values
'''

import numpy as np
import math
import utils


x0 = 0.91
gamma_start = 394.9
gamma_end = 800.0
w_pred = 374.107


def get_sign_func_val(w):
    '''
    Calculate and return value of sign function to search alpha_c
    (oscillating case) value
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
    return (teta*np.sinh(hi)*np.cos(teta)+hi*np.cosh(hi)*np.sin(teta)) / \
           (hi*np.sinh(hi)*np.cos(teta)-teta*np.cosh(hi)*np.sin(teta)) - np.tanh(hi*x0)*np.tan(teta*x0)


def output_data(out_data):
    '''
    Print gamma and corresponding omega and alpha_c (oscillating case) values
    :param out_data: data for output
    '''
    dict_keys = list(sorted(out_data.keys(), reverse=True))
    for gamma in dict_keys:
        w, alpha_c = out_data[gamma][0], out_data[gamma][1]
        print('{:.6};{:.6};{:.6}'.format(gamma, w, alpha_c))


if __name__ == '__main__':
    gamma = gamma_start + utils.H
    out_data = {}
    while abs(gamma) <= abs(gamma_end):
        w_start = 0.9*w_pred
        w_end = 1.1*w_pred
        try:
            w_pred = utils.dichotonomy_root_search(w_start, w_end, get_sign_func_val)
        except:
            output_data(out_data)
            exit(1)
        else:
            out_data[gamma] = [w_pred, utils.get_alpha_c(gamma, w_pred, x0)]
        gamma += utils.H
    output_data(out_data)