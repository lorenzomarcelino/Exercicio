#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(void){

int m[3][3];
int l = 0;
int i, j, k;

while(scanf("%d %d %d", &i, &j, &k) != EOF){
        m[l][0] = i;
        m[l][1] = j;
        m[l][2] = k;
l++;
if(l%3 == 0){
    l = 0;
    if(m[1][0]==0 && m[2][0]==0 && m[2][1]==0){
            printf("Por baixo\n");
        }
        else if(m[0][1]==0 && m[0][2]==0 && m[1][2]==0){
            printf("Por cima\n");
        }
        else{
            printf("Nao pode atravessar\n");
        }
}
}
return 0;
}
