'''
Research zero stability by means of special function
'''


import numpy as np
import drawer
import time
import utils

from tqdm import tqdm


x0 = 0.45
gamma = 6.89
alpha = -3.41417 #-3.41414
a_right = 0.6
delta_a = 1e-2

SAVE_DIRECTORY = f'../Tracer/Results/x0={x0:.2f}'
DRAW_U_FUNCS = False


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


def second_border_func_val(u, v):
    u_x0, v1 = 0.0, 0.0
    xs = np.hstack((np.arange(0.0, x0-utils.EPS, utils.H),
                    np.arange(x0, 1.0-utils.EPS, utils.H),
                    np.array(1.0)))
    for x in xs:
        u, v = method_Runge_Kutta(u, v) #modified_Euler_method(u, v)
        if x == x0:
            u_x0 = u
        if x == 1.0:
            v1 = v
    return v1 - alpha*u_x0


def build_original_u_func(u0=0.0, v0=0.0):
    xs = np.arange(0.0, 1.0+utils.EPS, utils.H)
    us = []
    u, v = u0, v0
    for x in xs:
        if x == 0.0:
            us.append(u0)
        else:
            u, v = method_Runge_Kutta(u, v) #modified_Euler_method(u, v)
            us.append(u)
    return xs, us


def flexible_bisection_root_search(a_left, f_left, a_right, f_right):
    a12 = (a_left+a_right) / 2.0
    f12 = second_border_func_val(u=a12, v=0.0)
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
    a_values = np.arange(0.0, a_right+utils.EPS, delta_a)
    func_values = []
    with utils.time_measure():
        for _, a in tqdm(enumerate(a_values), total=len(a_values)):
            f_a = second_border_func_val(u=a, v=0.0)
            func_values.append(f_a)
    print('Roots:\na = 0.0')
    a_roots = [0.0]
    for idx in range(1, len(a_values)-1):
        a_left, f_left = a_values[idx], func_values[idx]
        a_right, f_right = a_values[idx+1], func_values[idx+1]
        if (f_left*f_right <= 0.0):
            a_star = flexible_bisection_root_search(a_left, f_left, a_right, f_right)
            print(f'a = {a_star}')
            a_roots.append(a_star)
    # draw function F(a)
    fa_pict = 'Fa_gamma={:.4}_alpha={:.5}'.format(gamma, alpha)
    dr = drawer.Drawer(x_label='a', y_label='F', figure_name=fa_pict, save_dir=SAVE_DIRECTORY)
    dr.drawAxis(show_Ox=True, show_Oy=True)
    #dr.drawPoints(a_roots, [0.0] * len(a_roots))
    dr.drawCurve(a_values, func_values, curve_color='chocolate',
                 up=None, bottom=None)
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