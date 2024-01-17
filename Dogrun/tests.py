import play
import scoreboard
import enemy_models
import settings
import pygame


def test_Sort_score():
    assert scoreboard.Sort_score({'a': '100', 'b': '50'}, 'c', 75) == [['a', 100], ['c', 75], ['b', 50]]


def test_Bubble_sort():
    assert scoreboard.Bubble_sort([['b', 50], ['a', 100], ['c', 75]]) == [['b', 50], ['c', 75], ['a', 100]]
    assert scoreboard.Bubble_sort([['a', 100], ['c', 75], ['b', 75]]) == [['c', 75], ['b', 75], ['a', 100]]


def test_Reverse():
    assert scoreboard.Reverse_list([['b', 50], ['c', 75], ['a', 100]]) == [['a', 100], ['c', 75], ['b', 50]]


def test_Sec_to_mili():
    assert settings.Sec_to_mili(settings.seconds) == 800


def test_Check_alive():
    assert play.check_alive(10) == None
