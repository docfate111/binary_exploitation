# What are fastbins?

Fastbins are a memory optimization that instead consolidating freed chunks they are stored in a stack
to be used again if another small allocation of the same size happens. When a request is made that is
 bigger than the size of any fastbin, all the fast bins will be either moved into an unsorted bin or 
 merged with adjacent free chunks.

Source: https://azeria-labs.com/heap-exploitation-part-2-glibc-heap-free-bins/

Let's say three chunks are allocated as a, b, and c.

```
char* a = malloc(8);
char* b = malloc(8);
char* c = malloc(8);
```

Then we free a chunk twice, placing the 2 freed chunks into the fastbins.
```
free(a);
free(a);
```

This results in an error message about a double-free
```
double free or corruption (fasttop)
```

There is a check to prevent a chunk from being in the fastbins twice that prevents programmers from 
freeing a chunk twice. However, it is easy to get around.
```
free(a);
free(b);
free(a);
```

Since a was no longer at the top of the fastbin stack the memory allocator was fine with it being freed 
twice. But what if we want to allocate another chunk of the same size as a, wouldn't we then have a 
pointer to a chunk that is freed and unfreed at the same time? Yes!
```
char* n = malloc(8);
n -> a
fastbins stack: b -> a ->
n also points here   ^
```

In pwndbg: 
vis -> see heap
tcachebins or fastbins
heap -> see heap as separated into allocation types
find_fake_fast -> find good candidates for fake chunks near an address
# Fastbin dup into stack

Allocating the same size chunk pops the chunk of the fastbin stack and which if we have control over can 
write an address into which will add a pointer to the simulateneously in-use and free chunk.
This means the stack is the next element in the fastbin stack under the current element.
Then allocating a same size chunk again when the stack chunk is in the fastbins allows use
to have a chunk of memory that is the stack, allowing us to write anything to the stack.