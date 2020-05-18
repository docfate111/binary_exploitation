#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int vuln() {
    char buf[32];
    printf("Enter your favorite color: ");
    gets(buf);
    int good = 0;
    for (int i = 0; buf[i]; i++) {
        good &= buf[i] ^ buf[i];
    }
    return good;
}
int main(int argc, char** argv){
    //setresuid(getegid(), getegid(), getegid());
    //setresgid(getegid(), getegid(), getegid());
    //disable buffering.
    setbuf(stdout, NULL);
    if (vuln()) {
        puts("Me too! That's my favorite color too!");
        puts("You get a shell! Flag is in flag.txt");
        system("/bin/sh");
    } else {
        puts("Boo... I hate that color! :(");
    }
    return 0;
}
