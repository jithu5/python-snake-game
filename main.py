from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create snake 
snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    # detect collosion with food 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
        print("food")
    # print(snake.head.xcor,snake.head.ycor)
    
    # detect collision with wall 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        score_board.reset()

    # detect collision with tail 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score_board.reset()

screen.exitonclick()