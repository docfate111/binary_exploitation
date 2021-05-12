void allocate(void){ // choice 1
  ulong uVar1;
  ulong __size;
  void *pvVar2;
  long lVar3;
  printf("Index:");
  uVar1 = read_long();
  if ((uVar1 < 2) && (heap[uVar1] == 0)) {
    printf("Size:");
    __size = read_long();
    if (__size < 0x79) {
      pvVar2 = realloc((void *)0x0,__size);
      if (pvVar2 == (void *)0x0) {
        puts("alloc error");
      } else {
        heap[uVar1] = pvVar2;
        printf("Data:");
        lVar3 = read_input(heap[uVar1], __size & 0xffffffff,uVar1 * 8,
                           __size & 0xffffffff);
        heap[uVar1] = 0;
      }
    } else {
      puts("Too large!");
    }
  } else {
    puts("Invalid !");
  }
  return;
}

void reallocate(void){ // choice 2
  ulong uVar1;
  ulong __size;
  void *pvVar2;
  printf("Index:");
  uVar1 = read_long();
  if ((uVar1 < 2) && (heap[uVar1] != 0)) {
    printf("Size:");
    __size = read_long();
    if (__size < 0x79) {
      pvVar2 = realloc(heap[uVar1],__size);
      if (pvVar2 == (void *)0x0) {
        puts("alloc error");
      } else {
        heap[uVar1] = pvVar2;
        printf("Data:");
        read_input(heap[uVar1],__size & 0xffffffff,uVar1 * 8,
                   __size & 0xffffffff);
      }
    } else {
      puts("Too large!");
    }
  } else {
    puts("Invalid !");
  }
  return;
}

void rfree(void){ // choice 3
  ulong uVar1;
  printf("Index:");
  uVar1 = read_long();
  if (uVar1 < 2) {
    realloc(heap[uVar1],0);
    heap[uVar1] = 0;
  }
  else {
    puts("Invalid !");
  }
  return;
}