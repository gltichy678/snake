from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import scoreboard , GameOver

screen = Screen()

screen.setup(width=600, height=600)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = scoreboard()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(key="w", fun=snake.top)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="d", fun=snake.right)
    if snake.head.distance(food) < 15:
        print("Size increased")
        food.randomize()
        snake.extend()
        score.update_score()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        end = GameOver()
        is_game_on = False
    elif snake.check_collision():
        end = GameOver()
        is_game_on = False


screen.exitonclick()
