import cImage as image
import turtle

def pixel_grigi(immagine,lista):
    img = image.Image(immagine)
    for riga in range(img.getHeight()):
        for colonna in range(img.getWidth()):
            p = img.getPixel(colonna,riga)
            media=(p.getRed()+p.getGreen()+p.getBlue())//3
            lista[media]+=1
    

def draw_bar_first(move,firstvalore,r,g,b):
    move.color(r,g,b)
    move.hideturtle()
    move.penup()
    move.goto(-484,-310)
    move.pensize(1)
    move.pencolor(0,0,0)
    move.pendown()
    move.begin_fill()
    move.forward(20)
    move.left(90)
    move.forward(firstvalore)
    move.right(90)
    move.forward(3.6)
    move.right(90)
    move.forward(firstvalore)
    move.end_fill()
    move.left(180)


def draw_bar(move,posizione,valore,r,g,b):
    move.color(r,g,b)
    move.pencolor(0,0,0)
    move.pensize(1)
    move.setpos(posizione)
    move.begin_fill()
    move.forward(valore)
    move.right(90)
    move.forward(3.6)
    move.right(90)
    move.forward(valore)
    move.end_fill()
    move.right(180)

def divisione(move):
    move.hideturtle()
    move.penup()
    move.goto(-225,-309)
    move.left(90)
    move.pensize(4)
    move.pencolor(255,0,0)
    move.pendown()
    move.forward(643)
    move.penup()
    move.goto(225,-309)
    move.pendown()
    move.forward(643)

def case(move):
    move.hideturtle()
    move.penup()
    move.goto(-484,-310)
    move.left(90)
    move.pensize(3)
    move.pendown()
    move.forward(645)
    move.right(90)
    move.forward(965)
    move.right(90)
    move.forward(645)
    move.penup()
    move.forward(30)
    move.right(90)
    move.penup()
    move.forward(115)
    move.pendown()
    move.write("LUCI",align="center",font=("ComicSans",11,"bold"))
    move.penup()
    move.forward(360)
    move.pendown()
    move.write("MEZZI TONI",align="center",font=("ComicSans",11,"bold"))
    move.penup()
    move.forward(355)
    move.pendown()
    move.write("OMBRE",align="center",font=("ComicSans",11,"bold"))

def taglio(img,win):
    new_pixel=image.Pixel(255,255,255)
    click_1=win.getMouse()
    click_2=win.getMouse()
    click_1_x=click_1[0]
    click_1_y=click_1[1]
    click_2_x=click_2[0]
    click_2_y=click_2[1]
    for col in range(img.getHeight()):
        for row in range(img.getWidth()):

            if click_1_x  <= click_2_x and click_1_y <= click_2_y:
                if not (click_1_x < row < click_2_x and click_1_y < col < click_2_y):   
                    img.setPixel(row,col,new_pixel)

            if click_1_x >= click_2_x and click_1_y <= click_2_y:
                if not (click_2_x < row < click_1_x and click_1_y < col < click_2_y):
                    img.setPixel(row,col,new_pixel)

            if click_1_x >= click_2_x and click_1_y >= click_2_y:
                if not (click_2_x < row < click_1_x and click_2_y < col < click_1_y):
                   img.setPixel(row,col,new_pixel)

            if click_1_x <= click_2_x and click_1_y >= click_2_y:
                if not (click_1_x < row < click_2_x and click_2_y < col < click_1_y):
                  img.setPixel(row,col,new_pixel)  
    img.draw(win)

def main_taglio(cont,win,immagine):
    immagine.draw(win)
    taglio(immagine,win)

    salva=input("L'immagine è stata ritagliata con successo! Salvare? [S/N] ")
    while not (salva == "n" or salva== "N" or salva == "s" or salva == "S"):
                salva=input("Scelta non consentita. Inserisci [S] o [N]: ")

    if salva == "s" or salva== "S":
        try:
            i=0
            while True:
                open("Nuova_immagine_"+str(i)+"_cutted.gif")
                i+=1
        except:
            immagine.save("Nuova_immagine_"+str(i)+"_cutted.gif")
            print("L'immagine è stata salvata con successo come: Nuova_immagine_"+str(i)+"_cutted.gif")
            print(" ")
        
    cont+=1
    return (cont)

def main_istogramma(cont1):
    lista_cont_grigi=[0]*256
    pixel_grigi(scrivi,lista_cont_grigi)

    mass=max(lista_cont_grigi)

    if mass > 625:
        scala=mass/620
        for i in range(len(lista_cont_grigi)):
            lista_cont_grigi[i]=lista_cont_grigi[i]/scala
    
    
    turtle.setup(1000,700)
    wn=turtle.Screen()
    wn.colormode(255)

    peppe=turtle.Turtle()
    peppe.speed(0)
    
    draw_bar_first(peppe,lista_cont_grigi[0],0,0,0)
    pos3=peppe.pos()
    for i in range(len(lista_cont_grigi)):
        draw_bar(peppe,pos3,lista_cont_grigi[i],i,i,i)
        pos3=peppe.pos()
    peppe.pensize(3)
    peppe.right(90)        
    peppe.forward(20)
    peppe.backward(965)

    rocco=turtle.Turtle()
    rocco.speed(0)
    divisione (rocco)

    giusi=turtle.Turtle()
    giusi.speed(0)
    case(giusi)
    print(" ")
    cont1+=1
    return cont1
    
    
print(" ")
print ("                        CUTTER E ISTOGRAMMA DI IMMAGINE")
print(" ")
cont=0
cont1=0
while True:
    try:
        if cont > 0 or cont1 > 0:
            verifica=input("Vorresti caricare una nuova immagine? [S/N] ")
            while not (verifica == "n" or verifica == "N" or verifica == "s" or verifica == "S"):
                verifica=input("Scelta non consentita. Inserisci [S] o [N]: ")

            if verifica=="n" or verifica=="N":
                print(" 1. Termina")
                if cont1 > cont:
                    print(" 2. Ritaglio immagine da doppio click")
                else:
                    print(" 2. Rappresentazione istogramma di luminosità dell'immagine")
                verifica2=input("Scelta ---> ")
                while not (verifica2 == "1" or verifica2 == "2"):
                    verifica2=input("Scelta non consentita. Inserisci [1] o [2]: ")

                if verifica2=="1":
                    print("Vabbene, ciao!")
                    if cont1 > 0:
                        turtle.bye()
                    if cont > 0:
                        win._close()
                    break

                elif verifica2=="2":
                    if cont1 >= cont:
                        turtle.bye()
                        win = image.ImageWin(height=immagine.getHeight(),width=immagine.getWidth())
                        cont=main_taglio(cont,win,immagine)
                        break

                    elif cont >= cont1:
                        win._close()
                        cont1=main_istogramma(cont1)
                        break
                            
        scrivi=input("Inserisci il nome di una immagine (es. immagine.estensione): ")
        immagine = image.Image(scrivi)
        print(" ")
        print("Definisci le azioni da eseguire:")
        print(" 1. Rappresentazione istogramma di luminosità dell'immagine")
        print(" 2. Ritaglio immagine da doppio click")
        print (" ")
        scelta=input("Scelta ---> ")
        if scelta == "2":
            win = image.ImageWin(height=immagine.getHeight(),width=immagine.getWidth())
            cont=main_taglio(cont,win,immagine)
        elif scelta == "1":
            cont1=main_istogramma(cont1)
       
    except:
        print("I caratteri inseriti non sono validi.")
        print(" ")
