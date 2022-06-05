#Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

def maximo(x, y):
    if x > y:
        maior = x
    elif x == y:
        maior = x
    else:
        maior = y
    return maior

x = int(input("x "))
y = int(input("y "))
grande= maximo(x, y)
print(grande)
