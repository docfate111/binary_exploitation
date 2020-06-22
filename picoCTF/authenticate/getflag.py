#!/usr/bin/python3
from pwn import *
import sys
if __name__=='__main__':
    
# printf is used without a specifier
# so we can use this to changes
LOCAL = True
HOST  = '2018shell.picoctf.com'
PORT = 27114
def find_fmt():
