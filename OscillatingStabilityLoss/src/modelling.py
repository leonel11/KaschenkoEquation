"""
@package modelling
Main module of launching the program
"""

from argparse import ArgumentParser
from controller import Controller


def init_argparse():
    """
    Initialize argument parser
    @return argparser
    """
    pars = ArgumentParser(description='Modelling of stability loss of null solution for Kaschenko boundary-value problem')
    pars.add_argument(
        '-j',
        '--json',
        nargs='?',
        help='path to json-file with params of the task',
        default='data/params_example.json',
        type=str)
    pars.add_argument(
        '-d',
        '--delay',
        nargs='?',
        help='True, if time delay is needed',
        default=False,
        type=bool)
    return pars


"""
Main function
"""
def main():
    args = init_argparse().parse_args()
    cont = Controller(args.json, args.delay)
    cont.run()


if __name__ == '__main__':
    main()