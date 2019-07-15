import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


beta = 1.0
x0 = 0.45
DATA_PATH = 'C:/_Repositories/KaschenkoEquation/Tracer/Variations/Cubic Boundary Condition/x0=0.45'
CSV_FILE = 'x0=0.45_analytical_after_tangent.csv'
AFTER_TANGENT = True


plt.rcParams.update({'font.size': 13})
plt.rcParams['savefig.directory'] = '../Tracer/Variations/Cubic Boundary Condition'


def read_csv_params():
    df = pd.read_csv(os.path.join(DATA_PATH, CSV_FILE), sep=';')
    gammas, omegas, alphas = list(df['gamma']), list(df['w']), list(df['alpha_c'])
    return gammas[:-1], omegas[:-1], alphas[:-1]


def phi0_d0_A(g, w, a, x0):
    i = 1.0j
    mu = np.sqrt(-g+i*w)
    mu_conj = np.conj(mu)
    nu = mu + 2*i*mu.imag
    kappa = mu + 2*mu.real
    phi = -2.0*mu*np.cosh(mu*x0) / (mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
    d = 1.5*beta*mu*(np.cosh(kappa*x0) + np.cosh(nu*x0) + 2.0*np.cosh(mu_conj*x0)) / \
        (mu*np.cosh(mu) + np.sinh(mu) - a*x0*np.sinh(mu*x0))
    if AFTER_TANGENT:
        phi = -phi
    A = np.sqrt(abs(phi.real/d.real))
    return phi.real, d.real, A


def calc_Lyapunov_exps(gs, ws, alphas):
    phis, ds, amps = [], [], []
    for idx in range(len(gammas)):
        phi0, d0, A = phi0_d0_A(gs[idx], ws[idx], alphas[idx], x0)
        phis.append(phi0)
        ds.append(d0)
        amps.append(A)
    return phis, ds, amps


def prepare_plot():
    #plt.xticks(gammas_ticks)
    plt.xlabel('$\gamma$')
    plt.grid(True)
    plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.95)
    plt.axhline(y=0.0, linewidth=2, color='grey', zorder=2)


def draw_phid_dependencies(gammas, phis, ds):
    suffix_name = '_after_tangent' if AFTER_TANGENT else ''
    plt.figure('oscillating_phi0d0{}_x0={:.5},beta={:.5}'.format(suffix_name, x0, beta))
    prepare_plot()
    plt.plot(gammas, phis, label=r'$\varphi_0$', color='darkcyan', linewidth=2)
    plt.plot(gammas, ds, label='$d_0$', color='darkorange', linewidth=2, zorder=3)
    #x1,x2,y1,y2 = plt.axis()
    #plt.axis((x1,x2,y1,0.4))
    plt.legend()
    plt.show()


def draw_amplitude_dependency(gammas, amps):
    suffix_name = '_after_tangent' if AFTER_TANGENT else ''
    plt.figure('oscillating_A{}_x0={:.5},beta={:.5}'.format(suffix_name, x0, beta))
    prepare_plot()
    plt.plot(gammas, amps, label='$A_u$', color='crimson', linewidth=2)
    plt.legend()
    plt.show()


gammas, omegas, alphas = read_csv_params()
phis, ds, amps = calc_Lyapunov_exps(gammas, omegas, alphas)
draw_phid_dependencies(gammas, phis, ds)
draw_amplitude_dependency(gammas, amps)