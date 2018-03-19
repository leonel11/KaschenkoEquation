"""
@package calculator
Non object-oriented module for parallel calculation of potential critical values
"""

import numpy as np
import cmath
from numba import jit


def get_grid(arg_omega, arg_alpha):
    omegas = np.linspace(arg_omega['first'], arg_omega['last'], arg_omega['steps'])
    alphas = np.linspace(arg_alpha['first'], arg_alpha['last'], arg_alpha['steps'])
    return np.meshgrid(omegas, alphas)


@jit(nopython=True, nogil=True, target='cpu')
def abs_boundary_function(gamma, cur_omega, cur_alpha, delay, shift):
    mu = cmath.sqrt(complex(-gamma, cur_omega))
    # definition of function depending on the type of shift
    if delay:
        eq = abs(mu * cmath.sinh(mu) - cur_alpha * cmath.cosh(mu) * \
                 cmath.exp(complex(0, cur_omega * shift)))
    else:
        eq = abs(mu * cmath.sinh(mu) - cur_alpha * cmath.cosh(mu * shift))
    return eq


@jit(nogil=True, target='cpu')
def search_potential_criticals(crits, gamma, mesh_omegas, mesh_alphas, delay, shift, eps):
    for i in range(mesh_omegas.shape[0]):
        for j in range(mesh_alphas.shape[1]):
            cond_val = abs_boundary_function(gamma, mesh_omegas[i, j], mesh_alphas[i, j], delay, shift)
            # condition of existence of potential critical values
            if cond_val < eps:
                dict_key = '{:.4f}'.format(mesh_omegas[i, j])
                if dict_key in crits:
                    crits[dict_key].append(mesh_alphas[i, j])
                else:
                    crits[dict_key] = [mesh_alphas[i, j]]


def potential_criticals(gamma, arg_omega, arg_alpha, delay, shift, eps):
    mesh_alphas, mesh_omegas = get_grid(arg_omega, arg_alpha)
    crits = dict()
    search_potential_criticals(crits, gamma, mesh_omegas, mesh_alphas, delay, shift, eps)
    return crits