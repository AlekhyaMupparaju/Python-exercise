#include<stdio.h>

void main()
{
    int n1, n2, t, sum, r, i;
    scanf("%d %d", &n1,&n2);
    for(i=n1+1;i<n2;i++){
    
    t = i;
    sum=0;
    while(t!= 0)
    {
        r = t % 10;
        sum = sum + (r * r * r );
        t = t / 10;
    }
    if(i == sum)
    {
        printf("%d",i);
        }
        }
    
}
