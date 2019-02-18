import arcade
import random

WIDTH = 480
HEIGHT = 640
TITLE = 'RAIN'

BLACK = arcade.color.BLACK
ALICE_BLUE = arcade.color.ALICE_BLUE
PURPLE = arcade.color.PURPLE

class Drop:
    def __init__(self, x, y, dx, dy, speed, thic):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.speed = speed
        self.color = PURPLE
        self.thic = thic

    def update(self):
        self.y -= self.speed
        self.dy -= self.speed

    def reset(self):
        self.x = random.randrange(WIDTH)
        self.y = random.randrange(HEIGHT, HEIGHT + 100)
        self.dx = random.randrange(self.x-1, self.x+1)
        self.dy = random.randrange(self.y-10, self.y)
        self.speed = random.randrange(5, 8)
        self.thic = random.randrange(1,3)

    def draw(self):
        arcade.draw_line(self.x, self.y, self.dx, self.dy, self.color, self.thic)

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.rain = None

    def on_draw(self):
        arcade.start_render()
        for drop in self.rain:
            drop.draw()

    def update(self, delta_time):
        for drop in self.rain:
            drop.update()
            if drop.dy < 0:
                drop.reset()

    def setup(self):
        arcade.set_background_color(ALICE_BLUE)
        self.rain = []
        for i in range(150):
            x = random.randrange(WIDTH)
            y = random.randrange(HEIGHT, HEIGHT + 50)
            dx = random.randrange(x-1, x+1)
            dy = random.randrange(y-10, y)
            speed = random.randrange(5, 8)
            thic = random.randrange(1,3)
            drop = Drop(x, y, dx, dy, speed, thic)
            self.rain.append(drop)

def main():
    window = Window(WIDTH, HEIGHT, TITLE)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
