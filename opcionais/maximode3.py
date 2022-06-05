#Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

def maximo(x, y, z):
    if x >= y and x >= z:
        resultado = x
    elif y >= x and y >= z:
        resultado = y
    elif z >= x and z >= y:
        resultado = z
    return resultado

x = int(input("x "))
y = int(input("y "))
z = int(input("z "))

print(maximo(x, y, z))

