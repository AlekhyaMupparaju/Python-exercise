#include <stdio.h>
void main() {
     int c;
    scanf("%s",&c);
    if((c>='a' && c<='z')||(c>='A' && c<='Z'))
    {
        printf("given character is alphabet");
    }
    else
    {
        printf("given character is not alphabet");
    }
   
}
