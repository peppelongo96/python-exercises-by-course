print ("Salve! Hai di fronte un semplice applet in grado di verificare la tua idoneità al voto in Italia.")
print ("Per fare ciò, è necessario che inserisci progressivamente giorno, mese e anno, se richiesti, della tua data di nascita.")
print (" ")
while True :
 print (" ")
 anno= int (input ("Inserisci il tuo anno di nascita: "))
 if (anno < 1997 and anno > 1910 and anno < 2015):
    print (" ")
    print ("Vai a votare oraaaa!")
    print ("Poiché tu dovresti avere circa...")
    print (2015- anno,"anni")
   
 elif (anno > 1997 and anno < 2015):
    print (" ")
    print ("Statti a casa.")
    print ("Piccolino...hai ancora",2015 - anno,"anni")
 elif (anno < 1910 or anno >= 2015):
    print (" ")
    print ("Mi pigghi po culu!?")
    print ("Vorrei conoscere quel deficiente che potrebbe mai credere che tu abbia",2015-anno,"anni!")
 else :
    print (" ")
    mese= int(input("Adsesso verifichiamo il mese... "))
    if (mese > 10 and mese <= 12):
        print (" ")
        print ("Mi dispiace...non puoi votare ancora...ma è solo questione di mesi ;)")

    elif (mese < 10 and mese != 0):
        print (" ")
        print ("Puoi correre liberamente allo sportello più vicino e reclamare i tuoi diritti!")
    elif (mese <= 0 or mese > 12):
        print (" ")
        print ("... Mi pigghi pe scem'?!")
    else:
        print (" ")
        giorno= int (input("Quindi è solo questione di giorni... Inserisci il giorno, su: "))
        if (giorno > 9 and giorno < 31):
            print (" ")
            print ("Per pochissimi giorni puoi...non votare, mi dispiace.")
            print (giorno," \ ",mese," \ ",anno)
        elif (giorno < 9 and giorno <31 and giorno != 0):
            print (" ")
            print ("Ti sei salvato per un soffio! Votaaaa!!")
            print (giorno," \ ",mese," \ ",anno)
        elif (giorno <= 0 or giorno > 31):
            print (" ")
            print ("Si... e io so fare il caffé u.u")
            print ("Non sapevo esistesse il",giorno,"giorno!")
        else :
            print (" ")
            print ("Sei fortunato! Esattamente quest'anno sei uno tra i primi ad acquisire il diritto di voto!")
            print ("Buon compleanno allora dato che sei nato oggi",giorno,mese,anno)            
            
 print (" ")
 print ("Addio.")



                    
                    
                    
            
            
    
        



        










    

              
