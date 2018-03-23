numero=int(input("Digite um número inteiro:"))
eh_adjacente=False
referencia=numero%10
numero=numero//10

while(not eh_adjacente and numero>0):
    if(referencia!=numero%10):
        referencia=numero%10
        numero=numero//10
    else:
        eh_adjacente=True

if (eh_adjacente):
    print("sim")
else:
    print("não")
