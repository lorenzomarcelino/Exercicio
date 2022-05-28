#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
int L , C;
int i, j;
int somaP = 0;
int somaS = 0;
int countP = 0;
int countN = 0;

printf("");
scanf("%d %d",&L,&C);

int matriz[L][C];

  for(i=0;i<L;i++){
    for(j=0;j<C;j++){
      printf("",i,j);
      scanf("%d", &matriz[i][j]);
      if (matriz[i][j] > 0){
          countP = countP + 1;
      }
      else if (matriz[i][j] < 0){
          countN = countN + 1;
      }
 	}
}
printf("Matriz formada:\n");

void imprime_matriz(int rows, int cols, int matrix[rows][cols]){
	for (i = 0; i < rows; i++) {
		for (j = 0; j < cols; j++) {
                printf("%d", matrix[i][j]);
            if(j != C - 1)
                printf(" ");
        }
     printf("\n");
	}
}
imprime_matriz( L, C, matriz);
for( i = 0; i < L; i++ ){
    for( j = 0; j < C; j++ ){
			if( i==j )
                somaP += matriz[i][j];
        }
    } 
for( i = 0; i < L; i++ ){
    for( j = 0; j < C; j++ ){
			if((i + j) == (L - 1)){
                somaS += matriz[i][j];
            }
        }
    } 
if(L != C){
	printf("A diagonal principal e secundaria nao pode ser obtida.");
}
else if( L==C ){
	printf( "A diagonal principal e secundaria tem valor(es) %d e %d respectivamente.", somaP ,somaS );
}
printf("\nA matriz possui %d numero(s) menor(es) que zero.", countN);
printf("\nA matriz possui %d numero(s) maior(es) que zero.", countP);
return 0;
}
