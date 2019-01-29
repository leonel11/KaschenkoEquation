import numpy as np
import sys
import math


EPS = 0.000001
PI = math.pi


def sign_func(y):
    return np.tan(y) + np.tanh(y)


def omega_func(y):
    return float(2.0*y*y)


def alpha_func(y):
    return y*(np.sinh(y)*np.cos(y) - np.cosh(y)*np.sin(y))


def dichotonomy_root_search(left_border, right_border):
    y = (left_border + right_border) / 2.0
    f = sign_func(y)
    if (f > EPS):
        return dichotonomy_root_search(left_border, y)
    elif (f < -EPS):
        return dichotonomy_root_search(y, right_border)
    else:
        return y


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('Error: wrong call of script!\n')
        print('Right call: alpha_k.py k')
        print('k - amount of alpha_k')
    else:
        k = int(sys.argv[1])
        for i in range(0, k):
            left_border = max(0, i*PI-PI/2.0)
            right_border = i*PI + PI/2.0
            y_i = dichotonomy_root_search(left_border, right_border)
            w_i = omega_func(y_i)
            a_i = alpha_func(y_i)
            print('({:.4f}, {:.4f}):\ty={:.4f},\tw={:.4f},\ta={:.4f}'.format(left_border, right_border, y_i, w_i, a_i))