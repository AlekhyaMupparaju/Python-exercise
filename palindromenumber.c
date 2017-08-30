#include<stdio.h>

void main(){
    int n,r,t,p=0;
    scanf("%d",&n);
    t=n;
    while(n>0){
        r=n%10;
        p= p*10 + r;
        n=n/10;
    }
    //printf("%d\n",t);
    //printf("%d\n",p);
    if(t==p){
        printf("number is palindrome");
    }
    else{
        printf("number is not palindrome");
    }
}
