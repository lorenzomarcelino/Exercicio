#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(void){
int L,C;
int voto = 0;
int somav = 0;
int i, j;

scanf("%d %d", &C,&L);

int matriz[L][C];

for(i = 0; i < L; i++){
    for(j = 0; j < C; j++){
        scanf("%d", &matriz[i][j]);
    }
}

for(;voto < C; voto++){
  somav = 0;
    for(i = 0; i < L ;i++){
        for(j=0; j < C ;j++){
            if (j == voto){
            somav = somav + matriz[i][j];
            }
        }
    }
printf("Princesa %d: %d voto(s)\n",voto + 1, somav);
}
return 0;
}
