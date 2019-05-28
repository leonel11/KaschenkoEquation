import numpy as np
import matplotlib.pyplot as plt


x0 = 0.0
gamma = 5.1


def v_func(g, x):
    if g <= 0:
        mu = np.sqrt(-g)
        return np.cosh(mu*x)
    else:
        mu = np.sqrt(g)
        return np.cos(mu*x)


def visualise_func(xs, vs):
    plt.rcParams.update({'font.size': 13})
    plt.figure().canvas.set_window_title('x0={:.2}__g={:.4}'.format(x0, gamma)) # change window title
    plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.98)
    plt.xlabel('x')
    plt.ylabel('v', rotation='horizontal', position=(0.0, 0.55))
    plt.grid()
    plt.plot(xs, vs, color='slateblue', linewidth=2, zorder=3)
    plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)
    plt.axvline(x=0.0, linewidth=2, color='grey', zorder=2)
    plt.show()


xs = np.linspace(0, 1, 10000)
vs = [v_func(gamma, x) for x in xs]
visualise_func(xs, vs)