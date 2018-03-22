import math
a=int(input("Digite a:"))
b=int(input("Digite b:"))
c=int(input("Digite c:"))

if(b**2 < 4*a*c):
    print("esta equação não possui raízes reais")
else:
    if (b**2 == 4*a*c):
        print("a raiz desta equação é X")
    else:
        print("as raízes da equação são X e Y")
