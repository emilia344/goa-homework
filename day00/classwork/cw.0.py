from turtle import *

speed(30)
#we want to paint a house

#step 1: draw a square
width(7)
color("purple")
forward(200)
left(90)       

forward(200)
left(90)


forward(200)
left(90)       

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("blue")
left(90)
forward(120)   #heigt of the door
right(90)
forward(60)
right(90)        
forward(120)        
        
penup()
goto(200, 200)
pendown()

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


print("emilia")

print("9")

print("sushi")








exitonclick()