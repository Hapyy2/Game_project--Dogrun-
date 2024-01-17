import pygame
import settings


size_rat = settings.size_rat
size_bird = settings.size_bird
size_cat = settings.size_cat


def Model(type):
    if type == 'rat':
        rat_walk_1 = pygame.image.load('animation/Rat/walk_steps/walk1.png').convert_alpha()
        rat_walk_1 = pygame.transform.scale(rat_walk_1, size_rat)
        rat_walk_2 = pygame.image.load('animation/Rat/walk_steps/walk2.png').convert_alpha()
        rat_walk_2 = pygame.transform.scale(rat_walk_2, size_rat)
        rat_walk_3 = pygame.image.load('animation/Rat/walk_steps/walk3.png').convert_alpha()
        rat_walk_3 = pygame.transform.scale(rat_walk_3, size_rat)
        rat_walk_4 = pygame.image.load('animation/Rat/walk_steps/walk4.png').convert_alpha()
        rat_walk_4 = pygame.transform.scale(rat_walk_4, size_rat)
        return [rat_walk_1, rat_walk_2, rat_walk_3, rat_walk_4]
    elif type == 'bird':
        bird_1 = pygame.image.load('animation/Bird/walk_steps/walk1.png').convert_alpha()
        bird_1 = pygame.transform.scale(bird_1, size_bird)
        bird_2 = pygame.image.load('animation/Bird/walk_steps/walk2.png').convert_alpha()
        bird_2 = pygame.transform.scale(bird_2, size_bird)
        bird_3 = pygame.image.load('animation/Bird/walk_steps/walk3.png').convert_alpha()
        bird_3 = pygame.transform.scale(bird_3, size_bird)
        bird_4 = pygame.image.load('animation/Bird/walk_steps/walk4.png').convert_alpha()
        bird_4 = pygame.transform.scale(bird_4, size_bird)
        bird_5 = pygame.image.load('animation/Bird/walk_steps/walk5.png').convert_alpha()
        bird_5 = pygame.transform.scale(bird_5, size_bird)
        bird_6 = pygame.image.load('animation/Bird/walk_steps/walk6.png').convert_alpha()
        bird_6 = pygame.transform.scale(bird_6, size_bird)
        return [bird_1, bird_2, bird_3, bird_4, bird_5, bird_6]
    else:
        cat_1 = pygame.image.load('animation/Cat/walk_steps/walk1.png').convert_alpha()
        cat_1 = pygame.transform.scale(cat_1, size_cat)
        cat_2 = pygame.image.load('animation/Cat/walk_steps/walk2.png').convert_alpha()
        cat_2 = pygame.transform.scale(cat_2, size_cat)
        cat_3 = pygame.image.load('animation/Cat/walk_steps/walk3.png').convert_alpha()
        cat_3 = pygame.transform.scale(cat_3, size_cat)
        cat_4 = pygame.image.load('animation/Cat/walk_steps/walk4.png').convert_alpha()
        cat_4 = pygame.transform.scale(cat_4, size_cat)
        cat_5 = pygame.image.load('animation/Cat/walk_steps/walk5.png').convert_alpha()
        cat_5 = pygame.transform.scale(cat_5, size_cat)
        cat_6 = pygame.image.load('animation/Cat/walk_steps/walk6.png').convert_alpha()
        cat_6 = pygame.transform.scale(cat_6, size_cat)
        return [cat_1, cat_2, cat_3, cat_4, cat_5, cat_6]