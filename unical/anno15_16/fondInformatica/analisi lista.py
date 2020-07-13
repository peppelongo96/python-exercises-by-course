while True:
    k=int(input("Inserisci numero K: "))
    
    n=int(input("Inserisci numero di posizioni nell'array: "))
    v=[0]*n
    for i in range(n):
        v[i]=int(input("Inserisci elemento in posizione "+ str(i)+" : "))
            
    maximum=v[0]
    minimum=v[0]
    dispari=0
    pari=0
    print ("La lista è così composta:",v)

    for i in v:
        if maximum < i:
          maximum=i
        if minimum > i:
          minimum=i
        if i % 2 ==0 :
            pari+=1
        else:
            dispari+=1

    
    print ("Il numero più piccolo della lista è",minimum)
    print ("Il numero più grande della lista è",maximum)

    if k > maximum:
        print ("K è più grande di tutti i numeri della lista")
    elif k == maximum:
        print ("K è uguale al numero più grande della lista, cioè",maximum,".")
    elif k < minimum:
        print ("K è più piccolo di tutti i numeri della lista.")
    elif k == minimum:
        print ("K è uguale al numero più piccolo della lista, cioé",minimum,".")
    else:
        print ("K non è né più grande né più piccolo di nessun elemento della lista.")

    print ("Nella lista ci sono",pari,"numeri pari e",dispari,"numeri dispari.")
    print (" ")


    
