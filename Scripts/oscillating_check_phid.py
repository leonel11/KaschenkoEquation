import numpy as np


alpha = -17.7986
omega = 11.1866
#alpha = -34514.5759
#omega = 149.2778


def phi_o(a, w):
    i = 1.0j
    mu = np.sqrt(i*w)
    A = (1.0/2.0)*(a/(i*w) + np.cosh(mu))
    phi = 1.0/A
    return phi.real


def G(y):
    return y*np.sinh(y)


def d_o(a, w):
    i = 1.0j
    mu = np.sqrt(i*w)
    mu_conj = np.sqrt(-i*w)
    kappa = 2.0*mu + mu_conj
    nu = 2.0*mu - mu_conj
    B = (3.0/(25.0*w))*(11.0*a*i - 12.5*i*G(mu_conj) - (1.0-0.75*i)*G(kappa) + (1.0+0.75*i)*G(nu))
    A = (1.0/2.0)*(a/(i*w) + np.cosh(mu))
    d = B/A
    return d.real


phi0 = phi_o(alpha, omega)
d0 = d_o(alpha, omega)
print('phi_o = {:.5} \nd_o   = {:.5}'.format(phi0, d0))