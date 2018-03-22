# -*- coding: utf-8 -*-
import math
a=float(input("Digite a:"))
b=float(input("Digite b:"))
c=float(input("Digite c:"))
if(b**2 < 4*a*c):
    print("esta equação não possui raízes reais")
else:
    if(b**2 == 4*a*c):
        x1=(-b + math.sqrt(b**2-4*a*c))/(2*a)
        print("a raiz desta equação é %0.2f" % x1)
    else:
        x1=(-b + math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b - math.sqrt(b**2-4*a*c))/(2*a)
        print(x1,x2)
        if(x1<x2):
            print("as raízes da equação são %0.2f e %0.2f" %(x1,x2))
        else:
            print("as raízes da equação são %0.2f e %0.2f" %(x2,x1))

#O resultado dos testes com seu programa foi:

#***** [0.3 pontos]: Testando Báskara com uma raiz real (a = 9, b = -12, c = 4) - Falhou *****
#AssertionError: ('Esta equação tem exatamente uma raiz, mas a resposta recebida foi\n%s', 'a raiz desta equação é X\n')

#***** [0.4 pontos]: Testando Báskara com 2 raízes reais (a = 1, b = -3, c = -10) - Falhou *****
#AssertionError: As raízes devem ser listadas em ordem crescente
