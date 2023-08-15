# Example file showing a basic pygame "game loop"
import random
from typing import Type

import pygame

from apple import generate_apple
from constants import HEIGHT, WIDTH
from snake import Snake
from snake_collision import apple_collision, wall_collision
from square import Shape, Triangle
from utils import generate_position


def game(obj: Type[Shape]):
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()
    running = True

    vector_choice = ("RIGHT", "LEFT", "DOWN", "UP")

    snake = Snake(
        obj_type=obj, position=generate_position(), vector=random.choice(vector_choice)
    )

    snake_speed = 0
    snake_speed_limit = 20

    apple = generate_apple(obj, snake.tail)

    while running and snake.alive:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.vector != "DOWN":
                        snake.vector = "UP"
                if event.key == pygame.K_DOWN:
                    if snake.vector != "UP":
                        snake.vector = "DOWN"
                if event.key == pygame.K_RIGHT:
                    if snake.vector != "LEFT":
                        snake.vector = "RIGHT"
                if event.key == pygame.K_LEFT:
                    if snake.vector != "RIGHT":
                        snake.vector = "LEFT"

        snake_speed += 1
        if snake_speed > snake_speed_limit:
            snake.move()
            if wall_collision(snake):
                snake.alive = False
            if apple_collision(apple, snake):
                snake.eat()
                apple = generate_apple(obj, snake.tail)
                snake_speed_limit -= 1
            snake_speed = 0

        # fill the screen with a color to wipe away anything from last frame

        screen.fill("purple")

        apple.draw(screen)

        snake.draw(screen)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


print("Game is started with triangle")
game(Triangle)
