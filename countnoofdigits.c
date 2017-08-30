#include<stdio.h>

void main(){
  int n,count=0;
    scanf("%d",&n);
    while(n!=0){
        n=n/10;
        count=count+1;
    }
    printf("number of digits of an integer is:%d",count);
}
