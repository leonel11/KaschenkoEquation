'''
Script for automatic search of one alpha_c value (critical value of alpha, when
zero solution of LINEARIZED BOUNDARY-VALUE PROBLEM loses its stability
in OSCILLATING way) and corresponding omega values (imaginary part of
purely imaginary eigenvalues). Search is implemented for segment of omega values
and fixed gamma and x0=0
'''

import numpy as np
import math
import utils


gamma = 4.1
w_pred = 1.86053
w_start = 0.35*w_pred
w_end = 1.65*w_pred


def get_sign_func_val(w):
    '''
    Calculate and return the value of sign function to search alpha_c
    (oscillating case) for fixed gamma and x0=0
    :param w: omega value
    :return: value of sign function
    '''
    r = np.sqrt(np.sqrt(gamma*gamma+w*w))
    if gamma <= 0.0:
        t = np.arctan(-w/gamma)/2.0
    else:
        t = (math.pi - np.arctan(w/gamma)) / 2.0
    return r*np.sin(t)*np.sinh(r*np.cos(t))*np.cos(r*np.sin(t)) + \
           r*np.cos(t)*np.cosh(r*np.cos(t))*np.sin(r*np.sin(t))


if __name__ == '__main__':
    w = utils.dichotonomy_root_search(w_start, w_end, get_sign_func_val)
    print('{};{:.6};{:.6}'.format(gamma, w, utils.get_alpha_c(gamma, w, x0=0.0)))