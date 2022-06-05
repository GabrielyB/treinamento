# Fazer um programa que diga se o número digitado tem dois números adjacentes iguais.

numero = float(input("Digite um número: "))
n = 0
while numero != 0:
    b = numero%10 
    numero = numero//10
    c = numero%10
    if b == c:
        n = n + 2
    
if n%2 == 0 and n > 0:
    print("Há números adjacentes.")
else:
     print("Não há números adjacentes.")
            