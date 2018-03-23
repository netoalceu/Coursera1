n=int(input("Digite o valor de n:"))
if(n==0):
    print("")
else:
    numero_impar=1
    while(n>0):
        print(numero_impar)
        numero_impar+=2
        n-=1
