# Little Light :candle:

![Candle Light](/images/giphy.gif)

A basic Python game currently consisting of 5 levels, made as a school project and chosen in order to practice concepts of game design that are common to many games.

[Landing Page](https://gabrielabdul.github.io/LittleLight/)

## About / synopsis

A game about a small boy in a very big world, who just wants to make the world a brighter place.

## Built With

* [Python]

## How to install :computer:

* To run from source code, Python version 3.4 or higher along with the PyGame module must be installed. Once installed run
```
python3 ./littlelight.py
```
and you'll be good to go!

## Built By

* [Brett Davis](https://github.com/menacingmanatee) [twitter](https://twitter.com/bre_p_d) [LinkedIn](https://www.linkedin.com/in/brett-davis-132916155/): Level design and backend :adult:
* [Gabriel Abdul-Raheem](https://github.com/gabrielabdul) [twitter](https://twitter.com/__GabrielAbdul) [LinkedIn](https://www.linkedin.com/in/gabriel-abdul-raheem-3a1a01144/): Save and Achievements feature, minor sprite design/aesthetics :adult:
* [Jill Rogers](https://github.com/jilroge7) [twitter](https://twitter.com/JilRoge7) [LinkedIn](https://www.linkedin.com/in/jill-rogers-ba29313a/): Art design - sprites, maps :woman:
* Lauren Collins: Title screen image, pause screen image :woman:

## How to play :desktop\_computer:

### Controls: :keyboard:

* ESC - Pause the game
* W, A, S, D - jump/climb, move left, move down through platforms, and move right respectively. The arrow keys may also be used
* R - resets the level if you get stuck
* L - Lights a candle if you are close enough to the wick

### Gameplay:

The goal of each level is to move to the candle and light it, before proceeding to the bottom right of the screen. Reaching the candle will be done using both platforming and puzzling skills.
Enemies exist on each level, and while defeating them is not mandatory, their deaths may make levels easier. Killing/sparing enemies has no effect on gameplay currently, but plans are in place to add weight to the decision in the future.
The player has 3 stats you can control at the start of the game; strength, agility, and glow. All have more planned interactions in future versions, but currently strength and glow affect your health, while agility affects how frequently you can jump.
The player has 3 lives at the start of the game, and will have to load from a save upon losing all of them. The game autosaves after each level, but manual saving is not yet implemented.

### Screenshots: :framed\_picture:

<details>
    <summary>Main Menu:</summary>

![Main Menu](/images/littlelight_mainMenu.png)
</details>
<details>
    <summary>Character Creation:</summary>

![Character Creation](/images/littlelight_charSelection.png)
</details>
<details>
    <summary>Level One:</summary>

![Level One](/images/littlelight_levelOne.png)
</details>
<details>
    <summary>Level Two:</summary>

![Level Two](/images/littlelight_levelTwo.png)
</details>
<details>
    <summary>Level Three:</summary>

![Level Three](/images/littlelight_levelThree.png)
</details>
<details>
    <summary>Level Four:</summary>

![Level Four](/images/littlelight_levelFour.png)
</details>
<details>
    <summary>Level Five:</summary>

![Level Five](/images/littlelight_levelFive.png)
</details>

### Project contents

| Filename | Description |
| --- | --- |
|littlelight.py|Main game file, initializes the game and starts at the title screen|
|engine/|Contains the file storage module, defining how saving is performed|
|images/|Contains all images used in the project, including sprites, maps, and menus|
|models/|Contains all classes used in the project, as well as the game loop|
