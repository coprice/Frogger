### Overview

My project is a video game, called Frogger50, in which the goal of the game is to survive as long as possible. You are a frog living on a dangerous highway, where you are constantly dodging cars trying to run you over. You lose once you get run over by a car. The game has two features: playing mode and the high scores menu.

### How to Play

While playing, you can use the arrow keys to move your character (the frog) around the screen. You can go forward and backward (which may seem futile but going forward helps give some depth perception for cars going around you), along with going side to side to dodge cars. At first, cars will spawn slowly and move relatively slowly. The longer you survive, the faster the cars will come at you and more cars will appear after a short while.

Once you lose, if your end score is higher than any of the top 5 scores (or if there are not 5 scores logged), a pop up window will appear asking for your initials to save along with your score. If you go back to the main menu and then the high score menu, you will now see your initials alongside your score. The high score menu will display up to the five high scores. The scoring is multiplied by the time of your survival--the longer you survive, your score grows at a faster rate (there is a maximum score multiplier, however).

### Additional Details

The main file for launching the game is in the graphics.py file. To launch the game, just run the graphics.py file (you will need rules.py and the img folder in the same directory). This will take you to the main menu of Frogger50, where you can choose to look at high scores of start the game. You will need python 2.7 installed.
