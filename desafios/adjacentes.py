# Fazer um programa que diga se o número digitado tem dois números adjacentes iguais.

numero = float(input("Digite um número: "))
y = 1
a = numero%10 
y = numero//10

while y != 0:
    b = y%10 
    y = y//10
    c = y%10
    if a == b or b == c:
        print("Há números adjacentes.")
    else:
        print("Não há números adjacentes.")
            