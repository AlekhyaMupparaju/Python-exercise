
#include<stdio.h>
int fact(int);

int main()
{
    int n;
    scanf("%d",&n);
   int c= fact(n);
    printf("%d",c);
    return 0;
}
int fact(int num){
    if(num==0){
        return 1;
    }
    else{
    return num*fact(num-1);
    }
}
