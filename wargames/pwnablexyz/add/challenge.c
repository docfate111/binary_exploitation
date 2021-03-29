int main(void)
{
  long i, j, k;
  long stackvar[11];
  unsigned long b = 0;
  while(true){
    i = 0;
    j = 0;
    k = 0;
    for (int t = 10; t > 0; t--; ) {
      stackvar[t] = 0;
    }
    printf("Input: ");
    int args = __isoc99_scanf("%ld %ld %ld",&i,&j,&k);
    if (args != 3) break;
    stackvar[k] = j + i;
    printf("Result: %ld",stackvar[k]);
}
    return 0;
  }