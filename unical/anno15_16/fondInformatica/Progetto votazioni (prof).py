giorno = int (input("giorno: ")

mese= int (input("mese: ")
anno = int (input("anno: ")

go=12
mo=10
ao=2015

anno= anno +18
voto= False


if ao > anno :
            voto = True
elif ao == anno :
            if mo > mese :
                voto = True
            elif mo == mese :
                 if go > giorno :
                     voto = True
                 elif go == giorno :
                      print ("Buon compleanno")
if voto :
    print ("Vota bene...")
else :
    print ("Non puoi ancora votare")
