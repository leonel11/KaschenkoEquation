'''

'''


import numpy as np
import pandas as pd
import drawer
import multiprocessing
import time
import utils

from functools import partial

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


NUMERICAL_METHODS = ['Euler', 'Runge-Kutta', 'Butcher']
COLUMNS = ['a', 'F']

x0 = 0.45
gamma = 6.89
alpha = -3.41417 #-3.41414
a_right = 0.6
delta_a = 2e-2

SAVE_DIRECTORY = f'../Tracer/Results/x0={x0:.2f}'
PROCESSES = 2*multiprocessing.cpu_count()
METHOD = 'Butcher'
DRAW_U_FUNCS = False


def get_numerical_method():
    if METHOD == 'Euler':
        return modified_Euler_method
    elif METHOD == 'Runge-Kutta':
        return method_Runge_Kutta
    elif METHOD == 'Butcher':
        return method_Butcher
    else:
        raise ValueError(f'Irrelevant numerical method! Choose one from the following: {NUMERICAL_METHODS}')


def get_func_val(u, v):
    return np.array([v, -gamma*u + u**3])


def modified_Euler_method(u, v):
    k1 = get_func_val(u, v)
    u12, v12 = np.array([u, v]) + utils.H * k1
    k2 = get_func_val(u12, v12)
    u, v = np.array([u, v]) + utils.H/2.0 * (k1 + k2)
    return u, v


def method_Runge_Kutta(u, v):
    k1 = get_func_val(u, v)
    u14, v14 = np.array([u, v]) + utils.H/2.0 * k1
    k2 = get_func_val(u14, v14)
    u12, v12 = np.array([u, v]) + utils.H/2.0 * k2
    k3 = get_func_val(u12, v12)
    u34, v34 = np.array([u, v]) + utils.H * k3
    k4 = get_func_val(u34, v34)
    u, v = np.array([u, v]) + utils.H/6.0 * (k1 + 2.0*k2 + 2.0*k3 + k4)
    return u, v


def method_Butcher(u, v):
    k1 = get_func_val(u, v)
    u17, v17 = np.array([u, v]) + utils.H/2.0 * k1
    k2 = get_func_val(u17, v17)
    u27, v27 = np.array([u, v]) + 2.0*utils.H/3.0 * k2
    k3 = get_func_val(u27, v27)
    u37, v37 = np.array([u, v]) + utils.H/3.0 * k3
    k4 = get_func_val(u37, v37)
    u47, v47 = np.array([u, v]) + 5.0*utils.H/6.0 * k4
    k5 = get_func_val(u47, v47)
    u57, v57 = np.array([u, v]) + utils.H/6.0 * k5
    k6 = get_func_val(u57, v57)
    u67, v67 = np.array([u, v]) + utils.H * k6
    k7 = get_func_val(u67, v67)
    u, v = np.array([u, v]) + utils.H * (k1*13.0/200.0 + k3*11.0/40.0 + k4*11.0/40.0 + k5*4.0/25.0 + k6*4.0/25.0 + k7*13.0/200.0)
    return u, v


def second_border_func_val(u, v=0.0, numerical_method=method_Runge_Kutta):
    u_x0, v1 = 0.0, 0.0
    xs = np.hstack((np.arange(0.0, x0-utils.EPS, utils.H),
                    np.arange(x0, 1.0-utils.EPS, utils.H),
                    np.array(1.0)))
    for x in xs:
        u, v = numerical_method(u, v)
        if x == x0:
            u_x0 = u
        if x == 1.0:
            v1 = v
    return v1 - alpha*u_x0


def second_border_func_val_multiproc(idx, a_values, v=0.0, numerical_method=method_Runge_Kutta):
    a = a_values[idx]
    fa = second_border_func_val(u=a, v=v, numerical_method=numerical_method)
    print(f'{multiprocessing.current_process().name}:\ta={a: <7g}\tF(a)={fa:.5f}')
    return dict(zip(COLUMNS, [a, fa]))


def build_original_u_func(u0=0.0, v0=0.0, numerical_method=method_Runge_Kutta):
    xs = np.arange(0.0, 1.0+utils.EPS, utils.H)
    us = []
    u, v = u0, v0
    for x in xs:
        if x == 0.0:
            us.append(u0)
        else:
            u, v = numerical_method(u, v)
            us.append(u)
    return xs, us


def flexible_bisection_root_search(a_left, f_left, a_right, f_right, numerical_method=method_Runge_Kutta):
    a12 = (a_left+a_right) / 2.0
    f12 = second_border_func_val(u=a12, v=0.0, numerical_method=numerical_method)
    if (f12 > utils.EPS):
        if f_left < 0 and f_right > 0:
            return flexible_bisection_root_search(a_left, f_left, a12, f12)
        else:
            return flexible_bisection_root_search(a12, f12, a_right, f_right)
    elif (f12 < -utils.EPS):
        if f_left < 0 and f_right > 0:
            return flexible_bisection_root_search(a12, f12, a_right, f_right)
        else:
            return flexible_bisection_root_search(a_left, f_left, a12, f12)
    else:
        return a12


if __name__ == '__main__':
    print('Calculating F(a)...')
    a_values = np.arange(0.0, a_right+utils.EPS, delta_a)
    a_indices = range(len(a_values))
    func_values = []
    numerical_method = get_numerical_method()
    start_time = time.clock()
    # Multiprocessing calculation of function
    func_values.extend(multiprocessing.Pool(processes=PROCESSES).map(
        partial(second_border_func_val_multiproc, a_values=a_values, numerical_method=numerical_method), a_indices))
    df = pd.DataFrame(func_values).sort_values(by=[COLUMNS[0]])
    a_s, f_s = tuple(map(lambda x: df[x].tolist(), COLUMNS))
    print(f'Elapsed time: {int(time.clock() - start_time)} sec\nSearching for roots...\na = 0')
    a_roots = [0.0]
    for idx in range(1, len(a_s)-1):
        a_left, f_left = a_s[idx], f_s[idx]
        a_right, f_right = a_s[idx+1], f_s[idx+1]
        if (f_left*f_right <= 0.0):
            a_star = flexible_bisection_root_search(a_left, f_left, a_right, f_right, numerical_method)
            print(f'a = {a_star:g}')
            a_roots.append(a_star)
    # draw function F(a)
    fa_pict = 'Fa_gamma={:.4}_alpha={:.5}'.format(gamma, alpha)
    dr = drawer.Drawer(x_label=COLUMNS[0], y_label=COLUMNS[1], figure_name=fa_pict, save_dir=SAVE_DIRECTORY)
    dr.drawAxis(show_Ox=True, show_Oy=True)
    #dr.drawPoints(a_roots, [0.0] * len(a_roots))
    dr.drawCurve(a_s, f_s, curve_color='chocolate', up=None, bottom=None)
    # draw function u(x) for each a_*
    if DRAW_U_FUNCS:
        if len(a_roots) > 1:
            for a_star in a_roots[1:]:
                xs, us = build_original_u_func(a_star)
                #print (us)
                u_pict = 'u(x)_gamma={:.4}_alpha={:.5}_a={:.4}'.format(gamma, alpha, a_star)
                dr = drawer.Drawer(x_label='x', y_label='u', figure_name=u_pict, save_dir=SAVE_DIRECTORY)
                dr.drawAxis(show_Ox=True, show_Oy=True)
                dr.drawCurve(xs, us, curve_color='slateblue', up=None, bottom=None)