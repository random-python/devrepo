#!/usr/bin/env python

import sys
import inspect

def print_stack():
    this_stack = inspect.stack()
    for info in this_stack:
        print(info)
    
def level_1():
    level_2()
    
def level_2():
    level_3()
    
def level_3():
    print_stack()

def main():
    print(f"sys.argv[0]={sys.argv[0]}")
    level_1()

main()    
