while True :
    numberofdivisor=0
    numero=int(input("Inserisci numero: "))
    for i in range (1,numero+1):
       if numero % i == 0:
            numberofdivisor+=+1
            print ("Il suo numero è divisibie per",i)
    if numberofdivisor==2 :
        print (" ")
        print ("  ",numero,"è primo.")
        print (" \------------/")
        print (" ")
    elif numberofdivisor > 2 :
        print (" ")
        print (" ",numero,"ammette altri divisori oltre 1 e se stesso, quindi non è primo.")
        print (" \------------------------------------------------------------------/ ")
        print (" ")
    
