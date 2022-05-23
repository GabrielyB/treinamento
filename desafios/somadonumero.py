#um progrma que pegue um número qualquer e faça a soma dos números que compõem o número

n = int(input("Digite um número inteiro: "))

resto = 1

soma = 0

while resto != 0:
    ultimo = n%10
    resto = n//10
    n = resto
    soma = soma + ultimo
    
print("O valor da soma dos números é: ",soma)