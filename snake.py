from turtle import Turtle, Screen
positions = ((0, 0), (-20, 0), (-40, 0))
steps = 20
speed = 1  # can be changed by score increase ....
screen = Screen()
score = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[len(self.snake)-1]
        self.eat()
        self.movement()
        self.increase_speed()

    def create_snake(self):
        global steps, speed
        for position in positions:
            snake_unit = Turtle("square")
            snake_unit.penup()
            snake_unit.color("white")
            snake_unit.goto(position)
            self.snake.append(snake_unit)
            snake_unit.speed(speed)

    def move(self):
        for unit in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[unit - 1].xcor()
            new_y = self.snake[unit - 1].ycor()
            self.snake[unit].goto(new_x, new_y)
        self.snake[0].forward(steps)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
        else:
            self.move()

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
        else:
            self.move()

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
        else:
            self.move()

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
        else:
            self.move()

    def movement(self):
        self.move()
        screen.onkey(fun=self.up, key="Up")
        screen.onkey(fun=self.down, key="Down")
        screen.onkey(fun=self.right, key="Right")
        screen.onkey(fun=self.left, key="Left")

    def eat(self):
        tail_x = self.tail.xcor()
        tail_y = self.tail.ycor()
        snake_unit = Turtle("square")
        snake_unit.penup()
        snake_unit.color("white")
        snake_unit.goto(tail_x, tail_y)
        self.snake.append(snake_unit)
        snake_unit.speed(speed)

    def increase_speed(self):
        for unit in self.snake:
            unit.speed(+1)

    def check(self):
        for snake_unit in self.snake:
            dis = snake_unit.distance(self.snake[0])
            if dis < 20 and snake_unit != self.snake[0]:
                self.snake.clear()
                screen.clear()


