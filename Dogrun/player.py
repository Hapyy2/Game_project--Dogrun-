import pygame
import settings

pygame.display.init()

screen = pygame.display.set_mode(settings.map_size)
speed = settings.speed

scale = 4
size = (39*scale, 25*scale)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        p_walk_1 = pygame.image.load('animation/2_Dog_2/walk_steps/walk1.png').convert_alpha()
        p_walk_1 = pygame.transform.scale(p_walk_1, size)
        p_walk_2 = pygame.image.load('animation/2_Dog_2/walk_steps/walk2.png').convert_alpha()
        p_walk_2 = pygame.transform.scale(p_walk_2, size)
        p_walk_3 = pygame.image.load('animation/2_Dog_2/walk_steps/walk3.png').convert_alpha()
        p_walk_3 = pygame.transform.scale(p_walk_3, size)
        p_walk_4 = pygame.image.load('animation/2_Dog_2/walk_steps/walk4.png').convert_alpha()
        p_walk_4 = pygame.transform.scale(p_walk_4, size)
        p_walk_5 = pygame.image.load('animation/2_Dog_2/walk_steps/walk5.png').convert_alpha()
        p_walk_5 = pygame.transform.scale(p_walk_5, size)
        p_walk_6 = pygame.image.load('animation/2_Dog_2/walk_steps/walk6.png').convert_alpha()
        p_walk_6 = pygame.transform.scale(p_walk_6, size)
        self.player_walk = [p_walk_1, p_walk_2, p_walk_3, p_walk_4, p_walk_5, p_walk_6]
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(100, 400))

    def animation_state(self):
        self.player_index += 0.25
        if self.player_index >= len(self.player_walk): self.player_index = 0
        self.image = self.player_walk[int(self.player_index)]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and self.rect.bottom <= 800:
            self.rect.y += speed
        if keys[pygame.K_UP] and self.rect.bottom >= 340:
            self.rect.y -= speed

    def update(self):
        self.animation_state()
        self.move()
