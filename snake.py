from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.snake_body()

    def snake_body(self):
        for position in positions:
            self.add_segment(position)
        self.head = self.segments[0]

    def move_the_snake(self):
        for snake_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[snake_num - 1].xcor()
            y = self.segments[snake_num - 1].ycor()
            self.segments[snake_num].goto(x, y)
        self.head.forward(20)

    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.snake_body()
        self.head = self.segments[0]

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
