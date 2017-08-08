#include <stdio.h>
void main() {
     int c;
    scanf("%s",&c);
    if((c=='a'||c=='e'||c=='i'||c=='o'||c=='u')||(c=='A'||c=='E'||c=='I'||c=='O'||c=='U'))
    {
        printf("given character is vowel");
    }
    else
    {
        printf("given character is not vowel");
    }
   
}
