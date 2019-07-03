import numpy as np
import math
import matplotlib.pyplot as plt


EPS = 0.000001
X_0 = 0.39
gamma = 5.37
w_pred = 19.30316
w_start = 0.95*w_pred
w_end = 1.05*w_pred
n_points = 10000


def sign_func(w):
    r = np.sqrt(np.sqrt(gamma*gamma+w*w))
    if gamma <= 0.0:
        t = np.arctan(-w/gamma)/2.0
    else:
        t = (math.pi - np.arctan(w/gamma)) / 2.0
    hi = r*np.cos(t)
    teta = r*np.sin(t)
    return (teta*np.sinh(hi)*np.cos(teta)+hi*np.cosh(hi)*np.sin(teta))/\
           (hi*np.sinh(hi)*np.cos(teta)-teta*np.cosh(hi)*np.sin(teta)) - np.tanh(hi*X_0)*np.tan(teta*X_0)


def alpha_cr(w):
    r = np.sqrt(np.sqrt(gamma * gamma + w * w))
    if gamma <= 0.0:
        t = np.arctan(-w / gamma) / 2.0
    else:
        t = (math.pi - np.arctan(w / gamma)) / 2.0
    hi = r*np.cos(t)
    teta = r*np.sin(t)
    return (hi*np.sinh(hi)*np.cos(teta)-teta*np.cosh(hi)*np.sin(teta))/(np.cosh(hi*X_0)*np.cos(teta*X_0))


def draw_sign_function(ws, ys):
    plt.rcParams.update({'font.size': 13})
    plt.figure('Xo={:.5},gamma={:.5}'.format(X_0, gamma))
    w_star = ws[ys.index(min(list(map(abs, ys))))]
    a = alpha_cr(w_star)
    plt.title(r'$\omega$ = {:.6}, $\alpha_c$ = {:.6}'.format(w_star, a))
    plt.xlabel('$\omega$')
    plt.grid(True)
    plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.94)
    plt.axhline(y=0.0, linewidth=2, color='gray', zorder=2)
    plt.plot(ws, ys, color='k', linewidth=2)
    plt.scatter(w_star, 0.0, color='black', s=16, zorder=4)
    plt.show()


ws = np.linspace(w_start, w_end, n_points)
ys = [sign_func(w) for w in ws]
draw_sign_function(ws, ys)