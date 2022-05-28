#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
int a,b,c;
int i,j;
int count=0;
int m[101][101]={0};
int d = 0;
int e = 0;
int f = 0; 
int g = 0;
  
scanf("%d",&a);
for(i=0;i<a;i++){
  for(j=0;j<a;j++){
    scanf("%d",&m[i][j]);
  }
}

for(i=0;i<a;i++){
count=0;
  for(j=0;j<a;j++){
    if(m[i][j]==1){
      while(m[i][j]!=0){
      g++;
      j++;
      count++;
      }
      j=a;
    }
  }
if(count>=d){
  d=count;
}
}
if(d==1){
  printf("%d",d);
}else if(g == 100*100){
printf("%d", g);
}
else{
count=0;
f = d;
for(i=0;i<a;i++){
  for(j=0;j<a;j++){
  d = f;
    if(m[i][j]==1){
      while(count!=((d+1)*(d+1))){
        count=0;
          for(b=i;b<(i+d) && b < a;b++){
            for(c=j;c<(j+d) && c < a;c++){
              if(m[b][c]==1){
              count++;
              }else{
              b=a;
              c=a;
              }
            }
          }
          d--;
      }
    if(count>e){
    e=count;
    }
    }
  }
}
printf("%d",e);
}
return 0;
}
