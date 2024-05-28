from turtle import  Screen
import time
import snake
import food
import score_board
import pygame

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

#Creating a snake
snake = snake.Snake()
food = food.Food()
score_board = score_board.Scoreboard()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake.speed_move)
    snake.move()
    if snake.head.distance(food) <= 25:
        play_sound('eating_sound.wav.wav')
        food.move()
        snake.grow(snake.tail.xcor(), snake.tail.ycor())
        score_board.upgrade()
        snake.speed_move *= 0.9
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
    for segment in snake.turtles[2:]:
        if snake.head.distance(segment) < 20:
            game_is_on = False

score_board.game_over()
play_sound('game_over.mp3')

screen.exitonclick()
