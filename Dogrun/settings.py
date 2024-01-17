import pygame

def Sec_to_mili(seconds):
    return seconds * 1000


# Font
pygame.font.init()
font_base = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 50)
font_small = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 20)
font_large = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 100)
font_title = pygame.font.Font('font/static/PixelifySans-Bold.ttf', 160)

map_size = (800, 800)
speed = 4
lives = 3
music_volume = 0.25

# Colors
warning_color = (178, 34, 34)
desc_color = (0, 139, 139)
title_color = (34, 139, 34)
menu_color = (65, 105, 225)

# Enemies
# Spawn of enemies
seconds = 0.8
spawn_rate = int(Sec_to_mili(seconds))
# Size of enemies
scale_rat = 3
scale_bird = 3
scale_cat = 3
size_rat = (25*scale_rat, 11*scale_rat)
size_bird = (19*scale_bird, 14*scale_bird)
size_cat = (31*scale_cat, 20*scale_cat)
# Animation speed of enemies
speed_anim = 0.25
