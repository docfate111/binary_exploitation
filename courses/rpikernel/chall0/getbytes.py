file = open("shellcode-raw", "rb")
byte = file.read(1)
ans = ''
while byte:
	byte = file.read(1)
	ans += '0x'+byte.hex()+','
print(ans)