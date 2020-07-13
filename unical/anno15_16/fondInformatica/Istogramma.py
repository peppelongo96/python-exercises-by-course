import turtle
import random

def draw_bar(move,alt,larg,conta,coeff,specifica,colore):
    move.fillcolor(colore)
    move.penup()
    move.goto(-650,-300)
    move.pendown()
    move.forward((larg*conta)+(larg/2))
    move.penup()
    move.sety(-321)
    move.pendown()
    move.write(specifica,align="center",font=("ComicSans",9,"normal"))
    move.penup()
    move.sety(-300)
    move.pendown()
    move.forward(larg/2)
    move.left(180)
    move.forward(larg)
    move.right(90)
    move.begin_fill()
    move.forward(alt)
    move.right(90)
    move.forward(larg/2)
    move.write(alt*coeff,align="center",font=("Arial",10,"bold"))
    move.forward(larg/2)
    move.right(90)
    move.forward(alt)
    move.left(90)
    move.end_fill()
   
def case_bar_alt(move,alt,coeff):
    move.penup()
    move.goto(-650,-300)
    move.pendown()
    move.left(90)
    move.forward(alt)
    move.right(90)
    move.forward(15)
    move.right(180)
    move.forward(15)
   
def case_bar_larg(move,larg):
    move.forward(larg)
    move.right(90)
    move.forward(10)
    move.left(180)
    move.forward(10)
    move.right(90)
        

def sottosoglia (v,x):
    for i in range (len(v)):
        if v[i]>x:
            return True
    return False

def main ():
    valorialt=[]
    valorialtscala=[]
    listaspec=[]
    tipologia=input("Cosa andrà a rappresentare l'istogramma? (scrivi < random > per casuale)  ")
    turtle.setup(1400,755)
    wn=turtle.Screen()
    wn.title("ISTOGRAMMA")
    if tipologia == "random" or tipologia == "random" or tipologia == "RANDOM":
        numvalori=random.randint(5,50)
        for i in range(numvalori):
            valore=random.randint(20,1000)
            valorialt.append(valore)
            specifica="Casuale"
            listaspec.append(specifica)
    else:
        numvalori=int(input("Inserisci numero valori: "))
        for i in range(numvalori):
            valore=int(input("Inserisci valore "+str(i+1)+": "))
            valorialt.append(valore)
            specifica=input("Descrizione per valore "+str(i+1)+"(lascia vuoto se non vuoi inserirla): ")
            listaspec.append(specifica)

    scala=sottosoglia(valorialt,550)
    scalaval=1
    conta=0
    larghezza=1300/(len(valorialt)+2)
    
    if scala==True:
        if tipologia == "random" or tipologia == "random" or tipologia == "RANDOM":
            scalaval=random.randint(2,5)
        else:
            print("Uno o più dati inseriti superano la scala reale consentita.")
            scalaval=int(input("Inserire coeffciente di proporzione: "))
        for i in valorialt :
            valorialtscala.append(i//scalaval)
            valorialt=valorialtscala

    print(" ")
    print("NOTA BENE: I valori più alti saranno designati da colonne rosse, i più bassi avranno colonne verdi.")
            
    for i in range(len(valorialt)):
        peppe=turtle.Turtle()
        peppe.shape("circle")
        peppe.shapesize(0.2)
        giusi=turtle.Turtle()
        giusi.shape("circle")
        giusi.shapesize(0.2)
        rocco=turtle.Turtle()
        rocco.shape("circle")
        rocco.shapesize(0.2)

        giusi.penup()
        giusi.goto(-650,-348)
        giusi.pendown()
        if tipologia == "random" or tipologia == "random" or tipologia == "RANDOM":
            tipologia="CASUALE"
        giusi.write(tipologia,font=("Arial", 13, "bold"))
        case_bar_alt(giusi,valorialt[i],scalaval)
        
        if conta >= 0:
            conta+=1

        if valorialt[i] == max(valorialt) and max(valorialt)!= min(valorialt)  :
            peppe.pensize(3)
            draw_bar(peppe,valorialt[i],larghezza,conta,scalaval,listaspec[i],"green")
        elif valorialt[i] == min(valorialt) and max(valorialt)!= min(valorialt) :
            peppe.pensize(2)
            draw_bar(peppe,valorialt[i],larghezza,conta,scalaval,listaspec[i],"red")
        elif max(valorialt)== min(valorialt):
            peppe.pensize(3)
            draw_bar(peppe,valorialt[i],larghezza,conta,scalaval,listaspec[i],"brown")
        else:
            draw_bar(peppe,valorialt[i],larghezza,conta,scalaval,listaspec[i],"white")

        if i+1==len(valorialt):
            peppe.forward(larghezza)
            peppe.penup()
            peppe.sety(-348)
            peppe.pendown()
            peppe.write(arg=("SCALA= 1 su ",scalaval),align="right",font=("ComicSans",11,"normal"))
            
            

    rocco.penup()
    rocco.goto(-650,-300)
    rocco.pendown()            
    rocco.left(90)
    rocco.forward(max(valorialt)+100)
    rocco.right(90)

    for i in range(len(valorialt)+1):
        case_bar_larg(rocco,larghezza)

    rocco.forward(larghezza)
    rocco.right(90)
    rocco.forward(max(valorialt)+100)
    rocco.right(90)
    rocco.pensize(3)
    rocco.forward((larghezza*numvalori)+(2*larghezza))
    
   
main()



