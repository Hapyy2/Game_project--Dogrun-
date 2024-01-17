import pygame
from sys import exit
import settings
import menu
import play
import scoreboard
import player


pygame.init()
screen = pygame.display.set_mode(settings.map_size)
pygame.display.set_caption('Dogrun')
clock = pygame.time.Clock()
#False - menu / True - game
game_active = False
#False - main menu / True - scoreboard
menu_number = False
give_nickname = True
start_time = 0

# Music
bg_music = pygame.mixer.Sound('audio/retro_vibe.mp3')
bg_music.set_volume(settings.music_volume)
bg_music.play(loops = -1)

# Menu background
menu_bg = menu.menu_bg

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and game_active == False and menu_number == False:
            if event.key == pygame.K_SPACE or event.key == pygame.K_1:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
            elif event.key == pygame.K_2:
                menu_number = True
            elif event.key == pygame.K_3:
                give_nickname = True
            elif event.key == pygame.K_4 or event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.KEYDOWN and game_active == False and menu_number == True:
            if event.key == pygame.K_1 or event.key == pygame.K_ESCAPE:
                menu_number = False
    if give_nickname:
        nick = menu.Nickname(screen)
        scoreboard.Save_name(nick)
        give_nickname = False
    if game_active:
        score = play.Play(screen, start_time)
        scoreboard.Save_score(score, nick)
        game_active = False
    else:
        if menu_number:
            scoreboard.Scoreboard(screen)
        else:
            screen.blit(menu_bg, (0, 0))
            menu.Menu(screen)

    pygame.display.update()
    clock.tick(60)
