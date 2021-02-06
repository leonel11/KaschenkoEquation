'''
Script for search of initial origin values (alpha_c - critical values of alpha, when
zero solution of LINEARIZED BOUNDARY-VALUE PROBLEM loses its stability
in OSCILLATING way and corresponding omega values - imaginary part of
purely imaginary eigenvalues). Search of certain number (k - input parameter of script)
of origins is implemented on special segments of PI length starting -PI/2 value
'''

import numpy as np
import sys
import utils


def get_sign_func_val(y):
    '''
    Calculate and return value of sign function to search alpha_c
    (oscillating case) in case gamma=0, x0=0
    :param w: y value
    :return: value of sign function
    '''
    return np.tan(y) + np.tanh(y)


def get_omega(y):
    '''
    Calculate and return omega value in case gamma=0, x0=0
    :param y: y value
    :return: omega value
    '''
    return float(2.0*y*y)


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('Error: wrong call of script!\n')
        print('Right call: oscillating_origin0.py k')
        print('k - amount of alpha_k')
    else:
        k = int(sys.argv[1])
        for i in range(0, k):
            left_border = max(0, i*utils.PI-utils.PI/2.0)
            right_border = i*utils.PI + utils.PI/2.0
            y_i = utils.bisection_root_search(left_border, right_border, get_sign_func_val)
            w_i = get_omega(y_i)
            a_i = utils.get_alpha_c_origin(y_i, x0=0.0)
            print('({:.4f}, {:.4f}):\ty={:.4f},\tw={:.4f},\ta={:.4f}'.format(left_border, right_border, y_i, w_i, a_i))