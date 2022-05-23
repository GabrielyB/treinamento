#ele deve calcular as equações de segundo grau.
#se o delta for igual a zero só uma raiz
#delta menor que zero não tem raizes reais
#delta maior que zero duas raizes

import math
from re import S, X 

a = float(input("Qual o valor de a? "))
b = float(input("Qual o valor de b? "))
c = float(input("Qual o valor de c? "))

delta = b**2 - 4*a*c

if a == 0 or b == 0 or c == 0:
    print("Esta equação não é de segundo grau. Tente um outro programa.")
else:                
    if delta < 0:
        print ("esta equação não possui raízes reais")  
    else:
        if delta == 0:
            equação = (-b + 0)/(2*a)
            print("a raiz desta equação é",equação)
        else:
            if delta > 0:
                deltaS = math.sqrt(delta)
                x1 = (-b + deltaS)/(2*a)
                x2 = (-b - deltaS)/(2*a)
                if x1>x2:
                   print("as raízes da equação são",x2,"e",x1)
                else:
                   print("as raízes da equação são",x1,"e",x2)
