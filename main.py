import pygame
from sys import exit
from random import randint
pygame.init()


def show_score():
    score_surf = def_font.render(f'Score: {score}', False, "Black")
    score_rect = score_surf.get_rect(center=(640, 60))
    screen.blit(score_surf, score_rect)



game_running = False
score = 0
screen = pygame.display.set_mode((1280, 760))
pygame.display.set_caption("Fruit Collector")
pygame.display.set_icon(pygame.image.load('img/basket.png'))
clock = pygame.time.Clock()
background_surf = pygame.image.load("img/bg.png")
def_font = pygame.font.Font("PixelFont.ttf", 100)
basket_surf = pygame.image.load("img/basket.png").convert_alpha()
spawn_timer = pygame.USEREVENT+1
pygame.time.set_timer(spawn_timer, 500)


game_title = def_font.render(
    'Fruit Collector! Collect them all!', False, (0, 0, 0))
game_title_rect = game_title.get_rect(center=(640, 60))
game_help = def_font.render('Press SPACE to get started!', False, (0, 0, 0))
game_help_rect = game_help.get_rect(center=(640, 640))
game_restart_help = def_font.render('Press SPACE to restart', False, (0, 0, 0))
game_restart_help_rect = game_restart_help.get_rect(center=(640, 640))
# Fruits
apple_surf = pygame.image.load("img/apple.png").convert_alpha()
grapes_surf = pygame.image.load("img/grapes.png").convert_alpha()
melon_surf = pygame.image.load("img/melon.png").convert_alpha()
bomb_surf = pygame.image.load("img/bomb.png").convert_alpha()

apple_rect = apple_surf.get_rect(center=(randint(70, 1210), 0))
melon_rect = melon_surf.get_rect(center=(randint(70, 1210), 0))
grapes_rect = grapes_surf.get_rect(center=(randint(70, 1210), 0))
bomb_rect = bomb_surf.get_rect(center=(randint(70, 1210), 0))

x = 640
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not game_running:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_running = True
                score = 0
                bomb_rect.y = 0
                apple_rect.y = 0
                bomb_start = 0
                melon_start = 0
                grape_start = 0
                random_bomb = randint(4,10)
                random_grapes = randint(3,15)
                random_melon = randint(35,50)
    userInput = pygame.key.get_pressed()
    if game_running:
        if userInput[pygame.K_LEFT]:
            x -=25
        if userInput[pygame.K_RIGHT]:
            x +=25

    if game_running:
        screen.blit(background_surf, (0, 0))
        basket_rect = basket_surf.get_rect(center=(x, 650))
        screen.blit(basket_surf, basket_rect)


        #apple movement---------------------------
        screen.blit(apple_surf, apple_rect)
        apple_rect.y += 15
        if apple_rect.y > 800:
            apple_rect.y = 0
            apple_rect = apple_surf.get_rect(center=(randint(70, 1210), 0))
            bomb_start += 1
            grape_start += 1
            melon_start += 0
        if basket_rect.colliderect(apple_rect):
            apple_rect.y = 0
            score += 10
            apple_rect = apple_surf.get_rect(center=(randint(70, 1210), 0))
            bomb_start += 1
            grape_start += 1
            melon_start += 1
        #grapes movement-------------------
        if grape_start >= random_grapes:
            screen.blit(grapes_surf, grapes_rect)
            grapes_rect.y += 15
            if grapes_rect.y > 800:
                grapes_rect.y = 0
                grapes_rect = grapes_surf.get_rect(center=(randint(70, 1210), 0))
                grape_start = 0
            if basket_rect.colliderect(grapes_rect):
                grapes_rect.y = 0
                score += 50
                grapes_rect = grapes_surf.get_rect(center=(randint(70, 1210), 0))
                grape_start = 0
        
        #melons movement-------------------
        if melon_start >= random_melon:
            screen.blit(melon_surf, melon_rect)
            melon_rect.y += 20
            if melon_rect.y > 800:
                melon_rect.y = 0
                melon_rect = melon_surf.get_rect(center=(randint(70, 1210), 0))
                melon_start = 0
            if basket_rect.colliderect(melon_rect):
                melon_rect.y = 0
                score += 250
                melon_rect = melon_surf.get_rect(center=(randint(70, 1210), 0))
                melon_start = 0

        #bomb movement-------------------
        if bomb_start >= random_bomb:
            screen.blit(bomb_surf, bomb_rect)
            bomb_rect.y += 15
            if bomb_rect.y > 800:
                bomb_rect.y = 0
                bomb_rect = bomb_surf.get_rect(center=(randint(70, 1210), 0))
                bomb_start = 0
            if basket_rect.colliderect(bomb_rect):
                bomb_rect.y = 0
                game_running = False
                bomb_rect = bomb_surf.get_rect(center=(randint(70, 1210), 0))
        show_score()
    else:
        screen.blit(background_surf, (0, 0))
        if score == 0:
            screen.blit(game_help, (game_help_rect))
            screen.blit(game_title, (game_title_rect))
        else:
            screen.blit(game_restart_help, (game_restart_help_rect))
            game_score = def_font.render(
                f'Your score is {score}', False, (0, 0, 0))
            game_score_rect = game_score.get_rect(center=(640, 60))
            screen.blit(game_score, (game_score_rect))

    pygame.display.update()
    clock.tick(60)
