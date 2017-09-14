#include <stdio.h>

int main(void)
{
    char * s = "FengWeilei";
    int i;
    for (i = 0; i < strlen(s); i++)
    {
        printf("%c\n",s[i]);
    }
    printf("%s\n",s );
    printf("The length of s is %i\n",strlen(s) );
}
