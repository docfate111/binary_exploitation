# challenge

old HacktheBox challenge childish calloc

glibc 2.27

strategy 

1. trick the ptmalloc allocator to combine freed chunks into unsorted bin by using off-by-one heap overflow to get a main arena pointer

2. use the leak to find the system and free hook address

3. realign the heap chunks so one of the chunks overlaps with free_hook

4. use the binary's write primitive to edit the free_hook to system("/bin/sh")

5. free a chunk to get a shell

There are constraints on allocations - see the exploit.py for more info



