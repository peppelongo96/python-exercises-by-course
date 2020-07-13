import math



a = float (input ("Inserisci coefficiente a: "))
b = float (input ("Inaserisci coefficiante b: "))
c = float (input ("Inserisci coefficiante c: "))

delta= b**2 - 4*a*c

if delta > 0 :
    print ("La equazione ammette due soluzioni: ")
    x1= (-b +math.sqrt(delta)) /(2*a)
    x2= (-b -math.sqrt(delta)) /(2*a) 
    print (x1,x2)

elif delta == 0 :
        print ("La equazione ammette una soluzione: ")
        print ((-b)/(2*a))
else :
     print ("La equazione non ammette soluzioni.")

    


    
