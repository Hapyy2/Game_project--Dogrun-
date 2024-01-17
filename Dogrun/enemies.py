import pygame
import settings
import enemy_models
from random import randint


pygame.display.init()
screen = pygame.display.set_mode(settings.map_size)
speed_anim = settings.speed_anim


class Enemies(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'rat':
            self.frames = enemy_models.Model('rat')
        elif type == 'bird':
            self.frames = enemy_models.Model('bird')
        else:
            self.frames = enemy_models.Model('cat')

        self.animation_index = 0
        self.image = self.frames[self.animation_index]

        if type == 'rat':
            self.rect = self.image.get_rect(midbottom=(randint(900, 1100), randint(340, 800)))
        elif type == 'bird':
            self.rect = self.image.get_rect(midbottom=(randint(900, 1100), randint(380, 800)))
        else:
            self.rect = self.image.get_rect(midbottom=(randint(900, 1100), randint(340, 800)))

    def animation_state(self):
        self.animation_index += speed_anim
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
