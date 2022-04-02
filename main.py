import turtle

def create_object():
	t = turtle.Turtle()
	t.speed(0)
	t.penup()
	t.hideturtle()
	t.setposition(9999, 9999)
	return t

def start_game():
	button_single.clear()
	button_multiplayer.clear()
	show_button()

def show_button():
	button_single.showturtle()
	button_single.shape('square')
	button_single.shapesize(2,8)
	button_single.setposition(-200,0)
	button_multiplayer.showturtle()
	button_multiplayer.shape('square')
	button_multiplayer.shapesize(2,8)
	button_multiplayer.setposition(200,0)

def iscollision(obj1, obj2, w1, w2, h1, h2):
	if obj1.xcor() + w1 > obj2.xcor() - w2 and obj1.xcor() - w1 < obj2.xcor() + w2:
		if obj1.ycor() + h1 > obj2.ycor() - h2 and obj1.ycor() - h1 < obj2.ycor() + h2:
			return True
	return False

def clear_window():
	for t in window.turtles():
		t.clear()
		t.hideturtle()
		t.setposition(9999, 9999)

def draw_playing_field():
	drawer.setposition(0,0)
	drawer.showturtle()
	drawer.shape('square')
	drawer.shapesize(30)
	drawer.stamp()
	drawer.setposition(9999,9999)
	x = -220
	y = 220
	for button_row in buttons_game:
		for button in button_row:
			button.showturtle()
			button.color('white')
			button.shape('square')
			button.shapesize(10)
			button.setposition(x, y)
			x += 220
		y -= 220
		x = -220

def menu():
	if iscollision(clicker, button_single, 20, 60, 10, 10):
		clear_window()
		draw_playing_field()
	elif iscollision(clicker, button_multiplayer, 20, 60, 10, 10):
		clear_window()
		draw_playing_field()

def choice_shape():
	if clicker.clicks%2 == 0:
		shape = 'x.gif'
	else:	
		shape = 'o.gif'
	return shape

def click(x,y):
	clicker.setposition(x,y)
	menu()
	for button_row in buttons_game:
		for button in button_row:
			if iscollision(clicker, button, 90, 10, 90, 10):
				clicker.clicks += 1
				shape = choice_shape()
				button.stamp()
				button.value = shape
				button.shape(button.value)
				button.stamp()
				button.setposition(9999, 9999)
	

window = turtle.Screen()
window.register_shape('x.gif')
window.register_shape('o.gif')
button_single = create_object()
button_multiplayer = create_object()
clicker = create_object()
clicker.clicks = 0
drawer = create_object()
buttons_game = []
for row in range(3):
	row_buttons = []
	for col in range(3):
		b = create_object()
		b.value = ''
		row_buttons.append(b)
	buttons_game.append(row_buttons) 

start_game()
window.onclick(click)
turtle.done()