#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
 python test module No.1
'''

__author__ = 'yuzd'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("---1---")
    elif len(args) == 2:
        print("---2---")
    else:
        print("---more than 2---")

if __name__ == '__main__':
    test()