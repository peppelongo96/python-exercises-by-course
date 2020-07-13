print ("Decidere il tipo di triangolo")


a= float(input("inserisci lato 1: "))
b= float (input ("Inserisci lato 2: "))
c= float (input ("Inserisci lat 3: "))

print ("Lato 1: ", a)
print ("Lato 2: ", b)
print ("Lato 3: ", c)

if a==b and b==c:
    print ("Triangolo equilatero")
elif a==b or b==c or a==c:
    print ("Trinagolo isoscele")
else:
    print ("Triangolo scaleno")
