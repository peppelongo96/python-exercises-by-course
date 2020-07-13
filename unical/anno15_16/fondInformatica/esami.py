try:
    numeroesami=int(input("Salve, inserisca il numero di esami che ha sostenuto nell'arco di tutta la sua carriera post-diploma:"))
    while not numeroesami > 0 :
         print ("Mi pigghi po culu merda!?")
         numeroesami=int(input("Scrivili o chiudi. ---> "))
except ValueError:
         print ("Fai u pulitu!")
         numeroesami=int(input("Inserisci il numero cosu lordu i merda u.u :"))

esamemax=0
sommavoti=0
listavoti=[]
listaconta=[0]*13
for i in range (numeroesami):
    votoesame = int(input("Inserisci voto esame : "))
    while not 18 <= votoesame <= 30 :
        print ("Eh sentiamo...quale corso di laurea accetta",votoesame,"come voto?!")
        votoesame = int(input("Inseriscine uno corretto, veloce : "))
    listavoti.append (votoesame)
    listaconta[votoesame-18]+=1
    sommavoti+=votoesame
    if esamemax < votoesame:
        esamemax=votoesame

media=sommavoti/numeroesami
print("listavoti",listavoti)
print("Hai una media di voti intorbo a",media)
print ("Il miglior voto preso fin'ora è",esamemax)

contamax=0
listamoda=[]
for i in listaconta:
    if contamax <= i:
       contamax=i
for i in range(len(listaconta)):
    if contamax==listaconta[i]:
        moda=i+18
        listamoda.append(moda)

if len(listamoda)> 1:
    print("I voti più frequenti sono",listamoda,"che si ripetono ben",contamax,"volte")
    print("Il voto più alto e più frequente è",moda)
        
else:        
    print("Il voto più frequente é",listamoda,)
    print("Esso si ripete ben",contamax,"volte.")
