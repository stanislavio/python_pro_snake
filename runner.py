# Example file showing a basic pygame "game loop"
import pygame

from apple import generate_apple
from constants import WIDTH, HEIGHT
from snake import Snake
from utils import generate_position

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()
running = True

snake = Snake(generate_position())

snake_speed = 0
snake_vector = pygame.K_RIGHT

apple = generate_apple(snake.tail)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_vector = pygame.K_UP
            if event.key == pygame.K_DOWN:
                snake_vector = pygame.K_DOWN
            if event.key == pygame.K_RIGHT:
                snake_vector = pygame.K_RIGHT
            if event.key == pygame.K_LEFT:
                snake_vector = pygame.K_LEFT

    snake_speed += 1
    if snake_speed > 20:
        snake.move(snake_vector)
        snake_speed = 0

    # fill the screen with a color to wipe away anything from last frame

    screen.fill("purple")

    apple.draw(screen)

    snake.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
