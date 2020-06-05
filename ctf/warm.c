#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
int fd;
void init(){
  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stderr,(char *)0x0,2,0);
  fd = open("flag.txt",0);
  if (fd < 0) {
    puts("flag.txt not found");
    exit(1);
  }
  return;
}
void win(){
	char local_38[40];
	read(fd,local_38,0x1e);
  	write(1,local_38,0x1e);
}
void vuln(){
  //long offset;
  char l218 [256];
  char l118 [264];
  //int local_10 = *(int *)(offset+0x28);
  read(0,l218,0x100);
  snprintf(l118,0x100,l218);
  printf("1st: ");
  puts(l118);
  printf("2nd: ");
  puts(l218);
  exit(0);
}
int main(){
	init();
	vuln();
	return 0;
}
