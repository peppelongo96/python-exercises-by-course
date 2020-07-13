import turtle
import cImage as image
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
    move.goto(-691,-430)
    move.pensize(1)
    move.pencolor(0,0,0)
    move.pendown()
    move.begin_fill()
    move.forward(20)
    move.left(90)
    move.forward(firstvalore)
    move.right(90)
    move.forward(5.3)
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
    move.forward(5.3)
    move.right(90)
    move.forward(valore)
    move.end_fill()
    move.right(180)

def divisione(move):
    move.hideturtle()
    move.penup()
    move.goto(-230.733333333,-430)
    move.left(90)
    move.pensize(4.5)
    move.pencolor(255,0,0)
    move.pendown()
    move.forward(920)
    move.penup()
    move.goto(254.733333333334,-430)
    move.pendown()
    move.forward(920)

def case(move):
    move.hideturtle()
    move.penup()
    move.goto(-691,-430)
    move.left(90)
    move.pensize(3)
    move.pendown()
    move.forward(920)
    move.right(90)
    move.forward(1402)
    move.right(90)
    move.forward(920)
    move.penup()
    move.forward(40)
    move.right(90)
    move.penup()
    move.forward(220)
    move.pendown()
    move.write("LUCI",align="center",font=("ComicSans",11,"bold"))
    move.penup()
    move.forward(475)
    move.pendown()
    move.write("MEZZI TONI",align="center",font=("ComicSans",11,"bold"))
    move.penup()
    move.forward(475)
    move.pendown()
    move.write("OMBRE",align="center",font=("ComicSans",11,"bold"))



def main():
    immagine=input("Una volta copiata l'immagine nella stessa directory dell'algoritmo, inserisci esattamende il nome della gif: ")
    lista_cont_grigi=[0]*256
    pixel_grigi(immagine,lista_cont_grigi)

    mass=max(lista_cont_grigi)

    if mass > 900:
        scala=mass/900
        for i in range(len(lista_cont_grigi)):
            lista_cont_grigi[i]=lista_cont_grigi[i]/scala
    
    
    turtle.setup(1500,1080)
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
    peppe.backward(1402)

    rocco=turtle.Turtle()
    rocco.speed(0)
    divisione (rocco)

    giusi=turtle.Turtle()
    giusi.speed(0)
    case(giusi)

    print(" ")
    main()


main()

    
