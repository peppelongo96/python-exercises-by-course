def leggi_anno():
    anno = int(input("Inserisci l'anno: "))
    while anno < 1583 :
        print("L'anno inserito non è gregoriano.")
        anno = int(input("Inserisci di nuovo l'anno: "))
    return anno

def anno_bisestile(anno):
    if anno%100==0 and anno%400!=0:
        return False
    elif anno%4==0:
        return True
    return False

def giorno_primo(anno):
    totale_anni = anno - 1800
    totale_anni_bisestili = 0
    for i in range (anno,1800,-1):
        if anno_bisestile(i)== True:
            totale_anni_bisestili+=1
    totale_giorni = totale_anni*365 + totale_anni_bisestili
    giorno_primo = (totale_giorni)%7 
    giorno_primo = (giorno_primo + 5)%7 
    return giorno_primo

def stampa_mese(numero_mese):
    mesi=["GENNAIO","FEBBRAIO","MARZO","APRILE","MAGGIO","GIUGNO","LUGLIO","AGOSTO","SETTEMBRE","OTTOBRE","NOVEMBRE","DICEMBRE"]
    return (mesi[numero_mese-1])

def durata_mese(anno,mese):
    durata_mesi=[31,28,31,30,31,30,31,31,30,31,30,31]
    if anno_bisestile(anno):
        durata_mesi[1]=29
    return durata_mesi[mese-1]

def stampa_intestazioni():
    print("LU"+"\t"+"MA"+"\t"+"ME"+"\t"+"GI"+"\t"+"VE"+"\t"+"SA"+"\t"+"DO")
    print("---------------------------------------------------")

def stampa_offset(g):
    cont = 0
    while cont < g :
        print("",end="\t")
        cont = cont +1

def calcolo_approssimato_eclissi_gemelle(anno):
    totale_anni=anno-1800
    totale_anni_bisestili = 0
    z=11
    for i in range (anno,1800,-1):
        if anno_bisestile(i)== True:
            totale_anni_bisestili+=1
    if totale_anni_bisestili==3:
        z=12
    elif totale_anni_bisestili==5:
        z=10
    num_eclissi = (totale_anni*365)//(6570+z)
    return (num_eclissi)

print (" ")
print("                           CALENDARIO PERPETUO")
print (" ")
while True:

    anno = leggi_anno()
    print (" ")
    giorno_primo = giorno_primo(anno)
    mese = 1

    while mese <= 12 :
        durata = durata_mese(anno,mese)
        print(stampa_mese(mese),anno)
        print(" ")
        stampa_intestazioni()
        stampa_offset(giorno_primo)
        giorno = 1
        contatore = giorno_primo
        while giorno <= durata:
            if contatore < 6:
                print(giorno, end='\t')
            else:
                print(giorno)
            contatore = (contatore + 1) % 7
            giorno = giorno + 1
        giorno_primo = (giorno_primo + durata)%7
        mese = mese +1
        print (" ")
        print (" ")
        print (" ")
        print (" ")

    eclissi=calcolo_approssimato_eclissi_gemelle(anno) 
    print (" ")
    if anno > 1800:
        print ("- Dal 1800 fino al",anno,", sono definite approssimativamente",eclissi,"eclissi gemelle -")
        print (" ")
    



    
