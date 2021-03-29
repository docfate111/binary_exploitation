int main(void)
{
  long *plVar1;
  void *__buf;
  long in_FS_OFFSET;
  size_t n;
  long lStack32;
  puts("Welcome.");
  p = (long *)malloc(0x40000);
  *p = 1;
  __printf_chk(1,"Leak: %p\n",plVar1);
  __printf_chk(1,"Length of your message: ");
  n = 0;
  __isoc99_scanf("%lu",&n);
  __buf = malloc(n);
  __printf_chk(1,"Enter your message: ");
  read(0,__buf,n);
  *(undefined *)((long)__buf + (n - 1)) = 0;
  // writes buffer to stdout
  write(1,__buf,n);
  if (*p == 0) {
    system("cat /flag");
  }
  return 0;
}