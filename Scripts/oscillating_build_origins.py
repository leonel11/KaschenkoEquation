'''
Script for automatic search of origin values (alpha_c - critical values of alpha, when
zero solution of LINEARIZED BOUNDARY-VALUE PROBLEM loses its stability
in OSCILLATING way and corresponding omega values - imaginary part of
purely imaginary eigenvalues). Step-by-step search of certain number (count_origins)
of origins is implemented by x0 values, starting from x0_begin and w_prev
(corresponding origin value of omega for x0=x0_begin) and ending with x0_end.
'''

import numpy as np
import utils


x0_begin = 0.86
x0_end = 0.89
count_origins = 4
w_prev = 656.999


def get_sign_func_val(y, x0):
    '''
    Calculate and return value of sign function to search origin (omega, alpha_c)
    values for further calculations
    :param y: y value
    :param x0: x0 value
    :return: value of sign function
    '''
    return (np.sinh(y)*np.cos(y) + np.cosh(y)*np.sin(y)) / \
           (np.sinh(y)*np.cos(y) - np.cosh(y)*np.sin(y)) - \
           np.tanh(y*x0)*np.tan(y*x0)


if __name__ =='__main__':
    xs = np.linspace(x0_begin, x0_end, count_origins)
    print('x0;y;w;a')
    for x0 in xs[1:]:
        y_prev = np.sqrt(w_prev/2.0)
        y_left, y_right = 0.98*y_prev, 1.1*y_prev
        y = utils.dichotonomy_root_search(y_left, y_right,
                                          get_sign_func_val, x0=x0)
        w = 2.0*y*y
        a = utils.get_alpha_c_origin(y, x0)
        print('{:.7};{:.7};{:.7};{:.7}'.format(x0,y,w,a))
        w_prev = w