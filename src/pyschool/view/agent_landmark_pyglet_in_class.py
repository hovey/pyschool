# agent_landmark_pyglet.py
import time
from numpy.random import randint

import pyglet
from pyglet.window import key
from pyglet import shapes

# references:
# double-buffing and tearing
# https://pyglet.readthedocs.io/en/latest/programming_guide/windowing.html#double-buffering
# /pyglet/examples/graphics/shapes.py


class ViewPyglet:
    def __init__(self):
        # configuration
        # furture acommodation for when the minimum point is not (0, 0)
        self.x_min = 0  # pixels, lower horizontal bound of view
        self.x_max = 800  # pixels, upper horizontal bound of view

        self.y_min = 0  # pixels, lower vertical bound of the view
        self.y_max = self.x_max  # pixels, upper vertical bound of the view

        x_mid = (
            self.x_max - self.x_min
        ) // 2 + self.x_min  # pixels, int, floor division
        y_mid = (
            self.y_max - self.y_min
        ) // 2 + self.y_min  # pixels, int, floor division

        self.steps_per_span = (
            10  # number of discrete points per span in either x or y direction
        )
        self.delta_x = (
            self.x_max - self.x_min
        ) // self.steps_per_span  # magnitude of x-direction step size
        self.delta_y = (
            self.y_max - self.y_min
        ) // self.steps_per_span  # magnitude of y-direction step size

        self.window = pyglet.window.Window(width=self.x_max, height=self.y_max)

        instructions_string = """
          Instructions:\n\n
          'r' refresh initial positions\n
          'q' quit demonstration\n\n
          'j' move agent down\n
          'k' move agent up\n\n
          'h' move agent left\n
          'l' move agent right
        """

        self.label = pyglet.text.Label(
            instructions_string,
            x=x_mid,
            y=y_mid,
            anchor_x="center",
            anchor_y="center",
            width=self.x_max // 4,
            multiline=True,
        )

        red = (255, 0, 0)
        green = (0, 255, 0)

        self.batch = pyglet.graphics.Batch()

        x0, y0 = self.intialize_position()
        self.agent = shapes.Rectangle(
            x=x0,
            y=y0,
            width=self.delta_x,
            height=self.delta_y,
            color=green,
            batch=self.batch,
        )
        self.agent.opacity = 100

        x0, y0 = self.intialize_position()  # updated initial draw of random positions
        self.landmark = shapes.Rectangle(
            x=x0,
            y=y0,
            width=self.delta_x,
            height=self.delta_y,
            color=red,
            batch=self.batch,
        )
        self.landmark.opacity = 100

    def intialize_position(self):
        # https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
        # Return random integers from the “discrete uniform” distribution of the specified
        # dtype in the “half-open” nterval [low, high).
        _x = randint(low=0, high=self.steps_per_span) * self.delta_x
        _y = randint(low=0, high=self.steps_per_span) * self.delta_y
        return (_x, _y)

    # @window.event
    # @self.window.event
    # @__class__.window.event
    # @pyglet.window.event
    # def on_draw(self):
    def draw(self):
        self.window.clear()
        self.label.draw()
        self.batch.draw()

    """
    @window.event
    def on_key_press(self, symbol, modifiers):

        print(f"Key {key.symbol_string(symbol)} was pressed.")

        if symbol == key.J:  # move up
            # enforce lower bounds prior to move attempt
            if self.agent.y - self.delta_y >= self.y_min:
                self.agent.y -= self.delta_y

        elif symbol == key.K:  # move up
            # enforce upper bounds prior to move attempt
            if self.agent.y + self.delta_y < self.y_max:
                self.agent.y += self.delta_y

        elif symbol == key.H:  # move left
            # enforce left side bounds prior to move attempt
            if self.agent.x - self.delta_x >= self.x_min:
                self.agent.x -= self.delta_x

        elif symbol == key.L:  # move right
            # enforce right side bounds prior to move attempt
            if self.agent.x + self.delta_x < self.x_max:
                self.agent.x += self.delta_x

        elif symbol == key.R:  # refresh the initial conditions
            # updated initial draw of random positions
            x0, y0 = self.intialize_position()
            self.agent.x = x0
            self.agent.y = y0

            # updated initial draw of random positions
            x0, y0 = self.intialize_position()
            self.landmark.x = x0
            self.landmark.y = y0

        elif symbol == key.Q:  # quit
            # close the figure, end the interactive demonstration
            # plt.close()
            self.window.close()
        """


def main():
    v = ViewPyglet()
    win = v.window

    @win.event
    def on_draw():
        v.draw()

    # sleep to allow user to actually see the window, otherwise it is torn down instantly
    # time.sleep(3)  # seconds
    pyglet.app.run()


if __name__ == "__main__":
    main()
