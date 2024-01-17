import pygame
import menu
import settings

menu_bg = menu.menu_bg
font_large = settings.font_large
font_base = settings.font_base
title_color = menu.title_color


def Scoreboard(screen):
    screen.blit(menu.menu_bg, (0, 0))
    title = font_large.render('Tablica wyników', False, title_color)
    title_rect = title.get_rect(center=(400, 150))
    screen.blit(title, title_rect)

    file = open('scoreboard.txt', 'r')
    scores = []
    for line in file:
        line = line.strip()
        scores.append(line)

    s_1 = font_base.render(f'{scores[0]}', False, title_color)
    s_1_rect = s_1.get_rect(center=(400, 300))
    s_2 = font_base.render(f'{scores[1]}', False, title_color)
    s_2_rect = s_2.get_rect(center=(400, 350))
    s_3 = font_base.render(f'{scores[2]}', False, title_color)
    s_3_rect = s_3.get_rect(center=(400, 400))
    s_4 = font_base.render(f'{scores[3]}', False, title_color)
    s_4_rect = s_4.get_rect(center=(400, 450))
    s_5 = font_base.render(f'{scores[4]}', False, title_color)
    s_5_rect = s_5.get_rect(center=(400, 500))
    screen.blit(s_1, s_1_rect)
    screen.blit(s_2, s_2_rect)
    screen.blit(s_3, s_3_rect)
    screen.blit(s_4, s_4_rect)
    screen.blit(s_5, s_5_rect)

def Save_name(nick):
    file = open('nick.txt', 'a')
    file.write(f'{nick}\n')

def Bubble_sort(scores):
    for i in range(len(scores) - 1):
        for j in range(0, (len(scores) - 1 - i)):
            if scores[j][1] > scores[j + 1][1]:
                scores[j + 1], scores[j] = scores[j], scores[j + 1]
    return scores

def Reverse_list(scores):
    copy_scores = scores.copy()
    scores.clear()
    for i in range((len(copy_scores) - 1), -1, -1):
        scores.append(copy_scores[i])
    return scores

def Sort_score(dict, mykey, myval):
    scores = []
    for x in dict:
        scores.append([x, int(dict[x])])
    scores.append([mykey, myval])
    scores = Bubble_sort(scores)
    return Reverse_list(scores)

def Save_score(score, nick):
    # print(f'{score} {nick}')
    file = open('scoreboard.txt', 'r')
    list_of_scores = {}
    for line in file:
        line.strip()
        line = line.split()
        list_of_scores.update({line[0]: line[1]})
    scores = Sort_score(list_of_scores, nick, score)
    # print(scores)
    file = open('scoreboard.txt', 'w')
    for i in range(5):
        file.write(f'{scores[i][0]} {scores[i][1]}\n')
