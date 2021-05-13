void main(void){
  uint i = 0;
  buffering();
  printf("Name:");
  read_input(&DAT_00602060,32);
  while( true ) {
        menu();
        long l = read_long();
        if (l == 1) {
            allocate();
        } else if (l == 2) {
            if (i < 8) {
                free(DAT_00602088);
                i += 1;
            }
        } else if (l == 3) {
            print_name();
        } else if (l == 4) {
            exit(0);
       } else{
            puts("Invalid choice");
       }
}

void print_name(void){
  printf("Name :");
  write(1,&DAT_00602060,32);
  return;
}

void allocate(void){
  printf("Size:");
  ulong size = read_long();
  if (size < 256) {
    DAT_00602088 = malloc(size);
    printf("Data:");
    int i = size-16;
    read_input(DAT_00602088,i,i);
    puts("Done !");
  }
  return;
}
