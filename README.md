<h1 align="Center">"Dogrun" - pygame project</h1>


## Description
---------------------------------
Dogrun is a project that uses pygame library to create a simple game about a **Dog** running. What else do you need? Just download the game and enjoy. <br>
To play You need to download the files and run the `main.py` file. You can use an editor like Pycharm.

## Requirements for the project
---------------------------------
1. Dividing the project into files<br>
  * List of the files
      * test.py - file with tests of functions
      * enemies.py - contains the class of enemies
      * enemy_models.py - models of the enemies (rat, bird and cat)
      * main.py - main module of the game (run it to initialize the game)
      * menu.py - code of the main menu 
      * nick.txt - text file with names of all the players who played
      * play.py - contains the actual game module
      * player.py - contains the class of player character
      * scoreboard.py - code responsible for displaying and operating the scoreboard (sorting and saving scores)
      * scoreboard.txt - text file with top 5 players and their scores
      * settings.py - variables used in the project for example `music_volume`
      * Credits.txt - contains links to assets used in the project
3. Function tests using pytest
```python
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
```
4. Use of arrays, tuples and dictionaries
 * Commonly used in the procet for example `Save_score` funtion bellow in point 8 uses a dictionary
6. Scoreboard <br><br>
![Game screen 3](/screen3.PNG "screen3")
8. Working with files
```python
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
```
9. Algorithms used
```python
# Bubble sort
def Bubble_sort(scores):
    for i in range(len(scores) - 1):
        for j in range(0, (len(scores) - 1 - i)):
            if scores[j][1] > scores[j + 1][1]:
                scores[j + 1], scores[j] = scores[j], scores[j + 1]
    return scores
# Reversing a list
def Reverse_list(scores):
    copy_scores = scores.copy()
    scores.clear()
    for i in range((len(copy_scores) - 1), -1, -1):
        scores.append(copy_scores[i])
    return scores
```
11. Academic level

## Screenshots from the game
---------------------------------
![Game screen 1](/screen1.PNG "screen1")<br><br>
![Game screen 2](/screen2.PNG "screen2")

Credits:<br>
*Animal animations*: https://free-game-assets.itch.io/free-street-animal-pixel-art-asset-pack<br>
*City background*: https://free-game-assets.itch.io/free-city-backgrounds-pixel-art<br>
*Sky background*: https://free-game-assets.itch.io/free-sky-with-clouds-background-pixel-art-set<br>
*Grass assets*: https://styloo.itch.io/pixel-grass-and-flowers<br>
*Music*: https://www.fesliyanstudios.com/royalty-free-music/download/8-bit-retro-funk/883<br>
