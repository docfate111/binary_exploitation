# README

the gist is to use a tcache dup and to get a write primitive(since a user can control a pointer of one the chunks
and can point it to __free_hook or __malloc_hook to allocate a chunk there then replace it with system)
no working exploit yet
