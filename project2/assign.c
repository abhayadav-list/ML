#include <stdio.h>
#define MAX 100
int arr[MAX];
int main()
{
  printf("enter the number of elements \n");
  int n;
  scanf("%d",&n);
printf("Enter the %d elements\n");
  for (int i = 0; i < n; ++i)
  {
   scanf("%d",&arr[i]);
  }

  printf("Enter no to search in the list\n");
  int x;
  scanf("%d",&x);
  int i;
  for (i = 0; i < n; ++i)
  {
    if (arr[i]==x)
    {
      printf("found %d at %d position\n",x,i+1);
      break;
    }
    if(i==n)
    {
      printf("Not found\n");
    }
    return 0;
    }
}