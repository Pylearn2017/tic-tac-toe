import turtle

window = turtle.Screen()
button_single = turtle.Turtle()
button_multiplayer = turtle.Turtle()
clicker = turtle.Turtle()

def start_game():
	button_single.clear()
	button_multiplayer.clear()
	show_button()

def show_button():
	button_single.showturtle()
	button_single.shape('square')
	button_single.shapesize(2,8)
	button_single.setx(-200)
	button_multiplayer.showturtle()
	button_multiplayer.shape('square')
	button_multiplayer.shapesize(2,8)
	button_multiplayer.setx(200)

def iscollision(obj1, obj2, w1, w2, h1, h2):
	if obj1.xcor() + w1 > obj2.xcor() - w2 and obj1.xcor() - w1 < obj2.xcor() + w2:
		if obj1.ycor() + h1 > obj2.ycor() - h2 and obj1.ycor() - h1 < obj2.ycor() + h2:
			return True
	return False

def click(x,y):
	clicker.setposition(x,y)
	if iscollision(clicker, button_single, 20, 60, 10, 10):
		window.bgcolor('blue')
	elif iscollision(clicker, button_multiplayer, 20, 60, 10, 10):
		window.bgcolor('red')	

start_game()
window.onclick(click)
turtle.done()