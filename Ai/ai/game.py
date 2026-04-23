import pygame
import random
pygame.init()
# Screen size
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font = pygame.font.SysFont(None, 30)
def score_display(score):
    value = font.render("Score: " + str(score), True, black)
    screen.blit(value, [10, 10])
def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block, block])
def game():
    game_over = False
    game_close = False
    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0
    snake_list = []
    snake_length = 1
    food_x = round(random.randrange(0, width - snake_block) / 10) * 10
    food_y = round(random.randrange(0, height - snake_block) / 10) * 10
    while not game_over:
        while game_close:
            screen.fill(white)
            msg = font.render("Game Over! Press Q-Quit C-Play", True, red)
            screen.blit(msg, [100, 150])
            score_display(snake_length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0
        x += x_change
        y += y_change
        # Wall collision
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        screen.fill(white)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        # Self collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        draw_snake(snake_block, snake_list)
        score_display(snake_length - 1)
        pygame.display.update()
        # Food collision
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10) * 10
            food_y = round(random.randrange(0, height - snake_block) / 10) * 10
            snake_length += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
game()