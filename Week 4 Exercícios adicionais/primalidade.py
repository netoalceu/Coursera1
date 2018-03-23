n=int(input("Digite um número inteiro:"))
e_primo=False
contador=n-1
if(n==2):
    e_primo=True
    contador=0
while (contador>1):
    if(n%contador==0):
        e_primo=False
        break
    else:
        e_primo=True
        contador-=1

if (e_primo):
    print("primo")
else:
    print("não primo")
