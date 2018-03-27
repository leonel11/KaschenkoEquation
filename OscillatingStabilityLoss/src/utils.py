"""
@package utils
Module of auxiliary useful functions
"""

from os import path, makedirs
from datetime import datetime


def time_to_str(t):
    """
    Convert float time to string
    @param t float time
    return time string in format min:sec.ms
    """
    # FIXME: output seconds with leading zero in some cases
    return '{}:{:.3f}'.format(int(t//60), t%60)


def create_dir(folder):
    """
    Makes path if it doesn't exist
    """
    if not path.exists(folder):
        makedirs(folder)


def results_filename(delay, shift):
    if delay:
        res = 'T='
    else:
        res = 'Xo='
    res += '{:.4f}__'.format(shift)
    str_moment = datetime.now().strftime('%d.%m.%Y_%H-%M')
    res += str_moment
    return res