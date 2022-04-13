import turtle

def main_deagonal_winner_line(obj1, obj2, obj3):
    print('Победитель ',obj1.value)
    drawer.width(9)
    drawer.color('red')
    drawer.hideturtle()
    drawer.setposition(obj1.pos())
    drawer.pendown()
    drawer.setposition(obj1.xcor()-900, obj1.ycor()+900)
    drawer.setposition(obj1.xcor()+900, obj1.ycor()-900)
    drawer.penup()
    drawer.setposition(obj2.pos())
    drawer.pendown()
    drawer.setposition(obj2.xcor()-900, obj2.ycor()+900)
    drawer.setposition(obj2.xcor()+900, obj2.ycor()-900)
    drawer.penup()
    drawer.setposition(obj3.pos())
    drawer.pendown()
    drawer.setposition(obj3.xcor()-900, obj3.ycor()+900)
    drawer.setposition(obj3.xcor()+900, obj3.ycor()-900)
    drawer.penup()

def horizont_winner_line(obj1, obj2, obj3):
    print('Победитель ',obj1.value)
    drawer.width(9)
    drawer.color('red')
    drawer.hideturtle()
    drawer.setposition(obj1.pos())
    drawer.pendown()
    drawer.setx(900)
    drawer.setx(-900)
    drawer.penup()
    drawer.setposition(obj2.pos())
    drawer.pendown()
    drawer.setx(900)
    drawer.setx(-900)
    drawer.penup()
    drawer.setposition(obj3.pos())
    drawer.pendown()
    drawer.setx(900)
    drawer.setx(-900)
    drawer.penup()
    
def vertical_winner_line(obj1, obj2, obj3):
    print('Победитель ',obj1.value)
    drawer.width(9)
    drawer.color('red')
    drawer.hideturtle()
    drawer.setposition(obj1.pos())
    drawer.pendown()
    drawer.sety(900)
    drawer.sety(-900)
    drawer.penup()
    drawer.setposition(obj2.pos())
    drawer.pendown()
    drawer.sety(900)
    drawer.sety(-900)
    drawer.penup()
    drawer.setposition(obj3.pos())
    drawer.pendown()
    drawer.sety(900)
    drawer.sety(-900)
    drawer.penup()
    
def is_solved():
    board = buttons_game
    print(board[0][0].value, board[0][1].value, board[0][2].value)
    print(board[1][0].value, board[1][1].value, board[1][2].value)
    print(board[2][0].value, board[2][1].value, board[2][2].value)
    for i in range(3):
        for j in range(3):
            if board[0][j].value == board[1][j].value == board[2][j].value:
                if board[0][j].value != 0:
                    vertical_winner_line(board[0][j], board[1][j], board[2][j])
                    return
            if board[i][0].value == board[i][1].value == board[i][2].value:
                if board[i][0].value != 0:
                    horizont_winner_line(board[i][0], board[i][1], board[i][2])
                    return
            if board[0][0].value == board[1][1].value == board[2][2].value:
                if board[1][1].value != 0:
                    main_deagonal_winner_line(board[0][0], board[1][1], board[2][2])
                    return
    return 


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
				is_solved()
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
		b.value = 0
		row_buttons.append(b)
	buttons_game.append(row_buttons) 

start_game()
window.onclick(click)
turtle.done()