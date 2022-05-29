# Fazer um programa que receba um número natural e imprima o seu fatorial.
#tambem poderia ser usado o comando math.factorial(x)

n = int(input("Digite o valor de n: "))

fatorial = n

if n == 1 or n == 0:
    fatorial = 1
else:
    while n != 1:
        n = n - 1
        fatorial = fatorial*n
print(fatorial)

