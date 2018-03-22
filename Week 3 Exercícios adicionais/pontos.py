import math
x1=int(input("Digite x1:"))
y1=int(input("Digite y1:"))
x2=int(input("Digite x2:"))
y2=int(input("Digite y2:"))
dist_calc = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(dist_calc)

if(dist_calc>=10):
    print("longe")
else:
    print("perto")
