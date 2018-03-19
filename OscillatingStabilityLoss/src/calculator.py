"""
@package calculator
Module for calculation of potential critical values
"""

import numpy as np
import cmath
#from numba import jit

class Calculator:
    """
    @class Calculator
    Main class of this module
    """

    def __init__(self, gamma, arg_omega, arg_alpha, arg_delay, shift, eps):
        """
        Constructor
        @param gamma: fixed parameter gamma. For this value the calculation will be implemented
        @param arg_omega: set of linspace parameters to form a grid of omegas
        @param arg_alpha: set of linspace parameters to form a grid of alphas
        @param arg_delay: bool var, which determines the type of shift in linear boundary condition
                          (True - time delay, False - coordinate delay)
        @param shift: value of delay (in coordinate or time measures)
        """
        self.__omega = arg_omega
        self.__alpha = arg_alpha
        self.__gamma = gamma
        self.__delay = arg_delay
        self.__shift = shift
        self.__eps = eps
        self.__crits = dict()

    def __make_grid(self):
        """
        Form the grid of alphas and omegas to implement the calculation
        @return: grid of alphas and omegas
        """
        omegas = np.linspace(self.__omega['first'], self.__omega['last'], self.__omega['steps'])
        alphas = np.linspace(self.__alpha['first'], self.__alpha['last'], self.__alpha['steps'])
        return np.meshgrid(omegas, alphas)

    def __abs_boundary_function(self, cur_omega, cur_alpha):
        """
        Calculate abs of function in linear boundary condition
        @param cur_omega: fixed value of parameter omega
        @param cur_alpha: fixed value of parameter alpha
        @return abs of function in linear boundary condition
        """
        mu = cmath.sqrt(complex(-self.__gamma, cur_omega))
        # definition of function depending on the type of shift
        if self.__delay:
            eq = abs(mu*cmath.sinh(mu) - cur_alpha*cmath.cosh(mu) * \
                     cmath.exp(complex(0, cur_omega*self.__shift)))
        else:
            eq = abs(mu*cmath.sinh(mu) - cur_alpha*cmath.cosh(mu*self.__shift))
        return eq

    #@jit(nopython=True, nogil=True, target='cpu')
    def ___search_criticals(self, mesh_omegas, mesh_alphas):
        """
        Search potential critical values omegas and alphas
        @param mesh_omegas: set of omegas as meshgrid
        @param mesh_alphas: set of alphas as meshgrid
        @return the dictionary, which reproduce the dependency of critical omegas and critical alphas
        """
        # FIXME: parallelize the calculation on CPU or GPU
        for i in range(mesh_omegas.shape[0]):
            for j in range(mesh_alphas.shape[1]):
                cond_val = self.__abs_boundary_function(mesh_omegas[i, j], mesh_alphas[i, j])
                # condition of existence of potential critical values
                if cond_val < self.__eps:
                    dict_key = '{:.4f}'.format(mesh_omegas[i, j])
                    if dict_key in self.__crits:
                        self.__crits[dict_key].append(mesh_alphas[i, j])
                    else:
                        self.__crits[dict_key] = [mesh_alphas[i, j]]

    def get_critical_values(self):
        """
        Get a dictionary of critical values of omegas and alphas
        @return the dictionary of critical values
        """
        mesh_alphas, mesh_omegas = self.__make_grid()
        self.___search_criticals(mesh_omegas, mesh_alphas)
        return self.__crits