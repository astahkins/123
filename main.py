import pygame
import random
import time

def generate_food():
    random_x = random.randint(0, WIDTH-tile_size)//tile_size*tile_size
    random_y = random.randint(0, HEIGHT-tile_size)//tile_size*tile_size
    food_coord = [random_x,random_y]
    if food_coord not in snake_titles:
        return food_coord
    else:
        generate_food()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
aqua = (0, 255, 255)

WIDTH = 800
HEIGHT = 800

tile_size = 20
snake_speed = 5

snake_x = WIDTH // 2
snake_y = HEIGHT // 2

change_x = change_y = 0

snake_titles = []
snake_size = 1

pygame.init()
main_screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

food_coord = generate_food()

while True:
    main_screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_y = -tile_size
                change_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_y = tile_size
                change_x = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_y = 0
                change_x = -tile_size
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_y = 0
                change_x = tile_size

    snake_x += change_x
    snake_y += change_y

    if [snake_x, snake_y] in snake_titles:





    new_tail = [snake_x, snake_y]
    snake_titles.append(new_tail)

    if len(snake_titles) > snake_size:
        snake_titles.pop(0)

    for x, y in snake_titles:
        pygame.draw.rect(
            main_screen,
            white,
            (x, y, tile_size, tile_size)
        )
    pygame.draw.rect(main_screen, red, (food_coord[0], food_coord[1], tile_size, tile_size))

    pygame.display.update()
    clock.tick(snake_speed)
