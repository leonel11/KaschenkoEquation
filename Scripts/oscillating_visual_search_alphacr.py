import numpy as np
import math
import matplotlib.pyplot as plt


EPS = 0.000001
X_0 = 0.45
gamma = 10.606
w_start = 12.5
w_end = 13.5
n_points = 100000


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


def get_w_star(ws, ys):
    for idx in range(1,len(ws)):
        if ys[idx-1]*ys[idx] < 0:
            return (ws[idx-1]+ws[idx])/2.0
    return None


def draw_sign_function(ws, ys):
    plt.rcParams.update({'font.size': 13})
    plt.figure('Xo={:.5},gamma={:.5}'.format(X_0, gamma))
    plt.xlabel('$\omega$')
    plt.grid(True)
    plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.94)
    plt.axhline(y=0.0, linewidth=2, color='gray', zorder=2)
    plt.plot(ws, ys, color='k', linewidth=2)
    w_star = get_w_star(ws, ys) #ws[ys.index(min(list(map(abs, ys))))]
    if w_star != None:
        a = alpha_cr(w_star)
        plt.title(r'$\omega$ = {:.6}, $\alpha_c$ = {:.6}'.format(w_star, a))
        plt.scatter(w_star, 0.0, color='black', s=16, zorder=4)
        print('{:.6};{:.6};{:.6}'.format(gamma, w_star, a))
    #x1,x2,y1,y2 = plt.axis()
    #plt.axis((x1,x2,-50.0,50.0))
    plt.show()


ws = np.linspace(w_start, w_end, n_points)
ys = [sign_func(w) for w in ws]
draw_sign_function(ws, ys)