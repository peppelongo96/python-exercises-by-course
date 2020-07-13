fraseCodificata= input ("Inserisci frase cifrata: ")
chiave= int(input ("Insersci chiave: "))

frase= " "
for carattere in fraseCodificata:
       x = ord(carattere) - chiave
       if x < ord("a"):
         x=x+26
       elif x==ord(carattere) - chiave:
         x=32

       frase += (chr(x))

print ("Ecco la tua frase decoodificata: ",frase)
