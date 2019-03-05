import numpy as np
import matplotlib.pyplot as plt
import math


EPS = 0.000001
x0_begin = 0.0
x0_end = 1.0
count_origins = 101
w_prev = 11.187


def sign_func(y, x0):
    return (np.sinh(y)*np.cos(y) + np.cosh(y)*np.sin(y))/(np.sinh(y)*np.cos(y) - np.cosh(y)*np.sin(y)) - \
           np.tanh(y*x0)*np.tan(y*x0)


def dichotonomy_root_search(y_left, y_right, x0):
    if sign_func(y_left, x0)*sign_func(y_right, x0) > 0:
        raise Exception('No roots')
    while True:
        y = (y_left+y_right)/2.0
        f = sign_func(y, x0)
        f_left = sign_func(y_left, x0)
        f_right = sign_func(y_right, x0)
        if abs(f_left) > 1000000 and abs(f_right) > 1000000:
            return y
        if (f > EPS):
            if f_left < 0 and f_right > 0:
                return dichotonomy_root_search(y_left, y, x0)
            else:
                return dichotonomy_root_search(y, y_right, x0)
        elif (f < -EPS):
            if f_left < 0 and f_right > 0:
                return dichotonomy_root_search(y, y_right, x0)
            else:
                return dichotonomy_root_search(y_left, y, x0)
        else:
            return y


def get_alpha_cr(y, x0):
    return (y*np.sinh(y)*np.cos(y)-y*np.cosh(y)*np.sin(y))/(np.cosh(y*x0)*np.cos(y*x0))


xs = np.linspace(x0_begin, x0_end, count_origins)
print('x0;w;a')
for x0 in xs[1:]:
    y_prev = np.sqrt(w_prev/2.0)
    y_left, y_right = 0.96*y_prev, 1.04*y_prev
    y = dichotonomy_root_search(y_left, y_right, x0)
    w = 2.0*y*y
    a = get_alpha_cr(y, x0)
    print('{:.7};{:.7};{:.7}'.format(x0,w,a))
    w_prev = w