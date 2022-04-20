import os
import turtle
import random


def other_deagonal_winner_line(obj1, obj2, obj3):
    print('Победитель ',obj1.value)
    drawer.width(9)
    drawer.color('red')
    drawer.hideturtle()
    drawer.setposition(obj1.pos())
    drawer.pendown()
    drawer.setposition(obj1.xcor()-900, obj1.ycor()-900)
    drawer.setposition(obj1.xcor()+900, obj1.ycor()+900)
    drawer.penup()
    drawer.setposition(obj2.pos())
    drawer.pendown()
    drawer.setposition(obj2.xcor()-900, obj2.ycor()-900)
    drawer.setposition(obj2.xcor()+900, obj2.ycor()+900)
    drawer.penup()
    drawer.setposition(obj3.pos())
    drawer.pendown()
    drawer.setposition(obj3.xcor()-900, obj3.ycor()-900)
    drawer.setposition(obj3.xcor()+900, obj3.ycor()+900)
    drawer.penup()

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
    
def is_drow():
    values = 0
    for row in buttons_game:
        for item in row:
            if item.value:
                values += 1
    if values == 9:
        return True
    else: 
        return False

def is_solved():
    board = buttons_game
    for i in range(3):
        for j in range(3):
            if board[0][j].value == board[1][j].value == board[2][j].value:
                if board[0][j].value != 0:
                    vertical_winner_line(board[0][j], board[1][j], board[2][j])
                    window.game = False
                    return True
            if board[i][0].value == board[i][1].value == board[i][2].value:
                if board[i][0].value != 0:
                    horizont_winner_line(board[i][0], board[i][1], board[i][2])
                    window.game = False
                    return True
            if board[0][0].value == board[1][1].value == board[2][2].value:
                if board[1][1].value != 0:
                    main_deagonal_winner_line(board[0][0], board[1][1], board[2][2])
                    window.game = False
                    return True
            if board[2][0].value == board[1][1].value == board[0][2].value:
                if board[1][1].value != 0:
                    other_deagonal_winner_line(board[2][0], board[1][1], board[0][2])
                    window.game = False
                    return True
    if is_drow():
        window.game = False
        return True


def create_object():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()
    t.setposition(9999, 9999)
    return t

def reser_drawer():
    drawer.color('black')

def start_game():
    window.game = True
    for row in buttons_game:
        for button in row:
            button.value = 0
    clear_window()
    reser_drawer()
    show_button()
    window.update()

def show_button():
    button_single.showturtle()
    button_single.setposition(-260,-50)
    button_single.write('With frends', font=('Arial', 18, 'normal'))
    button_single.shape('square')
    button_single.shapesize(2,8)
    button_single.setposition(-200,0)

    button_multiplayer.showturtle()
    button_multiplayer.setposition(125,-50)
    button_multiplayer.write('With computer', font=('Arial', 18, 'normal'))
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
            button.in_field = True
            x += 220
        y -= 220
        x = -220

def menu():
    if iscollision(clicker, button_single, 20, 60, 10, 10):
        window.game_mode = 'doubles'
        clear_window()
        draw_playing_field()
        window.update()

    elif iscollision(clicker, button_multiplayer, 20, 60, 10, 10):
        window.game_mode = 'singleplayer'
        clear_window()
        draw_playing_field()
        window.update()

def choice_shape(button):
    shape = path + '\\skins\\standart\\'
    if clicker.clicks%2 == 0:
        shape += 'x\\x' + str(random.randint(1,3)) + '.gif'
        button.shape(shape)
        return 'x'
    else:   
        shape += 'o\\o' + str(random.randint(1,3)) + '.gif'
        button.shape(shape)
        return 'o'
    

def computer_choice():
    for button_row in buttons_game:
        for button in button_row:
            if button.in_field:
                if random.choice([True, False]):
                    clicker.clicks += 1
                    button.stamp()
                    shape = choice_shape(button)
                    button.stamp()
                    button.value = shape
                    is_solved()
                    button.in_field = False
                    button.setposition(9999, 9999)
                    return
    else: 
        if not is_drow():
            computer_choice()


def click(x,y):
    clicker.setposition(x,y)
    menu()
    if window.game:
        if window.game_mode == 'doubles':
            for button_row in buttons_game:
                for button in button_row:
                    if iscollision(clicker, button, 90, 10, 90, 10):
                        clicker.clicks += 1
                        button.stamp()
                        shape = choice_shape(button)
                        button.stamp()
                        button.value = shape
                        is_solved()
                        button.in_field = False
                        button.setposition(9999, 9999)
                        return
        elif window.game_mode == 'singleplayer':
            for button_row in buttons_game:
                for button in button_row:
                    if iscollision(clicker, button, 90, 10, 90, 10):
                        clicker.clicks += 1
                        button.stamp()
                        shape = choice_shape(button)
                        button.stamp()
                        button.value = shape
                        if not is_solved():
                            button.in_field = False
                            button.setposition(9999, 9999)
                            computer_choice()
                            return


    else:
        clear_window()
        drawer.setposition(-200, 100)
        drawer.write('Press <Space>', font=('Arial', 48, 'normal'))
    
    

window = turtle.Screen()
window.tracer(0)
window.game = True
window.game_mode = ''
path = os.path.abspath(os.getcwd())
print(path)
# C:\Users\1\Documents\Python Scripts\Aleksander L\tic-tac-toe
# C:\Users\1\Documents\Python Scripts\Aleksander L\tic-tac-toe\skins\standart\x
window.register_shape(path + '\\skins\\standart\\x\\x1.gif')
window.register_shape(path + '\\skins\\standart\\o\\o1.gif')
window.register_shape(path + '\\skins\\standart\\x\\x2.gif')
window.register_shape(path + '\\skins\\standart\\o\\o2.gif')
window.register_shape(path + '\\skins\\standart\\x\\x3.gif')
window.register_shape(path + '\\skins\\standart\\o\\o3.gif')
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
window.listen()
window.onkeypress(start_game, 'space')
window.onclick(click)
turtle.done()
