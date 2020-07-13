import turtle
import random
import time


def passo_falso(move):
    passo_falso=False
    if move.xcor()>650 or move.xcor() < -550:
        passo_falso=True
    if move.ycor()>300 or move.ycor()<-300:
        passo_falso=True
    return passo_falso
        

def movimento(move,random_gradi,random_mov):
    casuale=random.randint(0,1)
    if casuale==0:
        move.left(random_gradi)
    if casuale==1:
        move.right(random_gradi)
    move.penup()
    move.forward(random_mov)
    if passo_falso(move)==True:
        move.backward(random_mov)

def gen_colori(t,screen):
    screen.colormode(255)
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    ris=t.color(r, g, b)
    return ris
 
    
def main():
    numtart=int(input("Inserisci numero tartarughe: "))
    turtle.setup(1390,745)
    wn=turtle.Screen()
    lago=turtle.Turtle()
    lago.fillcolor("blue")
    lago.speed(5)
    lago.penup()
    lago.begin_fill()
    lago.goto(-700,-400)
    lago.pendown()
    lago.left(90)
    lago.forward(800)
    lago.right(90)
    lago.forward(100)
    lago.right(90)
    lago.forward(800)
    lago.right(90)
    lago.forward(100)
    lago.end_fill()
    
    
    lista_tart=[]

    for i in range(numtart):
        random_mov=random.randint(20,100)
        random_gradi=random.randint(0,180)
        random_pos_x=random.randint(-550,650)
        random_pos_y=random.randint(-300,300)
        turtle.hideturtle()
        peppe=turtle.Turtle()
        peppe.hideturtle()
        peppe.shape("turtle")
        gen_colori(peppe,wn)
        peppe.shapesize(3)
        peppe.hideturtle()
        peppe.speed(1000)
        peppe.penup()
        peppe.goto(random_pos_x,random_pos_y)
        peppe.showturtle()
        peppe.speed(1)
        peppe.pendown()
        movimento(peppe,random_gradi,random_mov)
        lista_tart.append(peppe)
        
        
    while True:
        for j in lista_tart:
            random_mov=random.randint(0,100)
            random_gradi=random.randint(0,360)
            random_pos_x=random.randint(-550,650)
            random_pos_y=random.randint(-300,300)
            tempo_att=time.time()
            cord_x=j.xcor()
            
            if cord_x==-550:
                j.right(180)
                j.forward(random.randint(80,200))
                if passo_falso(j)==True:
                    move.backward(random.randint(50,80))
                movimento(j,random_gradi,random_mov)
                if passo_falso(j)==True:
                    move.backward(random_mov)

            elif (int(tempo_att))%8==0: #qui viene simulata una qualsiasi tartarugha
                angolo=j.heading()       #del vettore diretta ad abbeverarsi a un ipotetico fiume (barra blu a sinistra)
                if angolo < 180:
                    angolo_new=180-angolo
                    j.penup()
                    j.left(angolo_new)
                    j.setx(-550)

                if angolo > 180:
                    angolo_new=angolo-180
                    j.penup()
                    j.right(angolo_new)
                    j.setx(-550)

                else:
                    j.penup()
                    j.setx(-550)

            else:
                movimento(j,random_gradi,random_mov)
                if passo_falso(j)==True:
                    move.backward(random_mov)

main()


                
                
