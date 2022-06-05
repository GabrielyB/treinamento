def maximo(x, y, z):
    if x >= y and x >= z:
        resultado = x
    elif y >= x and y >= z:
        resultado = y
    elif z >= x and z >= y:
        resultado = z
    return resultado

def test_maximo0():
    assert maximo(0, -1, 13) == 13
def test_maximo1():
    assert maximo(2, 2342, 32) == 2342
def test_maximo2():
    assert maximo(-2, -5, -17) == -2
def test_maximo3():
    assert maximo(123, 23, 12) == 123
def test_maximo4():
    assert maximo(12, 11, 12) == 12