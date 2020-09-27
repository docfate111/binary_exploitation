Looking through the assembler we notice
```
ldr r2, [r11, -#8]
ldr r3, [pc, #48]
cmp r2, r3
```
We know that after strcpy copies the argument into some variable on the stack 
the value at the memory address in r11 subtracted by 8 is stored into r2
and the value stored at the address pointed to by the program counter-48 is a constant
that is then stored in r3. Stepping through the program in gdb and
we can see that the string at that address is 0x61626364.
Guessing the size of the char buffer on the stack, we can see that the stack 
is being overwritten by strcpy taking in a string that is too long. This
then overwrites r11-#8. By guessing and checking the offset with gdb, we find that after 64 bytes the rest is stored into r2.
So changing that part of the payload to 'dcba' overwrites the variable correctly, getting us the "flag".
