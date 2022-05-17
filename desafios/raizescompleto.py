#ele deve calcular as equações de primeiro e segundo grau.

import math
from re import X 

a = float(input("Qual o valor de a? "))
b = float(input("Qual o valor de b? "))
c = float(input("Qual o valor de c? "))

delta = b**2 - 4*a*c

if a == 0:
        x = b/c
        print("Esta é uma equação de primeiro grau cujo resultado é ",x)
else:
    if b==0 and ((-c)/a) > 0:
        x = math.sqrt((-c)/a) 
        print("Esta é uma equação de primeiro grau cujo resultado é ",x)
    else:
        if b==0 and ((-c)/a) < 0:
                print("Não há resultado, já que não existe uma raiz real para números negativos")  
        else:
            if c == 0:
                x = ((-b)/a)
                print("Esta é uma equação de primeiro grau cujo resultado é ",x)
            else:
                if delta == 0:
                     print("O valor de delta é ",delta)
                     equação = (-b + 0)/(2*a)
                     print("O valor da equação é:",equação)  
                else:
                 if delta < 0:
                     print("O valor de delta é ",delta)
                     print ("Já que o delta é menor que zero, a equação não tem raízes reais") 
                 else:
                    if delta > 0:
                        print("O valor de delta é ",delta)
                        deltaS = math.sqrt(delta)
                        x1 = (-b + deltaS)/(2*a)
                        x2 = (-b - deltaS)/(2*a)
                        print("Os valores da equação são:",x1,"e",x2)
              