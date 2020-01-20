'''
Script for building and visualization of v(x) function for fixed x0 and gamma
(OSCILLATING case of eigenfunction)
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import utils


x0 = 0.41
gamma = 6.0

AFTER_TANGENT = False
SUFFIX_NAME = '_after_tangent' if AFTER_TANGENT else ''
CSV_FILE = f'../Tracer/Results/x0={x0:.2f}/x0={x0:.2f}_analytical' + SUFFIX_NAME + '.csv'


def get_omega(g):
    '''
    Return omega(gamma) value
    :param g: gamma value
    :return: omega(gamma) value
    '''
    df = pd.read_csv(CSV_FILE, sep=';')
    return df.loc[(df['gamma'] < g+utils.EPS) & (df['gamma'] > g-utils.EPS)]['w'].values[0]


def get_v_func_val(g, w, x):
    '''
    Calculate and return value of v(x) for fixed gamma
    :param g: fixed gamma value
    :param g: fixed omega value
    :param x: x value
    :return: v(x) for fixed gamma
    '''
    if g <= 0:
        mu = np.sqrt(-g + w*1.0j)
        return np.cosh(mu*x)
    else:
        mu = np.sqrt(g + w*1.0j)
        return np.cos(mu*x)


def draw_v_func_components(xs, vs):
    '''
    Draw 2 graphics: Re(v(x)) dependency and Im(v(x)) dependency
    :param xs: x values
    :param vs: v(x) values
    '''
    f = plt.figure(figsize=(10, 4))
    f.canvas.set_window_title('x0={:.2}__g={:.4}'.format(x0, gamma))
    f.subplots_adjust(left=0.07, bottom=0.1, right=0.97, top=0.97, hspace=0.5)
    ax1 = f.add_subplot(121)
    ax2 = f.add_subplot(122)
    ax1.set_xlabel('x')
    ax1.set_ylabel('Re v', rotation='horizontal', position=(0.0, 0.53))
    ax1.grid()
    ys = [v.real for v in vs]
    ax1.plot(xs, ys, color='seagreen', linewidth=2, zorder=3)
    ax1.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    ax1.axvline(x=0.0, linewidth=2, color='grey', zorder=2)
    ax2.set_xlabel('x')
    ax2.set_ylabel('Im v', rotation='horizontal', position=(0.0, 0.53))
    ax2.grid()
    ys = [v.imag for v in vs]
    ax2.plot(xs, ys, color='peru', linewidth=2, zorder=3)
    ax2.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    ax2.axvline(x=0.0, linewidth=2, color='grey', zorder=2)
    plt.show()


if __name__ == '__main__':
    w = get_omega(gamma)
    xs = np.linspace(0, 1, 10000)
    vs = [get_v_func_val(gamma, w, x) for x in xs]
    draw_v_func_components(xs, vs)