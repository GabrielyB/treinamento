#Um número binomial é aquele produzido por dois elementos, ligados por um sinal de adição ou subtração.
#o cálculo do valor de um número binominal é (n/k) == n!/k!(k - n)! sendo k>=n 

def fatorial(n, k):
    subtração = n - k
    f2 = subtração
    if subtração == 1 or subtração == 0:
        f2 = 1
    else:
        while subtração > 1:
            subtração = subtração - 1
            f2 = f2*subtração
    f = n
    f_= k
    if n == 1 or n == 0:
        f = 1
    elif k == 1 or k == 0:
        f_ = 1
    else:
        while n > 1:
            n = n - 1
            f = f*n
        while k > 1:
            k = k - 1
            f_ = f_*k

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))
fatorial(n, k)

print("O resultado dos números binominais é: ", fatorial(n, k))