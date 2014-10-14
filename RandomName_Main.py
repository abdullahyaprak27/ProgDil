#!/usr/bin/python
from RandomName import *
import sys

def main(args):
    if len(args)==1:
        return RandomName()
    elif len(args)==2:
        if args[1]=="en":
            return RandomName(language=args[1])
        elif args[1].isdigit():
            return RandomName(again=args[1])

    elif len(args)==3:
        return RandomName(language=args[1],again=args[2])
    
args = sys.argv[:]
main(args)
