#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

def maior_primo(x):
    primo = 0
    while x > 2 and primo != x:
        if x == 3 or x == 5 or x == 7:
            primo = x
        elif x%2 == 0 and x>2 or x%3 == 0 and x>3 or x%5 == 0 and x>5 or x%7 == 0 and x>7:
            x = x - 1 
        else:
            primo = x 
    return primo 
