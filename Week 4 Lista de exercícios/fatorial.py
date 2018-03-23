n=int(input("Digite o valor de n:"))
if(n==0):
    print(1)
else:
    fatorial=1
    while(n>0):
        fatorial=fatorial*n
        n-=1
    print(fatorial)
