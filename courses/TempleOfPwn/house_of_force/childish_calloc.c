int main(void)
{
  size_t choice;
  int turns;
  turns = 0;
  while (turns < 0x32) {
    puts("");
    printf("what_should_i_do");
    __isoc99_scanf("%d",&choice);
    puts("");
    switch(choice) {
    default:
      puts("Bad choice...");
      break;
    case 1:
      find_toy();
      break;
    case 2:
      fix_small_toy();
      break;
    case 3:
      examine_small_toy();
      break;
    case 4:
      big_alloc();
      break;
    case 5:
      exit(0);
    }
    turns = turns + 1;
  }
  return 0;
}

void find_toy(void)

{
  ulong uVar1;
  void *pvVar2;
  ulong size;
  ulong index [2];
  
  if (DAT_00104054 == 0xf) {
    puts("Nothing more!");
  }
  else {
    DAT_00104054 = DAT_00104054 + 1;
    printf("Choose an index: ");
    __isoc99_scanf("%d",index);
    if (((*(long *)(&DAT_00104060 + index[0] * 0x10) == 0) &&
        (*(long *)(&DAT_00104068 + index[0] * 0x10) == 0)) && (index[0] < 0xf)) {
      printf("\nHow much space do you need for it: ");
      __isoc99_scanf("%d",&size);
      uVar1 = index[0];
      if ((size < 0x20) || (0x38 < size)) {
        puts("Your backpack cannot provide this type of space");
      }
      else {
        *(ulong *)(&DAT_00104060 + index[0] * 0x10) = size;
        pvVar2 = calloc(size,1);
        *(void **)(&DAT_00104068 + uVar1 * 0x10) = pvVar2;
        if (*(long *)(&DAT_00104068 + index[0] * 0x10) == 0) {
          puts("Something didn\'t work out...");
                    /* WARNING: Subroutine does not return */
          exit(-1);
        }
        puts("Input your toy\'s details: ");
        read(0,*(void **)(&DAT_00104068 + index[0] * 0x10),size + 1);
      }
    }
    else {
      puts("That\'s a poor choice for an index");
    }
  }
  return;
}

void fix_small_toy(void)
{
  ulong uVar1;
  void *p;
  ulong index;
  ulong size;
  long choice [2];
  printf("Choose an index: ");
  __isoc99_scanf("%d",&index);
  if (((*(long *)(&DAT_00104060 + index * 0x10) == 0) ||
      (*(long *)(&DAT_00104068 + index * 0x10) == 0)) || (0xe < index)) {
    puts("That\'s a poor choice for an index");
  }
  else {
    puts("Ok, let\'s get you some new parts for this one... seems like it\'s broken");
    free(*(void **)(&DAT_00104068 + index * 0x10));
    printf("\nHow much space do you need for this repair: ");
    __isoc99_scanf("%d",&size);
    uVar1 = index;
    if ((size < 0x20) || (0x38 < size)) {
      puts("Your backpack cannot provide this type of space");
    } else {
      *(ulong *)(&DAT_00104060 + index * 0x10) = size;
      p = calloc(size,1);
      *(void **)(&DAT_00104068 + uVar1 * 0x10) = p;
      if (*(long *)(&DAT_00104068 + index * 0x10) == 0) {
        puts("Something didn\'t work out...");
        exit(-1);
      }
      puts("Input your toy\'s details: ");
      read(0,*(void **)(&DAT_00104068 + index * 0x10),size);
      printf("What would you like to do now?\n1. verify the toy\n2. continue\nSelect choice: ");
      __isoc99_scanf("%d",choice);
      if (choice[0] == 1) {
        if (DAT_00104050 == 0) {
          puts(*(char **)(&DAT_00104068 + index * 0x10));
          DAT_00104050 = 1;
        } else {
          puts("Not time");
        }
      }
    }
  }
  return;
}

void examine_small_toy(void)
{
  ulong local_10;
  if (DAT_0010404c == 0) {
    DAT_0010404c = 1;
    printf("Choose an index: ");
    __isoc99_scanf(&DAT_001021a8,&local_10);
    if (((*(long *)(&DAT_00104060 + local_10 * 0x10) == 0) ||
        (*(long *)(&DAT_00104068 + local_10 * 0x10) == 0)) || (0xe < local_10)) {
      puts("That\'s a poor choice for an index");
    }
    else {
      puts(*(char **)(&DAT_00104068 + local_10 * 0x10));
    }
  }
  else {
    puts("Not time");
  }
  return;
}

void big_alloc(void)
{
  size_t size;
  if ((DAT_00104150 == 0) && (DAT_00104158 == (void *)0x0)) {
    printf("How much space do you need for this massive toy: ");
    __isoc99_scanf("%d",&size);
    if (((ushort)size < 0x5b0) || (0xf5c0 < (ushort)size)) {
      puts("We cannot provide this type of space");
    } else {
      puts("Adding to your backpack");
      DAT_00104150 = size;
      DAT_00104158 = malloc(size);
    }
  } else {
    puts("You don't have enough");
  }
  return;
}