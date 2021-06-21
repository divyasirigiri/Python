/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    if(n<0)
    printf("Wrong Input");
    else{
        int square = n*n;
        int temp = square%10;
    
        if(temp == n)
        {
            printf("Correct number");
        }
        else{
            printf("Incorrect number");
        }
    }
    return 0;
}
