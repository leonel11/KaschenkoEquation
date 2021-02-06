'''
Script for checking suspicious points, where alpha_f (oscillating case) curve
are born from alpha_u curve and where alpha_c (other oscillating case) curve
"touches" alpha_u curve
'''

import cmath
import numpy as np
import utils


x0 = 0.33
g = 4.8956624355
l = 0j
a = -2.37874725


def F(a, g, l, x0):
    if abs(l.imag) < utils.EPS:
        mu = np.sqrt(g)
        return -mu*np.sin(mu) - a*np.cos(mu*x0)
    else:
        mu = cmath.sqrt(-g+l)
        return mu*cmath.sinh(mu) - a*cmath.cosh(mu*x0)


def F_der(a, g, l, x0):
    # F'
    if abs(l.imag) < utils.EPS:
        mu = np.sqrt(g)
        return (np.sin(mu) + mu*np.cos(mu) - a*x0*np.sin(mu*x0)) / (2.0*mu)
    else:
        mu = cmath.sqrt(-g+l)
        return (cmath.sinh(mu) + mu*cmath.cosh(mu) - a*x0*cmath.sinh(mu*x0)) / (2.0*mu)


def F_derder(a, g, l, x0):
    # F''
    if abs(l.imag) < utils.EPS:
        mu = np.sqrt(g)
        first = 0.25*(np.cos(mu)/(mu*mu) + np.sin(mu)/(mu*mu*mu))
        second = np.sin(mu)/(4.0*mu)
        third = -((a*x0)/4.0) * ((x0*np.cos(mu*x0))/(mu*mu) + (np.sin(mu*x0))/(mu*mu* mu))
    else:
        mu = cmath.sqrt(-g + l)
        first = 0.25*(cmath.cosh(mu)/(mu*mu) - cmath.sinh(mu)/(mu*mu*mu))
        second = cmath.sinh(mu)/(4.0*mu)
        third = -((a*x0)/4.0)*((x0*cmath.cosh(mu*x0))/(mu*mu) - (cmath.sinh(mu*x0))/(mu*mu*mu))
    return first+second+third


if __name__ == '__main__':
    f = F(a, g, l, x0)
    fd = F_der(a, g, l, x0)
    fdd = F_derder(a, g, l, x0)
    print('F={}'.format(f))
    print('F\'={}'.format(fd))
    print('F\'\'={:.4}'.format(fdd))