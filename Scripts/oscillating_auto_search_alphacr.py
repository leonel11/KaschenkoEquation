import numpy as np
import math


EPS = 0.000001
X_0 = 0.25
gamma_start = 0.0
gamma_end = -4.2
h = -0.1
w_pred = 16.156


def sign_func(w):
    r = np.sqrt(np.sqrt(gamma*gamma+w*w))
    if gamma <= 0.0:
        t = np.arctan(-w/gamma)/2.0
    else:
        t = (math.pi - np.arctan(w/gamma)) / 2.0
    hi = r*np.cos(t)
    teta = r*np.sin(t)
    return (teta*np.sinh(hi)*np.cos(teta)+hi*np.cosh(hi)*np.sin(teta))/(hi*np.sinh(hi)*np.cos(teta)-teta*np.cosh(hi)*np.sin(teta)) - np.tanh(hi*X_0)*np.tan(teta*X_0)


def alpha_cr(w):
    r = np.sqrt(np.sqrt(gamma*gamma + w*w))
    if gamma <= 0.0:
        t = np.arctan(-w/gamma)/2.0
    else:
        t = (math.pi - np.arctan(w/gamma))/2.0
    hi = r*np.cos(t)
    teta = r*np.sin(t)
    return (hi*np.sinh(hi)*np.cos(teta)-teta*np.cosh(hi)*np.sin(teta))/(np.cosh(hi*X_0)*np.cos(teta*X_0))


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


def output_data(out_data):
    dict_keys = list(sorted(out_data.keys(), reverse=True))
    for gamma in dict_keys:
        w, alpha_c = out_data[gamma][0], out_data[gamma][1]
        print('{:.3};{:.6};{:.6}'.format(gamma, w, alpha_c))


gamma = gamma_start + h
out_data = {}
while abs(gamma) <= abs(gamma_end):
    w_start = 0.9*w_pred
    w_end = 1.1*w_pred
    try:
        w_pred = dichotonomy_root_search(w_start, w_end)
    except:
        output_data(out_data)
        exit(1)
    else:
        out_data[gamma] = [w_pred, alpha_cr(w_pred)]
    gamma += h
output_data(out_data)