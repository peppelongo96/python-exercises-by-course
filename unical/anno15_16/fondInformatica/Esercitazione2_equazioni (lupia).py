import math



a = int(input("Inserisci il valore di a:> "))


b = int(input("Inserisci il valore di b:> "))

c = int(input("Inserisci il valore di c:> "))


delta = b**2 - 4*a*c


if delta < 0:
    print("Questa equazione non ammette soluzioni")

elif delta == 0:
    print("Questa equazione ammette una sola soluzione")
    x = -b / (2*a)
    print("e in particolare è x=",x)

else:
    print("Questa equazione ammette due soluzioni")
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("e in particolare sono x1=",x1,"e x2=", x2)

