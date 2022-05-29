#Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

n = int(input("Digite um número inteiro: "))

resto = 1
soma = 0

while resto != 0:
    ultimo = n%10
    resto = n//10
    n = resto
    soma = soma + ultimo
print(soma)