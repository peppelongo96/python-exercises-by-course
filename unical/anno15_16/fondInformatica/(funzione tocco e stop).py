import turtle

def main():
    wn=turtle.Screen()
    peppe=turtle.Turtle()
    peppe.left(100)
    g=turtle.Turtle()
    g.penup()
    g.goto(-50,80)
    g.pendown()
    g.forward(300)
    print(peppe.ycor(),g.ycor())
    while not int(peppe.ycor())-g.ycor() == 0:  
        print(int(peppe.ycor()),g.ycor())
        peppe.forward(1)
        

main()
