#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int mult(int a, int b){
if (a < b)
        return mult(b, a);
    else if (b != 0)
        return (a + mult(a, b - 1));
 
    else
        return 0;
}
int main(){
int i;
int j = 0;
int a[3]={};

while(scanf("%d", &i) != EOF){
a[j] = i;
j++;
if(j%3 == 0){
  j = 0;
  if (a[1] - mult(a[0], a[2]) < 0)
  {
    printf("Nao\n");
  }
  else
  {
    printf("Sim\n");
  }
}
}
return 0;
}
