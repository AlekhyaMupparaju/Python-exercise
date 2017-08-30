#include<stdio.h>

void main(){
    int base,expo,power=1,i;
    scanf("%d %d ",&base,&expo);
    for(i=1;i<=expo;i++){
        power=power*base;
    }
    printf("power is:%d",power);
}
