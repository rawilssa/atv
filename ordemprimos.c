#include <stdio.h>
#include <math.h>
#include <locale.h>

int ordemprimo(int n)
{
    int x, d, cont = 0, q=0;
    setlocale(LC_ALL, "Portuguese");

    for(d=1,cont=0;d<=x;d++)
    {
            if(x % d == 0)
                 cont++;
        if(cont == 2)
			printf("%d é primo\n",x);
        else
            printf("O número informado não pertence à sequência de primos.\n",x);
    }
    q += 1;
    return x;
}
    

main()
{
    int p, n;
    printf("qual o número?\n", p);
    scanf("%d", &p);
    p = ordemprimo(n);
    printf("o %d é o %d° número primo \n", p, n);
}


