#include <stdio.h>

int c=0;

void hanoi(int n, int from, int by, int to) {
    
    c++;
    
    if(n==1) {
        printf("%d %d\n", from, to);
        return;
    }
	hanoi(n-1, from, to, by);
    printf("%d %d\n", from, to);
    hanoi(n-1, by, from, to);
}

int main(void) {
  int n;
  scanf("%d",&n);
  hanoi(n, 1, 2, 3);
  printf("%d", c);
  return 0;
}
