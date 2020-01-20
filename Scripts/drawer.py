import matplotlib.pyplot as plt
import os


class Drawer:
    '''
    Class, which implements the drawer for dependencies
    '''

    __save_dir = '..' # directory of saving graphics
    __adjusts = {
        'left': 0.11,
        'bottom': 0.11,
        'right': 0.94,
        'top': 0.94,
    }

    def __init__(self, x_label=None , y_label=None, figure_name='Figure1',
                 save_dir=__save_dir, adjusts=__adjusts):
        plt.rcParams.update({'font.size': 13})
        if os.path.exists(save_dir):
            plt.rcParams['savefig.directory'] = save_dir
        else:
            plt.rcParams['savefig.directory'] = self.__save_dir
        plt.figure(figure_name)
        plt.subplots_adjust(left=adjusts['left'], bottom=adjusts['bottom'],
                            right=adjusts['right'], top=adjusts['top'])
        if x_label:
            plt.xlabel(x_label)
        if y_label:
            plt.ylabel(y_label, rotation='horizontal', position=(0.0, 0.54))
        plt.grid(True)

    def drawAxis(self, show_Ox=False, show_Oy=False):
        '''
        Draw graphic of alpha_u(gamma) (divergent case) and  alpha_1(gamma) (x0=1)
        dependencies
        :param gammas: list of gamma values
        :param au: list of alpha_u values
        :param a1: list of alpha_1 values
        '''
        if show_Ox:
            plt.axhline(y=0.0, linewidth=2, color='grey')
        if show_Oy:
            plt.axvline(x=0.0, linewidth=2, color='grey')

    def drawCurve(self, x_data=[], y_data=[], curve_lbl=None, curve_color='k',
                  z_order=2, save_name=None):
        '''
        Draw curve (one dependency)
        :param x_data: values on abscissa axis
        :param y_data: values on ordinate axis
        :param curve_lbl: name (label) of curve (dependency)
        :param curve_color: color of curve (dependency)
        :param z_order: order of disposition on graphic
        :param save_name: name of picture for saving the graphic
        :return:
        '''
        plt.plot(x_data, y_data, label=curve_lbl, color=curve_color,
                 linewidth=2, zorder=z_order)
        x1, x2, y1, y2 = plt.axis()
        plt.axis((x1, x2, y1, y2))
        if save_name:
            plt.savefig(save_name)
        else:
            plt.show()

    def drawTwoCurves(self, x_data=[], y1=[], y2=[], curve1_lbl=None,
                      curve2_lbl=None, curve1_color='k', curve2_color='k',
                      save_name=None):
        '''
        Draw 2 curves (dependencies) on one graphic
        :param x_data: values on abscissa axis
        :param y1: values on ordinate axis for the 1st curve (dependency)
        :param y2: values on ordinate axis for the 2nd curve (dependency)
        :param curve1_lbl: name (label) of the 1st curve (dependency)
        :param curve2_lbl: name (label) of the 2nd curve (dependency)
        :param curve1_color: color of the 1st curve (dependency)
        :param curve2_color: color of the 2nd curve (dependency)
        :param save_name: name of picture for saving the graphic
        :return:
        '''
        plt.plot(x_data, y1, label=curve1_lbl, color=curve1_color, linewidth=2,
                 zorder=2)
        plt.plot(x_data, y2, label=curve2_lbl, color=curve2_color, linewidth=2,
                 zorder=3)
        x1, x2, y1, y2 = plt.axis()
        plt.axis((x1, x2, y1, y2))
        plt.legend()
        if save_name:
            plt.savefig(save_name)
        else:
            plt.show()