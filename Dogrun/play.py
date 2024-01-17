import pygame
import enemies
import settings
import player
import math
from settings import font_base
from random import choice


def display_score(screen, start_time):
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = font_base.render(f'Score: {current_time}',False,(31,32,34))
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time

def display_lives(screen, lives):
    lives_surf = font_base.render(f'Lives: {lives}',False,settings.warning_color)
    lives_rect = lives_surf.get_rect(center = (400, 100))
    screen.blit(lives_surf, lives_rect)

def collision_sprite():
	if pygame.sprite.spritecollide(player1.sprite,enemies_group,False):
		return True
	else: return False


clock = pygame.time.Clock()

# Player
player1 = pygame.sprite.GroupSingle()
player1.add(player.Player())

# Enemies
enemies_group = pygame.sprite.Group()

enemies_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemies_timer,settings.spawn_rate)

# Background
background = pygame.image.load('background/city/6.png').convert()
background = pygame.transform.scale2x(background)
background2 = pygame.image.load('background/grass.png').convert()
bg_width = background.get_width()
bg2_width = background2.get_width()
tiles = math.ceil(800 / bg_width) + 1
tiles2 = math.ceil(800 / bg2_width) + 1

def check_alive(score):
    if collision_sprite():
        lives -= 1
        enemies_group.empty()
        if lives <= 0:
            enemies_group.empty()
            return score
    return None


def Play(screen, start_time):
    lives = settings.lives
    scroll = 0
    scroll2 = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == enemies_timer:
                enemies_group.add(enemies.Enemies(choice(['rat', 'rat', 'rat', 'bird', 'bird', 'cat'])))

        for i in range(0, tiles):
            screen.blit(background, (i * bg_width + scroll, 0))
        for i in range(0, tiles2):
            screen.blit(background2, (i * bg2_width + scroll2, 340))

        scroll -= 4
        scroll2 -= 6
        if abs(scroll) > bg_width:
            scroll = 0
        if abs(scroll2) > bg2_width:
            scroll2 = 0

        score = display_score(screen, start_time)
        display_lives(screen, lives)

        player1.draw(screen)
        player1.update()

        enemies_group.draw(screen)
        enemies_group.update()

        if collision_sprite():
            lives -= 1
            enemies_group.empty()
            if lives <= 0:
                enemies_group.empty()
                return score

        pygame.display.update()
        clock.tick(60)
