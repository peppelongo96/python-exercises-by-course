print ("Salve! Questo è un semplice script adibito al calcolo di una potenza A^N, con esponente da 0 a N.")

while True:

 try:
  print (" ")
  A= int(input("Inserisci base della potenza: ")) #utilizzare int o float (float mostrerà inf)
  if A == 0 :
       print ("Secondo me avrai sempre 0 come risultato...che ne pensi?!")
  else :
    N = int(input("Inserisci esponente intero positivo della potenza: "))
    if (N == 0 ):
       print ("La tua potenza sarà sempre uguale a 1 in questo modo.")
    elif (N < 0) :
         print ("Mi sembra di aver specificato INTERO POSITIVO! O no?!")
    else :
       risultato = 1
       for i in range (N+1):
           risultato = risultato * A
           print ("La potenza di",A,"elevato",i,"equivale a: ",risultato)

 except ValueError :
           print ("Solo esponenti interi, mi spiace.")
            
 print ("Good Luck!")
 
