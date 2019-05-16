import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


x0 = 0.33
DATA_PATH = 'C:/_Repositories/KaschenkoEquation/Tracer/Results/x0=0.33'
CSV_FILE = 'x0=0.33_analytical.csv'

gammas_ticks = np.arange(-4, 6, 1)


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
    phis, ds, amps = [], [], []
    for idx in range(len(gammas)):
        g, w, a = gs[idx], ws[idx], alphs[idx]
        phis.append(phi_o(g, a, w, x0))
        ds.append(d_o(g, a, w, x0))
        amps.append(np.sqrt(abs(phis[-1]/ds[-1])))
    return phis, ds, amps


def visualize_dependencies(gs, phis, ds, amps):
    plt.rcParams.update({'font.size': 13})
    plt.subplots_adjust(left=0.12, bottom=0.11, right=0.98, top=0.94)
    plt.xticks(gammas_ticks)
    plt.xlabel('$\gamma$')
    plt.ylabel(r'$\varphi_0$', rotation='horizontal', position=(0.0,0.55))
    plt.grid()
    plt.plot(gs, phis, color='darkcyan', linewidth=2)
    plt.savefig(os.path.join(DATA_PATH, 'oscillating_phi0_x0={:.5}.png'.format(x0)))
    plt.clf()
    plt.xticks(gammas_ticks)
    plt.xlabel('$\gamma$')
    plt.ylabel('$d_0$', rotation='horizontal', position=(0.0,0.55))
    plt.grid()
    plt.plot(gs, ds, color='darkorange', linewidth=2)
    #x1,x2,y1,y2 = plt.axis()
    #plt.axis((3.0,4.94,-42.0,0.5))
    plt.savefig(os.path.join(DATA_PATH, 'oscillating_d0_x0={:.5}.png'.format(x0)))
    plt.clf()
    plt.xticks(gammas_ticks)
    plt.xlabel('$\gamma$')
    plt.ylabel('$A_c$', rotation='horizontal', position=(0.0,0.55))
    plt.grid()
    plt.plot(gs, amps, color='crimson', linewidth=2)
    plt.savefig(os.path.join(DATA_PATH, 'oscillating_amplutude_x0={:.5}.png'.format(x0)))


df = pd.read_csv(os.path.join(DATA_PATH, CSV_FILE), sep=';')
gammas, omegas, alphas = list(df['gamma']), list(df['w']), list(df['alpha_c'])
phis, ds, amps = calc_coefs_normal_form(gammas, omegas, alphas)
visualize_dependencies(gammas, phis, ds, amps)