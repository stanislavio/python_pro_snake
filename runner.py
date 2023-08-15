# Example file showing a basic pygame "game loop"
import random
from typing import Type

import pygame

from apple import generate_apple
from constants import HEIGHT, VECTOR_CHOICES, WIDTH
from snake import Snake
from snake_collision import apple_collision, wall_collision
from square import Shape, Triangle
from utils import generate_position

running = True


def game_setup():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    return screen, clock


def generate_snake(obj: Type[Shape]):
    return Snake(
        obj_type=obj, position=generate_position(), vector=random.choice(VECTOR_CHOICES)
    )


def manage_keyboard(snake: Snake):
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    global running
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


def game(obj: Type[Shape]):
    global running
    screen, clock = game_setup()

    snake = generate_snake(obj)

    apple = generate_apple(obj, snake.tail)

    while running and snake.alive:
        manage_keyboard(snake)
        snake.speed += 1
        if snake.speed > snake.speed_limit:
            snake.move()
            if wall_collision(snake):
                snake.alive = False
            if apple_collision(apple, snake):
                snake.eat()
                apple = generate_apple(obj, snake.tail)
                snake.speed_limit -= 1
            snake.speed = 0

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
print("Game over")
