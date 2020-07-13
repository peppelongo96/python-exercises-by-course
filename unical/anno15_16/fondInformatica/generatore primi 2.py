import time
while True:
    print (" ")
    numeromax=int(input("Calcolerò numeri primi nell'intervallo 1 - "))
    listaprimi=[]
    numeroprimi=0
    tempostart=time.time()
    
    for  i in range (1,numeromax):
        primo=True
        for i2 in range (i-1,1,-1):
            if i%i2==0:
                  primo=False
        if primo:
            numeroprimi+=+1
            listaprimi.append(i)

    print (" ")
    print (listaprimi)
    print (" ")
    tempoend= time.time()
    tempotot = float(tempoend-tempostart)
    print ("Ho impiegato",tempotot,"secondi, per determinare",numeroprimi,"numeri primi.")
    if tempotot > float(5) :
        print ("Vorrei vedere te a calcolarli in un tempo minore u.u")
        print (" ")
    
