n = int(input("Inserisci la dimensione dell'array: ")) # n deve essere un numero intero maggiore di 0
# creo un array "v" di n celle contenenti inizialmente il valore 0
v=[0]*n

# leggo da input "n" numeri interi e li inserisco nelle varie celle dell'array v
for i in range(len(v)):
    v[i]=int(input("Inserisci l'elemento in posizione " + str(i) + ": "))

print(v)


''' questa parte del programma determina il numero intero più grande (massimo) e il numero intero più 
piccolo (minimo) tra tutti quelli contenuti nell'array v '''

massimo = v[0] 
indiceMassimo = 0

minimo = v[0]
indiceMinimo = 0

for i in range(1, len(v)):
    if v[i] > massimo:
        massimo = v[i]
        indiceMassimo = i
    elif v[i] < minimo:
        minimo = v[i]
        indiceMinimo = i

if massimo == minimo: # verifichiamo in un colpo solo se v contiene in tutte le celle lo stesso elemento
    print("L'array v contiene in tutte le sue celle lo stesso valore e cioè, " + v[0]) 
else:
    print("L'elemento più grande è", massimo, "e si trova in posizione", i)
    print("L'elemento più piccolo è", minimo, "e si trova in posizione", i)


''' questa parte del programma verifica se tutti gli elementi contenuti nell'array v sono minori uguale di un intero positivo k'''


verifica = True
k=int(input("Inserisci un numero intero positivo:> "))
for i in range(len(v)):
	if v[i] > k:
		verifica = False
		break

print(verifica)

# si poteva fare anche sfruttando il massimo 

if massimo > k:
	print(False)

