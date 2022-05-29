# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

n = int(input("Digite o valor de n: "))

m = 0 
p = 0

while n != 0:
    m = m + 1
    if m%2 == 1:
        print(m)
        n = n - 1
