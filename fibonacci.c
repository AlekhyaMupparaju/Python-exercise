#include<stdio.h>
void main(){
    int n,i,a=-1,b=1,c,t;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        t=a+b;
        a=b;
        b=t;
        printf("%d\t",t);
    }
}
