#Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele fand uma vogal e False se fand uma consoante.

def vogal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    else:
        return False

def test_vogal0():
    assert vogal("a") 
def test_vogal1():
    assert vogal("e") 
def test_vogal2():
    assert vogal("i") 
def test_vogal3():
    assert vogal("o") 
def test_vogal4():
    assert vogal("u") 