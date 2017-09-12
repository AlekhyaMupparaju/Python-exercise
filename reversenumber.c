#include<stdio.h>
void main(){
    int a,r=0,t;
    scanf("%d",&a);
    while(a!=0){
        t=a%10;
        r=r*10+t;
        a=a/10;
        
    }
    printf("%d",r);
}
