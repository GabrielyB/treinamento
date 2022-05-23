#Exercício 5 - Verificando ordenação
#Receba 3 números inteiros na entrada e imprima
#crescente
#se eles forem dados em ordem crescente. Caso contrário, imprima 
#não está em ordem crescente

primeiro = int(input("Digite o primeiro número inteiro "))
segundo = int(input("Digite o segundo número inteiro "))
terceiro = int(input("Digite o terceiro número inteiro "))

if primeiro < segundo < terceiro:
    print("crescente")
else:
    print("não está em ordem crescente")