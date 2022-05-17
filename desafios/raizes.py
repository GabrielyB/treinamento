#ele deve calcular as equações de segundo grau.
#se o delta for igual a zero só uma raiz
#delta menor que zero não tem raizes reais
#delta maior que zero duas raizes

import math
from re import X 

a = float(input("Qual o valor de a? "))
b = float(input("Qual o valor de b? "))
c = float(input("Qual o valor de c? "))

delta = b**2 - 4*a*c
print("O valor de delta é ",delta)

if a == 0 or b == 0 or c == 0:
    print("Esta equação não é de segundo grau. Tente um outro programa.")
else:                
    if delta < 0:
        print ("Já que o delta é menor que zero, a equação não tem raízes reais")  
    else:
        if delta == 0:
            equação = (-b + 0)/(2*a)
            print("O valor da equação é:",equação)
        else:
            if delta > 0:
                deltaS = math.sqrt(delta)
                x1 = (-b + deltaS)/(2*a)
                x2 = (-b - deltaS)/(2*a)
                print("Os valores da equação são:",x1,"e",x2)
