import turtle

# إعدادات الشاشة
wind = turtle.Screen()
wind.title("Ping X Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)

# دالة لعرض شاشة البداية
def show_start_screen():
    start_screen = turtle.Turtle()
    start_screen.hideturtle()
    start_screen.color("white")
    start_screen.penup()
    start_screen.goto(0, 100)
    start_screen.write("Press 'P' to Play with Friend or 'C' to Play with Computer", align="center", font=("Courier", 18, "normal"))

    wind.listen()
    wind.onkeypress(start_game_friend, "p")
    wind.onkeypress(start_game_computer, "c")

# دالة لبدء اللعب مع صديق
def start_game_friend():
    show_start_screen()
    play_game(False)

# دالة لبدء اللعب مع الكمبيوتر
def start_game_computer():
    show_start_screen()
    play_game(True)

# دالة للعبة
def play_game(is_computer):
    # إعداد اللعبة
    madrab1 = turtle.Turtle()
    madrab1.speed(1)
    madrab1.shape("square")
    madrab1.shapesize(stretch_len=1, stretch_wid=5)
    madrab1.color("blue")
    madrab1.penup()
    madrab1.goto(-350, 0)

    madrab2 = turtle.Turtle()
    madrab2.speed(1)
    madrab2.shape("square")
    madrab2.shapesize(stretch_len=1, stretch_wid=5)
    madrab2.color("red")
    madrab2.penup()
    madrab2.goto(350, 0)

    ball = turtle.Turtle()
    ball.speed(4)
    ball.shape("circle")
    ball.shapesize(stretch_len=1, stretch_wid=1)
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = 1

    player_1 = 0
    player_2 = 0
    scour = turtle.Turtle()
    scour.speed(0)
    scour.color("white")
    scour.penup()
    scour.hideturtle()
    scour.goto(0, 260)

    # تحديث النقاط
    def update_score():
        scour.clear()
        scour.write(f"Player 1: {player_1} Player 2: {player_2}", align="center", font=("Courier", 24, "normal"))

    # حركة المضرب 1
    def madrab1_up():
        y = madrab1.ycor()
        y += 20
        madrab1.sety(y)

    def madrab1_down():
        y = madrab1.ycor()
        y -= 20
        madrab1.sety(y)

    # حركة المضرب 2 (الكمبيوتر أو لاعب 2)
    def madrab2_computer():
        if is_computer:
            if ball.ycor() > madrab2.ycor() + 40:
                madrab2.sety(madrab2.ycor() + 20)
            elif ball.ycor() < madrab2.ycor() - 40:
                madrab2.sety(madrab2.ycor() - 20)
        else:
            # تحريك المضرب 2 من قبل اللاعب
            if ball.ycor() > madrab2.ycor() + 40:
                madrab2.sety(madrab2.ycor() + 20)
            elif ball.ycor() < madrab2.ycor() - 40:
                madrab2.sety(madrab2.ycor() - 20)

    # حركة الكرة
    def game_loop():
        global player_1, player_2
        wind.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            player_1 += 1
            update_score()

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            player_2 += 1
            update_score()

        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

        madrab2_computer()
        wind.ontimer(game_loop, 10)

    wind.listen()
    wind.onkeypress(madrab1_up, "w")
    wind.onkeypress(madrab1_down, "s")
    game_loop()

show_start_screen()
wind.mainloop()
