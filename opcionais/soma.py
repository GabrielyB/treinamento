tamanho =  int(input("Quantos números você deseja somar? "))
soma = 0
i = 0
while i<tamanho:
    valor = float(input("Digite os números que você deseja somar "))
    soma = soma + valor
    i = i + 1
print ("O resultado da soma é ",soma)

