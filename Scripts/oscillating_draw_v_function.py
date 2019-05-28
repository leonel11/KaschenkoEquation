import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


EPS = 0.000001
gamma = 3.1
x0 = 0.33
CSV_FILE = '../Tracer/Results/x0=0.33/x0=0.33_analytical.csv'


def get_omega(g):
    df = pd.read_csv(CSV_FILE, sep=';')
    return df.loc[(df['gamma'] < g+EPS) & (df['gamma'] > g-EPS)]['w'].values[0]


def v_func(g, w, x):
    if g <= 0:
        mu = np.sqrt(-g + w*1.0j)
        return np.cosh(mu*x)
    else:
        mu = np.sqrt(g + w*1.0j)
        return np.cos(mu*x)


def visualise_func(xs, vs):
    plt.rcParams.update({'font.size': 10})
    f = plt.figure(figsize=(10, 4))
    f.canvas.set_window_title('x0={:.2}__g={:.4}'.format(x0, gamma)) # change window title
    f.subplots_adjust(left=0.07, bottom=0.1, right=0.97, top=0.97, hspace=0.5)
    ax1 = f.add_subplot(121)
    ax2 = f.add_subplot(122)
    ax1.set_xlabel('x')
    ax1.set_ylabel('Re v', rotation='horizontal', position=(0.0, 0.55))
    ax1.grid()
    ys = [v.real for v in vs]
    ax1.plot(xs, ys, color='seagreen', linewidth=2, zorder=3)
    ax1.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    ax1.axvline(x=0.0, linewidth=2, color='grey', zorder=2)
    ax2.set_xlabel('x')
    ax2.set_ylabel('Im v', rotation='horizontal', position=(0.0, 0.55))
    ax2.grid()
    ys = [v.imag for v in vs]
    ax2.plot(xs, ys, color='peru', linewidth=2, zorder=3)
    ax2.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    ax2.axvline(x=0.0, linewidth=2, color='grey', zorder=2)
    plt.show()


w = get_omega(gamma)
xs = np.linspace(0, 1, 10000)
vs = [v_func(gamma, w, x) for x in xs]
visualise_func(xs, vs)