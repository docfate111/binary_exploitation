from pwn import *
s = ssh(user='level1', host='io.netgarage.org', password='level1', port=22)
# game at http://io.netgarage.org/
sh = s.run('bash')
sh.sendline(b'/levels/level01')
# disassembling the level01 binary we see a
# cmp to 0x10f to register eax
# so the input is 271
print(sh.recvline(timeout=1))
sh.sendline(b'271')
print(sh.recvline(timeout=1))
sh.sendline(b'cat /home/level2/.pass')
log.info('Password : '+sh.recvline(timeout=1).decode('utf-8')[8:-1])
s.close()
