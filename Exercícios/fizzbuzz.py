#Exercícios 4 - FizzBuzz parcial, parte 3
#Receba um número inteiro na entrada e imprima
#FizzBuzz
#na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

número = int(input("Digite um número inteiro "))

if número%3 == 0 and número%5 == 0:
    print("FizzBuzz")
else:
    print(número)