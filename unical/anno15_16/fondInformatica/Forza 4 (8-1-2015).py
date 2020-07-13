#Forza 4
import random
"""1. Serve una griglia n x m (6 x 7)
2. colori:
    o = casella vuota
    1 = pedine gioc 1
    2 = pedine gioc 2

3. le pedine occupano smpre la prima pos in basso
4. quando c'è vittoria, devono esserci 1 o 2 continui per diagonale, orizzontale, verticale
"""

def griglia():
    colonne=int(input("Quante colonne deve avere la griglia? "))
    righe=int(input("Quanate righe deve avere la griglia? "))
    griglia=[]
    for i in range(righe):
        griglia.append([0]*colonne)
    return (griglia,colonne)


def stampa_matrice(griglia):
    for i in griglia:
        print(i,end='\n')


def giocatore():
    giocarore1=1
    giocatore2=2
    return random.randint(1,2)
    

def aggiungi_pedina(griglia,colonna,giocatore):
    col=random.randrange(0,colonna-1)
    for i in range(len(griglia)-1,-1,-1):
        if griglia[i][col] == 0:
            griglia[i][col]=giocatore
            break
        
def inizializza_griglia(griglia,giocatore,colonne):
    """predned in ingresso tre numeri interi non negativi n,m,t
        -se t è 0 (0 turni), restituisco matrice vuota
        - se t > 0, stablisce chi gioca per prima va a simulare l'esecuzione delle mosse
        (si usa aggiungii pedina)
        ci mostra il gioco al turno 7"""

    t=int(input("Quale turno vuoi osservare? "))
    if t*2 == 0:
        return griglia
    cont=1
    player=giocatore
    while cont <= t*2:
        if player==3:
            player=1
        aggiungi_pedina(griglia,colonne,player)
        cont+=1
        player+=1
    stampa_matrice(griglia)
    if verifica_vittoria(griglia,giocatore,t)==1:
        print("Ha vinto il giocatore 1 !")
    elif verifica_vittoria(griglia,giocatore,t)==2:
        print("Ha vinto il giocatore 2!")
    else:
        print("Gioco ancora in parità, mi spiace...")
        

def verifica_vittoria(griglia,giocatore,t):
    """"prende in ingresso la griglia e il giocatore e restituisce un booleano, e va a vadere se il giocare ha vinto (true o false)"""
    if t >= 7:
        #verifica vittoria diagonale
        for i in range(len(griglia)):
            for j in range(len(griglia[0])):
                if i>=3 and j >=3:
                    if griglia[i][j]==griglia[i-1][j-1]==griglia[i-2][j-2]==griglia[i-3][j-3]==giocatore:
                        return (giocatore)
                if (len(griglia)-i)>=4 and j >=3:
                    if griglia[i][j]==griglia[i+1][j-1]==griglia[i+2][j-2]==griglia[i+3][j-3]==giocatore:
                        return (giocatore)
                if (len(griglia)-i)>=4 and (len(griglia[i])-j)>=4:
                    if griglia[i][j]==griglia[i+1][j+1]==griglia[i+2][j+2]==griglia[i+3][j+3]==giocatore:
                        return (giocatore)
                if i>= 3 and (len(griglia[0])-j)>= 4:
                    if griglia[i][j]==griglia[i-1][j+1]==griglia[i-2][j+2]==griglia[i-3][j+3]==giocatore:
                        return (giocatore)
        #verifica vittoria verticale
                    if (len(griglia)-i)>3:
                        if griglia[i][j]==griglia[i+1][j]==griglia[i+2][j]==griglia[i+3][j]==giocatore:
                            return (giocatore)
        #verifica vittoria orizzontale
                if (len(griglia[0])-j)>3:
                    if griglia[i][j]==griglia[i][j+1]==griglia[i][j+2]==griglia[i][j+3]==giocatore:
                        return (giocatore)


def main():
    a=griglia()
    grigliata=a[0]
    giocatoe=giocatore()
    inizializza_griglia(grigliata,giocatoe,a[1])


while True:
    main()

