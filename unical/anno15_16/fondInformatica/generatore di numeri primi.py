print ("                        -GENERATORE DI NUMERI PRIMI-")
print (" ")
import time
while True:
 numeromax=int(input("Troverò i numeri primi compresi tra 1 e... "))
 listamax=[]
 listanoprimi=[]
 numeronumerimax=0
 numeronumerinop=0
 tempo_iniziale = time.time()
 
 for i in range(2,numeromax+1):
  listamax.append(i)
  numeronumerimax+=+1
  for i2 in range(2,i-1):
    if (i%i2==0) :
      listanoprimi.append(i)
      numeronumerinop+=+1
      break

 listaprimi=[i for i in listamax if i not in listanoprimi]
 numeronumeriprimi=numeronumerimax-numeronumerinop
 print (" ")
 print ("(1)",listaprimi)
 print (" ")
  
 tempo_finale = time.time()  
 print ("Ho impiegato",str(tempo_finale - tempo_iniziale),"secondi, per calcolare",numeronumeriprimi+1,"numeri primi (considerando l'1).")
 print (" ")

 
        
