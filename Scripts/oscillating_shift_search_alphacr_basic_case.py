import numpy as np
import math


EPS = 0.000001
gamma = 4.1
w_pred = 1.86053
w_start = 0.35*w_pred
w_end = 1.65*w_pred


def sign_func(w):
    r = np.sqrt(np.sqrt(gamma*gamma+w*w))
    if gamma <= 0.0:
        t = np.arctan(-w/gamma)/2.0
    else:
        t = (math.pi - np.arctan(w/gamma)) / 2.0
    return r*np.sin(t)*np.sinh(r*np.cos(t))*np.cos(r*np.sin(t)) + r*np.cos(t)*np.cosh(r*np.cos(t))*np.sin(r*np.sin(t))


def alpha_cr(w):
    r = np.sqrt(np.sqrt(gamma * gamma + w * w))
    if gamma <= 0.0:
        t = np.arctan(-w / gamma) / 2.0
    else:
        t = (math.pi - np.arctan(w / gamma)) / 2.0
    return r*np.cos(t)*np.sinh(r*np.cos(t))*np.cos(r*np.sin(t)) - r*np.sin(t)*np.cosh(r*np.cos(t))*np.sin(r*np.sin(t))


def dichotonomy_root_search(w_left, w_right):
    if sign_func(w_left)*sign_func(w_right) > 0:
        raise Exception('No roots')
    while True:
        w = (w_left+w_right)/2.0
        f = sign_func(w)
        f_left = sign_func(w_left)
        f_right = sign_func(w_right)
        if (f > EPS):
            if f_left < 0 and f_right > 0:
                return dichotonomy_root_search(w_left, w)
            else:
                return dichotonomy_root_search(w, w_right)
        elif (f < -EPS):
            if f_left < 0 and f_right > 0:
                return dichotonomy_root_search(w, w_right)
            else:
                return dichotonomy_root_search(w_left, w)
        else:
            return w


w = dichotonomy_root_search(w_start, w_end)
print('{};{:.6};{:.6}'.format(gamma, w, alpha_cr(w)))