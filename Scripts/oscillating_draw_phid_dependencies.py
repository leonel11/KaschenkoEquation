import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


x0 = 0.25
x_ticks = np.arange(-4, 5, 1)
DATA_PATH = 'C:/_Repositories/KaschenkoEquation/Tracer/Results/x0=0.25 (u13)'
CSV_FILE = 'x0=0.25_analytical.csv'


def phi_o(g, a, w, x0):
    i = 1.0j
    mu = np.sqrt(-g + i*w)
    phi = -(2.0*mu*np.cosh(mu*x0))/(mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
    return phi.real


def G(y, a, mu, x0):
    return (a*np.cosh(y*x0)-y*np.sinh(y))/(y*y-mu*mu)


def d_o(g, a, w, x0):
    i = 1.0j
    mu = np.sqrt(-g + i*w)
    mu_conj = np.conj(mu)
    nu = mu + 2*i*mu.imag
    kappa = mu + 2*mu.real
    B = 3*mu*(G(kappa, a, mu, x0) + G(nu, a, mu, x0) + 2*G(mu_conj, a, mu, x0))
    A = 2*(np.sinh(mu)+mu*np.cosh(mu)-a*x0*np.sinh(mu*x0))
    d = B/A
    return d.real


def calc_coefs_normal_form(gs, ws, alphs):
    phis, ds = [], []
    for idx in range(len(gammas)):
        g = gs[idx]
        w = ws[idx]
        a = alphs[idx]
        phis.append(phi_o(g, a, w, x0))
        ds.append(d_o(g, a, w, x0))
    return phis, ds


def visualize_dependencies(gs, phis, ds):
    plt.rcParams.update({'font.size': 13})
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.98, top=0.98)
    plt.xlabel('$\gamma$')
    plt.xticks(x_ticks)
    plt.grid()
    plt.plot(gs, phis, label='$\phi_0$', color='darkcyan', linewidth=2)
    plt.legend()
    plt.savefig(os.path.join(DATA_PATH, 'oscillating_phi0.png'))
    plt.clf()
    plt.xticks(x_ticks)
    plt.grid()
    plt.plot(gs, ds, label='$d_0$', color='darkorange', linewidth=2)
    plt.legend()
    plt.savefig(os.path.join(DATA_PATH, 'oscillating_d0.png'))


df = pd.read_csv(os.path.join(DATA_PATH, CSV_FILE), sep=';')
gammas = list(df['gamma'])
omegas = list(df['w'])
alphas = list(df['alpha_c'])
phis, ds = calc_coefs_normal_form(gammas, omegas, alphas)
visualize_dependencies(gammas, phis, ds)