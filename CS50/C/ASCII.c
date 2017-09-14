#include <stdio.h>
/*
int main(void)
{
    // A = 65 in ASCII
    int i;
    for (i = 0; i <128; i++)
    {
        printf("%c in ASCII is %i\n",i, i);
    }
}
*/

main()
{
    char C[50] = "AhgiAgbkBKLujbYKBKbKbgkb";
    int len = strlen(C);
    int i;
    for (i = 0; i < len; i++)
    {
        if ('a' <= C[i] && C[i] <= 'z')
        {
            printf("%c",C[i]-32);
        }
        else
        {
            printf("%c",C[i]);
        }
    }
    printf("\n");
    printf("%s (The original string)",C);
}
