# agent_landmark_pyglet.py
from numpy.random import randint

import pyglet
from pyglet.window import key
from pyglet import shapes

# references:
# double-buffing and tearing
# https://pyglet.readthedocs.io/en/latest/programming_guide/windowing.html#double-buffering
# /pyglet/examples/graphics/shapes.py

# configuration
# furture acommodation for when the minimum point is not (0, 0)
x_min = 0  # pixels, lower horizontal bound of view
x_max = 800  # pixels, upper horizontal bound of view

y_min = 0  # pixels, lower vertical bound of the view
y_max = x_max  # pixels, upper vertical bound of the view

x_mid = (x_max - x_min) // 2 + x_min  # pixels, int, floor division
y_mid = (y_max - y_min) // 2 + y_min  # pixels, int, floor division

steps_per_span = 10  # number of discrete points per span in either x or y direction
delta_x = (x_max - x_min) // steps_per_span  # magnitude of x-direction step size
delta_y = (y_max - y_min) // steps_per_span  # magnitude of y-direction step size

window = pyglet.window.Window(width=x_max, height=y_max)


def intialize_position():
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
    # Return random integers from the “discrete uniform” distribution of the specified
    # dtype in the “half-open” nterval [low, high).
    _x = randint(low=0, high=steps_per_span) * delta_x
    _y = randint(low=0, high=steps_per_span) * delta_y
    return (_x, _y)


instructions_string = """
  Instructions:\n\n
  'r' refresh initial positions\n
  'q' quit demonstration\n\n
  'j' move agent down\n
  'k' move agent up\n\n
  'h' move agent left\n
  'l' move agent right
  """

label = pyglet.text.Label(
    instructions_string,
    x=x_mid,
    y=y_mid,
    anchor_x="center",
    anchor_y="center",
    width=x_max // 4,
    multiline=True,
)

red = (255, 0, 0)
green = (0, 255, 0)

batch = pyglet.graphics.Batch()

x0, y0 = intialize_position()
agent = shapes.Rectangle(
    x=x0,
    y=y0,
    width=delta_x,
    height=delta_y,
    color=green,
    batch=batch,
)
agent.opacity = 100

x0, y0 = intialize_position()  # updated initial draw of random positions
landmark = shapes.Rectangle(
    x=x0,
    y=y0,
    width=delta_x,
    height=delta_y,
    color=red,
    batch=batch,
)
landmark.opacity = 100


@window.event
def on_draw():
    window.clear()
    label.draw()
    batch.draw()


@window.event
def on_key_press(symbol, modifiers):

    print(f"Key {key.symbol_string(symbol)} was pressed.")

    if symbol == key.J:  # move up
        # enforce lower bounds prior to move attempt
        if agent.y - delta_y >= y_min:
            agent.y -= delta_y

    elif symbol == key.K:  # move up
        # enforce upper bounds prior to move attempt
        if agent.y + delta_y < y_max:
            agent.y += delta_y

    elif symbol == key.H:  # move left
        # enforce left side bounds prior to move attempt
        if agent.x - delta_x >= x_min:
            agent.x -= delta_x

    elif symbol == key.L:  # move right
        # enforce right side bounds prior to move attempt
        if agent.x + delta_x < x_max:
            agent.x += delta_x

    elif symbol == key.R:  # refresh the initial conditions
        x0, y0 = intialize_position()  # updated initial draw of random positions
        agent.x = x0
        agent.y = y0

        x0, y0 = intialize_position()  # updated initial draw of random positions
        landmark.x = x0
        landmark.y = y0

    elif symbol == key.Q:  # quit
        # close the figure, end the interactive demonstration
        # plt.close()
        window.close()


pyglet.app.run()
