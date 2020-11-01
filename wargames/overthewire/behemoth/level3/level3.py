#!/usr/bin/python3
from pwn import *
import os
session = ssh(host='behemoth.labs.overthewire.org', user='behemoth3', password='nieteidiel', port=2221)
# get file to decompile via Ghidra
# session.get('/behemoth/behemoth3')
io = session.run('sh')
if(io):
else:
    print("Error starting shell")
session.close()
