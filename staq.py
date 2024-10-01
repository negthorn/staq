"""STAQ
    Usage:
        staq.py [-v] FILE...
        staq.py [-v] -r DIR
        staq.py -h | --help
    Options:
        -r, --recursive      Recursive - in case FILE is a folder
        -v, --verbose        More output messages
        -h, --help           Shows this message

"""
# -f <name>, --file=<name>    Use this file as entry point


import sys
from os import times

from docopt import docopt


if __name__ == "__main__":
    #start the application here
    arguments = docopt(__doc__)
    print("F-off")
    print('FILE: ', arguments['FILE'])
    print('DIR: ',arguments['DIR'])
    if arguments['--recursive']:
        print("I will use DIR")
    else:
        print("I will use FILE")
    #print(arguments)

    print(sys.argv)
    pass
