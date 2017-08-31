#include<stdio.h>

void main(){
    int no,flag=1;
    scanf("%d",&no);
    for(int i=2;i<=no/2;i++){
    if((no%i)==0){
        flag=0;
        break;
            } 
    }
    if(flag==0){
        printf("given number is not prime");
    }
    else{
        printf("given number is prime");
    }

}
