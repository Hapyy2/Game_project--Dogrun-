import pygame
import settings

def Menu(screen):
    screen.blit(title, title_rect)
    screen.blit(option_1, option_1_rect)
    screen.blit(option_1_desc, option_1_desc_rect)
    screen.blit(option_2, option_2_rect)
    screen.blit(option_3, option_3_rect)
    screen.blit(option_exit, option_exit_rect)
    screen.blit(option_exit_desc, option_exit_desc_rect)

pygame.font.init()
font_base = settings.font_base
font_small = settings.font_small
font_large = settings.font_large
font_title = settings.font_title

# Menu
title_color = settings.title_color
menu_color = settings.menu_color
desc_color = settings.desc_color
warning_color = settings.warning_color

# Background
pygame.display.init()
screen = pygame.display.set_mode((800, 800))
menu_bg = pygame.image.load('background/clouds.png').convert()
menu_bg = pygame.transform.scale(menu_bg, (1422, 800))

title = font_title.render('Dogrun',False,title_color)
title_rect = title.get_rect(center = (400, 200))
option_1 = font_base.render('1. Rozpocznij grę',False,menu_color)
option_1_rect = option_1.get_rect(center = (400, 350))
option_1_desc = font_small.render('SPACJA LUB 1',False,desc_color)
option_1_desc_rect = option_1_desc.get_rect(center = (410, 390))
option_2 = font_base.render('2. Tabela wyników',False,menu_color)
option_2_rect = option_2.get_rect(center = (400, 440))
option_3 = font_base.render('3. Zmień nazwę',False,menu_color)
option_3_rect = option_2.get_rect(center = (440, 500))
option_exit = font_base.render('WYJDŹ',False,warning_color)
option_exit_rect = option_exit.get_rect(center = (400,560))
option_exit_desc = font_small.render('ESC LUB 4',False,desc_color)
option_exit_desc_rect = option_exit.get_rect(center = (435,610))

# Nick input
nick_input = font_base.render('Wprowadź swoje imię',False,title_color)
nick_input_rect = nick_input.get_rect(center = (400, 300))
warning = font_small.render('Max 14 znaków',False,desc_color)
warning_rect = warning.get_rect(center = (400, 330))
press_enter = font_small.render('TAB ABY ZAPISAĆ',False,desc_color)
press_enter_rect = press_enter.get_rect(center = (400, 450))
nick_error = font_base.render('WPISZ POPRAWNĄ NAZWĘ',False,warning_color)
nick_error_rect = nick_error.get_rect(center = (400, 500))


def nick_type(text):
    nick = font_base.render(f'{text}', False, 'black')
    nick_rect = nick_input.get_rect(center=(420, 400))
    return [nick, nick_rect]


def Nickname(screen):
    nick = ''
    error = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.TEXTINPUT:
                if len(nick) <= 14:
                    nick += event.text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_BACKSPACE:
                    nick = nick[:-1]
                if event.key == pygame.K_TAB and nick != '':
                    return nick
                if event.key == pygame.K_TAB and nick == '':
                    error = True

        screen.blit(menu_bg, (0, 0))
        screen.blit(nick_input, nick_input_rect)
        screen.blit(warning, warning_rect)
        screen.blit(press_enter, press_enter_rect)
        nick_text = nick_type(nick)[0]
        nick_text_rect = nick_type(nick)[1]
        screen.blit(nick_text, nick_text_rect)
        if error:
            screen.blit(nick_error, nick_error_rect)
        pygame.display.update()
