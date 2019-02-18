import arcade
import random

WIDTH = 480
HEIGHT = 640
TITLE = 'RAIN'

BLACK = arcade.color.BLACK
ALICE_BLUE = arcade.color.ALICE_BLUE
PURPLE = arcade.color.PURPLE

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        arcade.start_render()

    def setup(self):
        arcade.set_background_color(ALICE_BLUE)

def main():
    window = Window(WIDTH, HEIGHT, TITLE)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
