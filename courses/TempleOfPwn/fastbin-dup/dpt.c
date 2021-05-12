/** @file dpt.c
 *
 * @author marco corvi <marco_corvi@geocities.com>
 * @date   feb 2003
 *
 * \brief Read disk partition table
 *
 */
#include <stdio.h>   // printf
#include <stdlib.h>  // exit

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>

int
main(int argc, char ** argv )
{
  int fd;
  unsigned char mbs[512]; // master boot sector
  unsigned char * pp;     // partition pointer
  int head, sect, cyl;
  unsigned int sector;
  int n;

  if (argc <= 1) {
    fprintf(stderr, "Usage: %s <device>\n", argv[0] );
    exit(1);
  }

  fd = open( argv[1], O_RDONLY );
  if ( fd < 0 ) {
    fprintf(stderr, "Error: unable to open device %s\n", argv[1] );
    perror("");
    exit(1);
  }

  n = read( fd, mbs, 512);
  close(fd);

  if ( n < 512 ) {
    fprintf(stderr, "Error: short read %d\n", n );
    exit(1);
  }

  pp = mbs + 0x1BE;

  for (n=0; n<4; n++) {
    printf("PARTITION %d\n", n );
    printf("Boot flag   %2x\n", pp[0] );
    printf("System flag %2x\n", pp[4] );
    // C/H/S as 10+8+6
#if 0
    head = pp[1];
    sect = pp[2]; sect = (sect<<2) | (pp[3]>>6);
    cyl  = pp[3] & 0x3f;
    /*
    cyl = pp[1] >> 2;
    head = ((pp[1] & 0x03)<<6) | (pp[2]>>2);
    sect = pp[2] & 0x03;
    sect = (sect << 8) | pp[3];
    head = pp[1];
    sect = pp[3]>>6;
    sect = (sect<<8) | pp[2];
    cyl  = pp[3] & 0x3f;
    */
    printf("Start Cylinder %d Head %d Sector %d \n", cyl, head, sect );
    head = pp[5];
    sect = pp[6]; sect = (sect<<2) | (pp[7]>>6);
    cyl  = pp[7] & 0x3f;
    cyl = pp[5];
    printf("End   Cylinder %d Head %d Sector %d \n", cyl, head, sect );
#endif
    sector = pp[8] + (1<<8)*pp[9] + (1<<16)*pp[10] + (1<<24)*pp[11];
    printf("Sector number %u\n", sector);
    sector = pp[12] + (1<<8)*pp[13] + (1<<16)*pp[14] + (1<<24)*pp[15];
    printf("Number of sectors %u\n", sector);
    pp += 0x10;
  }
  
}
