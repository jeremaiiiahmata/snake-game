from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.x = 0
        self.createSnake()
        self.head = self.snake[0]

    def createSnake(self): #Creates a new block
        for pos in STARTING_POSITION:
            self.addSnakeBlock(pos)


    def addSnakeBlock(self, position):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(position)
        self.snake.append(block)

    def extendSnakeBlock(self):
        self.addSnakeBlock(self.snake[-1].position())

    def move(self):
        for each in range(len(self.snake) - 1, 0,-1):  # Sets the position of the next block to the current block, so it will be able to follow
            x = self.snake[each - 1].xcor()
            y = self.snake[each - 1].ycor()
            self.snake[each].setpos(x, y)

        self.head.forward(DISTANCE)  # The front block of the snake moves forward by 20 blocks.
        # The consecutive blocks will follow the first block because of the for loop earlier (where the position of the block next to it will be the its new position)

    def moveUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def moveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def moveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def moveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



