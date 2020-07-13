def alternati(v):
    #True, se i pari e i dispari sono alternati; False, se ci sono più pari o più dispari consecutivi
    for i in range(1,len(v)):
        if v[i-1]%2==v[i]%2:
            return False
    return True

def costruisci_lista(v1,v2):
    #costruisce una lista che nelle posizioni pari contiene la sommatoria degli elementi del primo
    #vettore a partire da quella posizione, nelle posizioni dispari contiene la produttoria del secondo
    #vettore a partire da quella posizione. L'ultima posizione sarà sempre 0
    v3=[]
    for i in range(len(v1)):
        if i%2==0:
            v3.append(somma_celle(v1,i+1))
        else:
            if i==len(v1)-1:
                v3.append(0)
            else:
                v3.append(prodotto_celle(v2,i+1))
    return v3

def somma_celle(v,pos):
    #restituisce la somma degli elementi del vettore da una posizione data fino al'ultima
    somma=0
    for i in range(pos,len(v)):
        somma+=v[i]
    return somma

def prodotto_celle(v,pos):
    #restituisce il prodotto degli elementi del vettore da una posizione data fino al'ultima
    prodotto=1
    for i in range(pos,len(v)):
        prodotto*=v[i]
    return prodotto

def roll_up(v):
    #restituisce un vettore con lunghezza dimezzata, costruito con determinate caratteristiche
    v_fin=[]
    for i in range(len(v)//2):
        v_fin.append(v[2*i]+v[2*i+1])
    return v_fin

def texture(a,b):
    #verifica che la prima lista sia una concatenazione della seconda
    #if len(a)<len(b):
    #   return False
    for i in range(len(a)):
        if a[i]!=b[i%len(b)]:
            return False
    return True

#una lista si può creare anche con                  v=[0 for i in range(10)]    v=[[] for i in range(10)]

#a=['C','I','A','O']         b=[x.lower() for x in a] (una lista con caratteri minuscoli)
#                                   c=[x.upper() for x in b] (una lista con caratteri maiuscoli)

#a=['c','i','a','o']          a.count('c') (quanti di quell'elemento sono contenuti nella lsta)

#v.insert(a,b)      (inserisce nella posizione a dell'array l'elemento b)

#v.pop(a)   (elimina il contenuto dell'array nella posizione a)
