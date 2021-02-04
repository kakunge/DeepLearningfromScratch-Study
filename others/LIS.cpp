#include <stdio.h>

int d[1001]={1};

int main(void) {
  int n,max=0;
  int arr[1001];
  scanf("%d\n", &n);
  for (int i=0; i<n;i++)
	  scanf("%d",&arr[i]);
  for(int i=0; i<n; i++){
    for(int j=0;j<i;j++){
      if(arr[i] > arr[j]){
        if(d[i] < d[j] + 1){
          d[i] = d[j] + 1;
        }
      }
    }
  }

  max = d[n-1];

  printf("%d",max);
  return 0;
}
