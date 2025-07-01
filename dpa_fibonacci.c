#include <stdio.h>
//verifique se um numero de fibonacci pode ser defectivo//
int soma_divisores(int num) {
    int soma = 0;
    for (int i = 1; i < num; i++)
        if (num % i == 0) soma += i;
    return soma;
}

int main() {
    int n, a = 1, b = 0, c = a + b;

    printf("Digite um número de Fibonacci: ");
    scanf("%d", &n);

    while (c < n) c = a + b, a = b, b = c;

    printf("%d %sé defectivo.\n", n, (soma_divisores(n) < n) ? "" : "não ");
    return 0;
}