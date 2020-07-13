import cImage as image
import random

def spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna):
    new_pixel=image.Pixel(255,255,255)
    for col in range(colonna):
        for row in range(riga):
            if (lista_punti[i][0][0] <= row <= lista_punti[i][1][0] and lista_punti[i][0][1] <= col <= lista_punti[i][1][1]):
                p = immagine.getPixel(row,col)
                if ris==1:
                    #spostamento pixel casella in avanti
                    immagine.setPixel(row,col-col_def,p)
                if ris==2:
                    #spostamento pixel casella indietro
                    immagine.setPixel(row,col+col_def,p)
                if ris==3:
                    #spostamento pixel casella giù
                    immagine.setPixel(row+riga_def,col,p)
                if ris==4:
                    #spostamento pixel casella su
                    immagine.setPixel(row-riga_def,col,p)
                immagine.setPixel(row,col,new_pixel)

     #settaggio spostamenti in liste               
    if ris==1:
        lista_punti[i-4][2]=False
        (lista_verifica[i],lista_verifica[i-4])=(lista_verifica[i-4],lista_verifica[i])
    elif ris==2:
        lista_punti[i+4][2]=False
        (lista_verifica[i],lista_verifica[i+4])=(lista_verifica[i+4],lista_verifica[i])
    elif ris==3:
        lista_punti[i+1][2]=False
        (lista_verifica[i],lista_verifica[i+1])=(lista_verifica[i+1],lista_verifica[i])
    else:
        lista_punti[i-1][2]=False
        (lista_verifica[i],lista_verifica[i-1])=(lista_verifica[i-1],lista_verifica[i])
    lista_punti[i][2]=True

    return lista_verifica

def click_gioco(win,lista_punti,immagine,riga_def,col_def,lista_verifica,imm,num_click,liv,riga,colonna):
    click=win.getMouse()
    click_x=click[0]
    click_y=click[1]
    i=0
    tag=False
    try:
        #ricerca casella del click corrispondente
        while not ((lista_punti[i][0][0]<click_x<lista_punti[i][1][0] and lista_punti[i][0][1]<click_y<lista_punti[i][1][1]) and lista_punti[i][2]==False):
            i+=1

        if i>3:
            ris=1
            if lista_punti[i-4][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True
            elif i>7 and lista_punti[i-8][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i-4,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True
            elif i>11 and lista_punti[i-12][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i-8,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i-4,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True

        if i<12:
            ris=2
            if lista_punti[i+4][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True
            elif i<8 and lista_punti[i+8][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i+4,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True
            elif i<4 and lista_punti[i+12][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i+8,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i+4,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True

        if i!=3 and i!=7 and i!=11 and i!=15:
            ris=3
            if lista_punti[i+1][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True
            elif i!=2 and i!=6 and i!=10 and i!=14 and lista_punti[i+2][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i+1,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True
            elif (i==0 or i==4 or i==8 or i==12) and lista_punti[i+3][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i+2,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i+1,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True

        if not i%4==0:
            ris=4
            if lista_punti[i-1][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True
            elif i!=1 and i!=5 and i!=9 and i!=13 and lista_punti[i-2][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i-1,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True
            elif (i==3 or i==7 or i==11 or i==15) and lista_punti[i-3][2]==True:
                lista_verifica=spostamento(immagine,lista_punti,ris,i-2,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i-1,riga_def,col_def,lista_verifica,riga,colonna)
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                num_click+=1
                tag=True

        if tag==False:
            raise
    except:
        print("Click errato.Riprova.")
        click_gioco(win,lista_punti,immagine,riga_def,col_def,lista_verifica,imm,num_click,liv,riga,colonna)
    
    if verifica_vittoria(lista_verifica,lista_punti):
        imm=image.Image(imm+str('.gif'))
        imm.draw(win)
        if num_click<=liv:
          print('')
          print("ECCEZIONALE! HAI VINTO IL GIOCO IN SOLI "+str(num_click)+" PASSI!")
          print("NON SBAGLI UN COLPO EH ;)")
        else:
            print('')
            print("COMPLIMENTI! HAI VINTO IN "+str(num_click)+" MOSSE!")
        print('(click sulla immagine per chiuderla)')
        win.exitonclick()
    else:
        click_gioco(win,lista_punti,immagine,riga_def,col_def,lista_verifica,imm,num_click,liv,riga,colonna)


def livello(k,lista_punti,immagine,riga_def,col_def,lista_verifica,win,riga,colonna):
    flag=False
    if k >= 16:
        flag=True
    cont=0
    if cont==0:
        m=0
    while cont < k:
        i=random.randrange(0,16)
        if i>3 and m!= 2 and lista_punti[i-4][2]==True:
                ris=1
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                cont+=1
                m=1
                if flag==True:
                    immagine.draw(win)
        if i<12 and m!=1 and cont < k and lista_punti[i+4][2]==True:
                ris=2
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                cont+=1
                m=2
                if flag==True:
                    immagine.draw(win)
        if i!=3 and i!=7 and i!=11 and i!=15 and m!= 4 and cont < k :
            if lista_punti[i+1][2]==True:
                ris=3
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                cont+=1
                m=3
                if flag==True:
                    immagine.draw(win)
        if not i%4==0 and m!=3 and cont < k and lista_punti[i-1][2]==True:
                ris=4
                lista_verifica=spostamento(immagine,lista_punti,ris,i,riga_def,col_def,lista_verifica,riga,colonna)
                cont+=1
                m=4
                if flag==True:
                    immagine.draw(win)
    
    immagine.draw(win)
    return lista_verifica
        

def verifica_vittoria(lista_verifica,lista_punti):
    for h in range(len(lista_punti)):
        if (lista_punti[h]!= lista_verifica[h]):
            return False
    return True
    

def prepara_pixel(immagine):
    new_pixel=image.Pixel(255,255,255)
    riga=immagine.getWidth()
    colonna=immagine.getHeight()
    while riga%4!=0:
        riga-=1
    while colonna%4!=0:
        colonna-=1
    riga_def=(riga//4)-1
    colonna_def=(colonna//4)-1
    win = image.ImageWin(height=colonna-1,width=riga-1)
    immagine.draw(win)
    lista_pos=[]
    lista_punti=[]
    lista_verifica=[]
    for col in range(colonna):
        for row in range(riga):
            flag=0
            if row==0 or row==riga_def or row==(riga_def*2) or row==(riga_def*3) or row==(riga_def*4) : 
                immagine.setPixel(row,col,new_pixel)
                flag+=1
            if col == 0 or col==colonna_def or col==(colonna_def*2) or col==(colonna_def*3) or col==(colonna_def*4) :  
                immagine.setPixel(row,col,new_pixel)
                flag+=1
            if flag==2:
                lista_pos.append((row,col))

    for i in range(len(lista_pos)-6):
        if not ((lista_pos[i][0]==0 and lista_pos[i][1]==colonna_def*4) or lista_pos[i][0]==riga_def*4):
            lista_punti.append([(lista_pos[i][0]+1,lista_pos[i][1]+1),(lista_pos[i+6][0]-1,lista_pos[i+6][1]-1),False])
            lista_verifica.append([(lista_pos[i][0]+1,lista_pos[i][1]+1),(lista_pos[i+6][0]-1,lista_pos[i+6][1]-1),False])

    print (lista_punti)
        
    immagine.draw(win)
    i=random.randrange(0,16,1)
    new_pixel=image.Pixel(255,255,255)
    for col in range(colonna):
        for row in range(riga):
            if (lista_punti[i][0][0] < row < lista_punti[i][1][0] and lista_punti[i][0][1] < col < lista_punti[i][1][1]):
                immagine.setPixel(row,col,new_pixel)
                lista_punti[i][2]=True
                lista_verifica[i][2]=True

    immagine.draw(win)
    return [immagine,lista_punti,colonna_def,riga_def,win,lista_verifica,riga,colonna]



def main():
    try:
        imm=input("Inserisci il nome dell'immagine con cui desideri giocare: ")
        immagine=image.Image(imm+str('.gif'))
    except:
        print("Caratteri errati. Verifica si tratti di una immagine .gif e che sia presente nella stessa directory dell'algoritmo.")
        print(' ')
        main()
    print(' ')
    print("Definisci livello di gioco:")
    print(" 1. Facile")
    print(" 2. Intermedio")
    print(" 3. Difficile")
    print(" 4. (livello avanzato random 20-30)")
    scelta=input("Scelta ---> ")
    while scelta != "1" and scelta != "2" and scelta != "3" and scelta!= "4":
        scelta=input("Il carattere inserito non corrisponde a nessuna delle proposte. Riprova: ")
    liv=0
    if scelta=="1":
        liv+=5
    elif scelta=="2":
        liv+=10
    elif scelta=="3":
        liv+=15
    else:
        liv+=random.randrange(20,31,1)
    
    lista_return=prepara_pixel(immagine)
    print(' ')
    print("Questa è l'immagine che ricomposta ti assicurerà la vittoria!")
    print('Potrai riuscirci anche con '+str(liv)+' mosse! Buona fortuna!')
    print(' ')
    print('Ora attendi il rimescolamento delle tessere...')
    vittoria=livello(liv,lista_return[1],lista_return[0],lista_return[3],lista_return[2],lista_return[5],lista_return[4],lista_return[6],lista_return[7])
    print(' ')
    print('VIA!!!')
    print('')
    num_click=0
    click_gioco(lista_return[4],lista_return[1],lista_return[0],lista_return[3],lista_return[2],vittoria,imm,num_click,liv,lista_return[6],lista_return[7])
    

print('')
print("                          GIOCO DEL 15 CON IMMAGINE")
print(" ")
main()
