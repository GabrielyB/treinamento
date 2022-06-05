#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

n = int(input("Digite um número inteiro: "))

if n%2 == 0 and n>2 or n%3 == 0 and n>3 or n%5 == 0 and n>5 or n%7 == 0 and n>7 or n == 0 or n == 1:
    print("não primo")
elif n == 2 or n == 3 or n == 5 or n == 7:
    print("primo")
else:
    print("primo")