// Compilation:
// gcc ./challenge.c -o challenge -fno-stack-protector -m32 -ggdb -no-pie

#include <stdio.h>
#include <stdlib.h>

void secretFunction()
{
   setuid(0);
   system("/bin/bash");
   printf("All Done\n");
}

void echo()
{
    char buffer[20];
    printf("Enter some text:\n");
    scanf("%s", buffer);
    printf("You entered: %s\n", buffer);
}

int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    echo();
    return 0;
}

