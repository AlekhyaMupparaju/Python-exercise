#include<stdio.h>

void main(){
   int n,sum=0;
   scanf("%d",&n);
   for(int i=1;i<=n;i++){
       sum=sum+i;
   }
   printf("sum of first %d number is: %d",n,sum);
}
