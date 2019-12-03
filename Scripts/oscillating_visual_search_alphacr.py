import numpy as np
import math
import matplotlib.pyplot as plt


EPS = 0.0000001
X_0 = 0.33
gamma = 8.0
w_start = 0.1
w_end = 1000.0
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


def get_w_a_star(ws, ys):
    res = {}
    for idx in range(1,len(ws)):
        if ys[idx-1]*ys[idx] < 0:
            w_star = (ws[idx-1]+ws[idx])/2.0
            res[str(w_star)] = alpha_cr(w_star)
    return res


def draw_sign_function(ws, ys):
    plt.rcParams.update({'font.size': 13})
    plt.figure('Xo={:.8},gamma={:.8}'.format(X_0, gamma))
    plt.xlabel('$\omega$')
    plt.grid(True)
    plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.98)
    plt.axhline(y=0.0, linewidth=2, color='gray', zorder=2)
    plt.plot(ws, ys, color='k', linewidth=2)
    w_a = get_w_a_star(ws, ys)
    print('gamma\tw_star\talpha_cr')
    for w, a in w_a.items():
        print('{} {:.8} {:.8}'.format(gamma, float(w), a))
    #x1,x2,y1,y2 = plt.axis()
    #plt.axis((x1,x2,-5.0,5.0))
    plt.show()


ws = np.linspace(w_start, w_end, n_points)
ys = [sign_func(w) for w in ws]
draw_sign_function(ws, ys)