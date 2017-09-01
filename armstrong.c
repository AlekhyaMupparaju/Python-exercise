#include<stdio.h>

void main()
{
    int n, t, sum = 0, r;
    scanf("%d", &n);
    t = n;
    while(n != 0)
    {
        r = n % 10;
        sum = sum + (r * r * r );
        n = n / 10;
    }
    if(sum == t)
    {
        printf("\nnumber is an Armstrong Integerr\n");
    }
    else
    {
        printf("\nnumber is not an Armstrong Integer\n");
    }
    
}
