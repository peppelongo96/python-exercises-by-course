while True :
    import math
    print(" ")
    max= int (input("Inserisci limite delle terne: "))
    print (" ")
    numero=0
    for a in range (1,max):
        for b in range (1,max):
            c=int(math.sqrt (a**2+b**2))
            if c**2==a**2+b**2:
                    numero=numero + 1
                    print ("| ",a," | ",b," | ",c," | ")
                    print (a**2,"+",b**2,"=",c**2)
                    print (a**2 + b**2,"=",c**2)
                    print (" ")
    print (" ")
    print ("Con a e b definiti entro",max,", avremo al massimo",numero,"terne.")

   
