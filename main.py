import turtle
import pandas
import scoreboard

screen = turtle.Screen()
screen.title("Estados Brasileiros Quiz by Yalmeida")


image = "brasil_por_regiões.gif"
win = "win.gif"
screen.addshape(image)
turtle.shape(image)
turtle_writer = turtle.Turtle()
turtle_writer.color("black")
turtle_writer.ht()
turtle_writer.penup()
score = scoreboard.Scoreboard()
####################################
# def get_mouse_click(x, y):
#     """ Returns x, y coordinates of click on  screen."""
#     print(x, y)
# turtle.onscreenclick(get_mouse_click)
####################################
data = pandas.read_csv("estados-brasileiros.csv")
estados_list = data.Estados.to_list()
estados_list__total = len(estados_list)
correct_list = []


def ask():
    while len(correct_list) < 27:
        answer = screen.textinput(title=f"{score.points}/27", prompt="Qual o próximo estado?")
        if answer != "":
            answer_title = answer.title()
            user_answer = data[data.Estados == answer_title]
            if answer_title == "Exit":
                break
            if answer_title in estados_list:
                turtle_writer.goto(int(user_answer.x), int(user_answer.y))
                turtle_writer.color("blue")
                turtle_writer.write(answer_title)
                correct_list.append(answer_title)
                score.update_score()
        else:

            ask()
    else:
        screen.clear()
        screen.bgcolor("black")
        screen.addshape(win)
        turtle.shape(win)


ask()

missing_estates = list(set(estados_list).difference(correct_list))
for item in missing_estates:
    turtle_writer.goto(int(data[data.Estados == item].x), int(data[data.Estados == item].y))
    turtle_writer.color("red")
    turtle_writer.write(item)

turtle.mainloop()

