from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The OG Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, key='Up')
screen.onkey(snake.move_down, key='Down')
screen.onkey(snake.move_right, key='Right')
screen.onkey(snake.move_left, key='Left')

is_game = True
while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move_the_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or 280 < snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()


