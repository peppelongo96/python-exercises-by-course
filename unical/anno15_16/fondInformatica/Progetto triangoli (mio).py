print ("Decidere il tipo di triangolo...")
lato1= float (input("Inserisci lato 1: "))
lato2= float (input("Inserisci lato 2: "))
lato3= float (input("Inserisci lato 3: "))


if (lato1 == lato2 == lato3):
              print ("Triangolo equilatero")
elif (lato1 == lato2 or lato2 == lato3 or lato1 == lato3):
              print ("Triangolo isoscele")
else :
              print ("Triangolo scaleno")
