def sottosoglia (v,x):
    for i in range (len(v)):
        if v[i]>x:
            return False
    return True

temp=int(input("Inserisci valore di temperatura da analizzare : "))
array= []

lenarray=int(input("Quanti valori vuoi considerare?: "))
for i in range(lenarray):
    temparray=int(input("Inserisci temperatura: "))
    array.append(temparray)

risultato= sottosoglia(array,temp)
if risultato:
    print ("La misurazione",temp,"° è maggiore di tutti i valori",array)
else:
    print ("Mi dispiace,ma",temp,"° non è la temperatura più bassa.")
