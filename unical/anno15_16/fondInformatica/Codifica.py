frase=input("Inserisci frase: ")
chiave=int(input("Inserisci chiave di cifratura: "))

fraseCriptata=" "
for carattere in frase:
    x=ord(carattere)+ chiave
    if x > ord ("z"):
       x=x-26
    elif x==ord(" ")+ chiave :
        x=32

    fraseCriptata +=(chr(x))

print("Ecco la tua frase criptata:",fraseCriptata)
