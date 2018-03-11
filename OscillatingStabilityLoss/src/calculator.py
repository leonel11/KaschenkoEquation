import numpy as np
import cmath

class Calculator:
    """
    @class Calculator
    Класс для расчета
    """

    def __init__(self, gamma, arg_alpha, arg_omega, arg_delay, shift, eps):
        """
        Конструктор класса
        @param gamma: фиксированное занчение параметра gamma, для которого будет идти счет
        @param arg_alpha: набор параметров alpha, необходимы для формирования сетки
        @param arg_omega: набор параметров omega, необходимый для формирования сетки
        @param arg_delay: булева переменная, определяющая тип сдвига в линейном краевом условии задачи
                          (True - сдвиг по времени, False - сдвиг по координате)
        @param shift: сдвиг по координате или по времени
        """
        self.__gamma = gamma
        self.__alpha = arg_alpha
        self.__omega = arg_omega
        self.__delay = arg_delay
        self.__shift = shift
        self.__eps = eps
        self.__crits = None

    def __make_grid(self):
        """
        Формирование сетки по параметрам alpha и omega, по которым будет протекать численный счет
        @return: сгенерированная сетка параметров alpha и omega
        """
        alphas = np.linspace(self.__alpha['first'], self.__alpha['last'], self.__alpha['steps'])
        omegas = np.linspace(self.__omega['first'], self.__omega['last'], self.__omega['steps'])
        return np.meshgrid(alphas, omegas)

    def __linear_condition(self, cur_omega, cur_alpha):
        mu = cmath.sqrt(complex(-self.__gamma, cur_omega))
        if self.__delay:
            eq = abs(mu*cmath.sinh(mu) - cur_alpha*cmath.cosh(mu) * \
                     cmath.exp(complex(0, cur_omega*self.__shift)))
        else:
            eq = abs(mu*cmath.sinh(mu) - cur_alpha*cmath.cosh(mu*self.__shift))
        return eq

    def ___search_criticals(self, mesh_omegas, mesh_alphas):
        crits = dict()
        for i in range(mesh_omegas.shape[0]):
            for j in range(mesh_omegas.shape[1]):
                cond_val = self.__linear_condition(mesh_omegas[i, j], mesh_alphas[i, j])
                print(cond_val)
                if cond_val < 1.0:
                    dict_key = '{:.6f}'.format(mesh_omegas[i, j])
                    if dict_key in crits:
                        crits[dict_key].append(mesh_alphas[i, j])
                    else:
                        crits[dict_key] = [mesh_alphas[i, j]]
        return crits

    def get_critical_values(self):
        return self.__crits

    def run(self):
        mesh_alphas, mesh_omegas = self.__make_grid()
        self.__crits = self.___search_criticals(mesh_omegas, mesh_alphas)