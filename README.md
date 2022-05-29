# Pyco-8

![Pyco-8 logo, no copyright claimed](logo.png)

**Pyco-8** is a game engine based on **Pygame**, enabling the creation of videogames with an API similar to the fantasy console **Pico-8**, with the **Python** programming language.

The goal was to solve three problems that people could have with **Pico-8** :

- It's paid, and you can't use it for free.
- It uses the **Lua** programming language, which is great but not as popular as **Python**.
- It has limitations. I understand it's the principal interest of fantasy consoles, but you might want to program using the style of **Pico-8**, without it's limitations.

This way, I've been recoding the engine in **Python**, and I hope it will be useful for you.

For now, it does not have a Graphical User Interface, and I don't support all the features of **Pico-8** yet (sprites, maps, sounds, etc).

In the future, the goal is to create a graphical user interface, and all the features of **Pico-8**, so that you can easily create games with the same simplicity, but with way more flexibility, external librairies, multiplayer, save states, etc.

---

## Documentation

### Installation

The module is not yet available on PyPI, but it's a goal on the roadmap.

You need to install the requirements by running the following command :

```bash
pip install -r requirements.txt
```

For now, to install the module, simply clone the repository, and create a python file containing the following boilerplate code in the root of the folder.

```python
from engine import *

def _init():
    pass

def _update():
    pass

def _draw():
    pass

run(_init, _update, _draw)
```

This boilerplate code should generate a blank window with a black background.

This window is resizeable, and you can even set it to fullscreen. The screen will always be a square, and the aspect ratio will be preserved. Black borders will be added to the sides if the window is not a square.

---

### Customization

After cloning the repository, you should have a `config.py` file, containing settings you can change to customize the engine.
By Default, these settings will emulate **Pico-8**, but you can break the limitations by adding colors, modifying the defaut font, changing the resolution, and adding inputs.

---

### Usage

You can write your code in four different sections of your game file.

#### **Constants, classes, functions**

You can define constants, classes, functions, and global variables in the body of your game file. Be careful, declaring simple variables here will prevent them from modifying their value in the game loop functions.

This is basic **Python** knowledge, which is required to use the engine.

I also recommend using objects to store your game data.

The best practice here is to store your constants as variables in the body of the code, and to store your variables in classes.

_Example :_

```python
from engine import *

# Don't do this :
# snakeX = 0
# snakeY = 0
# size = 4

# Do this : 
class Snake():
    def __init__(self):
        # These are variables that can be modified in the game loop
        self.x = 0
        self.y = 0

SIZE = 4 # This is a constant

snake = Snake() # This is an object you can use and modify in the game loop

run(None, None, None) # If you don't use any of the three functions, you can pass None instead
```

#### **Initialisation**

The `_init` function is called once at the beginning of the game loop. This function only runs when the engine is properly initialized. Here you can call system functions, to change the window title, the framerate, etc.

#### **Update**

The `_update` function is called every frame, and is the main function of your game. It's where you can modify your variables, and do your game logic. This is for exemple where you should manage user inputs, collisions, movement, etc.

#### **Draw**

The `_draw` function is called after the `_update` function, and is where you should draw your game. You can either draw directly on the screen, or call functions and methods from your classes to draw objects.

Objects are simply drawn in the order you write the code.
The last object drawn will be on top of the others.

### API

The engine comes with a set of functions you can use to create your game.

---

#### **Logging**

Logging in a video game is a very useful way of debugging. But in game engines, you often have a lot of information to display to the console, sometimes every frame or every time something happens.
For this reason, having big chunks of white text in your console is not the best way to find the informations you've been trying to log.
For this reason, **Pyco-8** comes with a set of logging functions, to print messages in the console in a more distinctive and colorful manner.

```python
# Sample messages
info("This is a sample info message") # Blue text
warning("This is a sample warning message") # Yellow text
error("This is a sample error message") # Red text
success("This is a sample success message") # Green text
debug("This is a sample debug message") # White text
```

You can still use the regular `print` function to print messages if you want some additional features the print function has, such as modifying the end character, or printing multiple variables using multiple arguments.

> TODO : Add all the optional parameters of the original `print`function into all of the logging functions.

---

#### **Running**

The `run` function takes three arguments as functions : `_init`, `_update`, and `_draw`. Please note that these are the names I personally give to my functions, but you can name them however you want.

It should be called at the end of your game file, as it will start the game loop.

The `run` function will handle user inputs, and will call the functions you passed as arguments at the required time.

The framerate can be changed using the `set_framerate` function.

```python
# You should call this function in the _init function.
set_framerate(60) # Set the framerate to 60 frames per second
```

Additionally, you can retrieve the fps count using the `get_fps` function.

```python
framerate = get_fps() # Get the current framerate
```

Finally, you can change the name of the window using the set_name() function.

```python
set_name("Hello from Pyco-8 Documentation !") # Change the name of the window
```

#### **Drawing**

The module comes with a set of functions to draw objects on the screen.

- `pset(x, y, [color])` : Draw a pixel at the given coordinates, with the given color. By default, - and that is true for every drawing function that takes an optional color argument -, the function will use the color 7, which is white with the default color palette.

- `rect(x, y, width, height, [color])` : Draw a rectangle at the given coordinates, with the given width and height, and the given color.

- `rectfill(x, y, width, height, [color])` : Draw a filled rectangle at the given coordinates, with the given width and height, and the given color.

- `circ(x, y, radius, [color])` : Draw a circle at the given coordinates, with the given radius, and the given color.

- `circfill(x, y, radius, [color])` : Draw a filled circle at the given coordinates, with the given radius, and the given color.

- `line(x1, y1, x2, y2, [color])` : Draw a line between the given coordinates, with the given color.

- `oval(x, y, width, height, [color])` : Draw an oval at the given coordinates, with the given width and height, and the given color.

- `ovalfill(x, y, width, height, [color])` : Draw a filled oval at the given coordinates, with the given width and height, and the given color.

> TODO : Make the width of the lines configurable via another parameter.

- `gprint(text, x, y, [color])` : Draw the given text at the given coordinates, with the given color using the font defined in the `config.py` file.

- `spr(sprite, x, y)` : Draw the given sprite at the given coordinates.

> TODO :
>
> - Make a sprite editor, to create sprites.
> - Allow sprites to be stretched, flipped, and rotated.

- `pget(x, y)` : Return the color of the pixel at the given coordinates.

#### **Inputs**

- `btn(button)` : Return the state of the given button.
- `btnp(button)` : Returns True if the button has just been pressed.
- `btnr(button)` : Returns True if the button has just been released.

> Note : The button argument is a key from the INPUT dictionary defined in the config.py file. By default : `up`, `down`, `left`, `right`,`'action1`, `action2`.
>
> The buttons strings are not case sensitive : `UP`, `Down`, `left`, `RIGHT`, `action1`, `aCtIoN2` are all valid.

## What else is coming ?

My goal is to create a fully-fledged game engine, wiht just enough features to be able to make complete games, but also simple enough to be used by anybody, and to have a extremely reasonable learning curve.

Some features are to be expected :

- Graphical User Interface, **Pico-8** style : It won't be mandatory, and you will still be able to use the engine without it. It probably won't contain a code editor, but it will be possible to create your own sprites, musics, maps, sound effects, etc.

- Sounds : You will be able to play sounds from mp3 files, or from a list of pre-defined sounds. You will also be able to play specific frequencies from a determined period of time.

- Music : You will be able to play music from mp3 files. You will also be able to combine sounds to create a music.

- Sprite editor : A GUI Tool that allows you to create sprites, and to edit them. Sprites can be stored in a single spritesheet, or in multiple separate files.

- Map editor : A GUI Tool that allows you to create maps, and to edit them.

- Camera : You will be able to move the camera around the screen, and to follow objects.

- Export : The goal is to create an exported for at least the three main Operating Systems (Windows, Linux, and MacOS), and for the web (HTML5). I'm not sure if it's possible to create stable enough versions for the web, but I'll do my best. (Maybe checkout Trinket ?)

- Replacing lists with numpy arrays : If I ever encounter performance issues, I'll try using numpy wherever I can to improve performance.

- Not using **Pygame** : **Pygame** sure is useful, but I may be able to recreate all my graphics features without it. This would be more performant and would result in a way lighter engine.

- `pip install pyco-8` : I want to upload the project on the Python Package Index (PyPI) once it's stable, complete and documented enough. For now, the only way to use the engine will be to download the source code.
