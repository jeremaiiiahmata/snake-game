from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

gameOver = False

snake = Snake()
food = Food()
scoreboard = Scoreboard()



# ----- Only executes when triggered
screen.listen()  # Listens for any key events
screen.onkey(key="w", fun=snake.moveUp)
screen.onkey(key="a", fun=snake.moveLeft)
screen.onkey(key="s", fun=snake.moveDown)
screen.onkey(key="d", fun=snake.moveRight)


while not gameOver:
    screen.update()
    time.sleep(0.1) #Screens update every 0.1 seconds
    snake.move() #Everytime the screen refreshes, the snake move by 20 steps.

    #Detect food collision
    if snake.head.distance(food) < 15:
        food.generate()
        scoreboard.increaseScore()
        snake.extendSnakeBlock()

    # Detect boundary collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameOver = True
        scoreboard.reset()
        snake.reset()

    #Detecting tail collision
    for tail in snake.snake[1:]:
        if snake.head.distance(tail) < 10:
            gameOver = True
            scoreboard.reset()
            snake.reset()





screen.exitonclick()