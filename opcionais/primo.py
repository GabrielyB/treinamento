#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

import math

n = int(input("Digite um número inteiro: "))

if math.sqrt(n) == int:
    print("não primo")
else:
    if n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0:
        print("não primo")
    else:
        print("primo")