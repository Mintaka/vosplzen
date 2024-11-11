import turtle

def vyresli(x, y, n):
    turtle.setup(500, 500)
    screen = turtle.Screen()
    screen.setworldcoordinates(-250, -250, 250, 250)
    
    t = turtle.Turtle()
    t.color("blue")
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # P
    t.circle(20,180)
    t.left(90)
    t.forward(65) 
    
    t.penup()
    t.goto(x + 50, y -10)
    t.setheading(0)  
    t.pendown()
    
    # T 
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.backward(50)
    
    # n-uhelnik
    t.color("red")
    t.penup()
    t.goto(x + 100, y + 40)
    t.pendown()
    
   
    side_length = 40  
    angle = 360 / n   
    
    for _ in range(n):
        t.forward(side_length)
        t.right(angle)
       
    t.hideturtle()
    turtle.done()

vyresli(-50, 50, 5)
