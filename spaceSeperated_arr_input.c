#include<stdio.h>
#include<stdlib.h>
#define max 30

int main(void)
{
    int *arr, n, i, j, temp;
    char *input;
    printf("Enter the length: ");
    scanf("%d", &n);
    fflush(stdin);
    arr = (int *)malloc(n*sizeof(int));
    input = (char *)malloc(max*sizeof(char));
    fgets(input, max, stdin);
    temp = j = 0;
    for (i = 0; input[i]!='\0'; i++)
    {
        if (input[i] != ' ' && input[i]!='\n')
        {
            temp = temp*10 + ((int)input[i] - 48);   
        }
        else
        {
            arr[j] = temp;
            j++;
            temp = 0;
        }        
    }
    for (i = 0; i < n; i++)
    {
        printf("%d | ", arr[i]+2);
    }

    
    return 0;
}