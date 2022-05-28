#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main(){
int n2 = 0, n5 = 0, n10 = 0, n20 = 0, n50 = 0, n100 = 0;
int m1 = 0, m5 = 0, m10 = 0, m25 = 0, m50 = 0, m100 = 0;
float valor = 0;

printf("");
scanf("%f",&valor);
valor = valor * 100;

do
{
if(valor>=10000)
{
valor-=10000;
n100++;
}

else if(valor>=5000)
{
valor-=5000;
n50++;
}

else if(valor>=2000)
{
valor-=2000;
n20++;
}

else if(valor>=1000)
{
valor-=1000;
n10++;
}

else if(valor>=500)
{
valor-=500;
n5++;
}

else if(valor>=200)
{
valor-=200;
n2++;
}

else if(valor>=100)
{
valor-=100;
m100++;
}

else if(valor>=50)
{
valor-=50;
m50++;
}

else if(valor>=25)
{
valor-=25;
m25++;
}

else if(valor>=10)
{
valor-=10;
m10++;
}

else if(valor>=5)
{
valor-=5;
m5++;
}

else if(valor>=1)
{
valor-=1;
m1++;
}

}while(valor!=0);

if (n100>0)
{
    printf("\n%d nota(s) de R$ 100.00",n100);
}

if (n50>0)
{
    printf("\n%d nota(s) de R$ 50.00",n50);
}

if (n20>0)
{
    printf("\n%d nota(s) de R$ 20.00",n20);
}

if (n10>0)
{
    printf("\n%d nota(s) de R$ 10.00",n10);
}

if (n5>0)
{
    printf("\n%d nota(s) de R$ 5.00",n5);
}

if (n2>0)
{
    printf("\n%d nota(s) de R$ 2.00",n2);
}

if (m100>0)
{
    printf("\n%d moeda(s) de R$ 1.00",m100);
}

if (m50>0)
{
    printf("\n%d moeda(s) de R$ 0.50",m50);
}

if (m25>0)
{
    printf("\n%d moeda(s) de R$ 0.25",m25);
}

if (m10>0)
{
    printf("\n%d moeda(s) de R$ 0.10",m10);
}

if (m5>0)
{
    printf("\n%d moeda(s) de R$ 0.05",m5);
}

if (m1>0)
{
    printf("\n%d moeda(s) de R$ 0.01",m1);
}
return 0;
}
