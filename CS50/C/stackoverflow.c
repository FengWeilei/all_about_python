#include "stdio.h"

int main(void)
{
    char name[9];
    printf("Type your name:");
    gets(name);
    printf("Hello, %s\n",name);
    printf("%s\n",'MY' );
    return 0;
}
