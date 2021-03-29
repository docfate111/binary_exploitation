int main(void)

{
  int i = 0;
  int j = 0;
  __printf_chk(1,"1337 input: ");
  __isoc99_scanf("%u %u",&i,&j);
  if ((i < 0x1337) && (j < 0x1337)) {
    if (i - j == 0x1337) {
      system("cat /flag");
    }
  } else {
    puts("Sowwy");
  }
  return 0;
}