# handling mouse and keyboard events
# https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html#handling-mouse-and-keyboard-events

# Full code at
# https://github.com/pyglet/pyglet/blob/pyglet-1.5-maintenance/examples/programming_guide/events.py

import pyglet
from pyglet.window import key
from pyglet.window import mouse


window = pyglet.window.Window()

# To react to keyboard and mouse event, write and attach event handlers.


# keyboard events have two parameters: the virtual key symbol that was pressed, and
# a bitwise combination of any modifiers that are pressed, such as the CTRL and
# SHIFT keys.
# Key symbols are defined in `pyglet.window.key`
@window.event
def on_key_press(symbol, modifiers):

    if symbol == key.H:  # in the future, will map this to move left
        print("The 'h' key was pressed.")

    elif symbol == key.L:  # to map to move right
        print("The 'l' key was pressed.")

    elif symbol == key.J:  # to map to move down
        print("The 'j' key was pressed.")

    elif symbol == key.K:  # to map to move up
        print("The 'k' key was pressed.")

    else:
        print("Some key other than 'h', 'j', 'k', 'l' was pressed.")


@window.event
def on_mouse_press(x, y, button, modifiers):
    # the `x` and `y` are the position of the mouse, relative to the lower-left
    # corner of the window, when the button was pressed
    if button == mouse.LEFT:
        print(f"The left mouse button was pressed with x={x}, and y={y}")


@window.event
def on_draw():
    window.clear()


# There are more than 20 event types that can be handled on a window.  To find
# the event names and paramteters:
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)
# which will cause all events received on the window to be printed to the console.
# This is super cool to show the event loop!

# Excerpt from the console upon run:

# on_text(text='r')
# on_key_press(symbol=R, modifiers=)
# Some key other than 'h', 'j', 'k', 'l' was pressed.
# on_draw()
# on_key_release(symbol=R, modifiers=)
# on_draw()

# on_text(text='q')
# on_key_press(symbol=Q, modifiers=)
# Some key other than 'h', 'j', 'k', 'l' was pressed.
# on_draw()
# on_key_release(symbol=Q, modifiers=)
# on_draw()

# on_text(text='w')
# on_key_press(symbol=W, modifiers=)
# Some key other than 'h', 'j', 'k', 'l' was pressed.
# on_draw()
# on_key_release(symbol=W, modifiers=)
# on_draw()

# on_text(text='j')
# on_key_press(symbol=J, modifiers=)
# The 'j' key was pressed.
# on_draw()
# on_key_release(symbol=J, modifiers=)
# on_draw()

# on_deactivate()
# on_draw()
# on_activate()
# on_draw()

# on_mouse_enter(x=460, y=175)
# on_draw()
# on_mouse_motion(x=458, y=178, dx=0, dy=3)
# on_draw()
# on_mouse_motion(x=456, y=182, dx=-2, dy=3)
# on_draw()
# on_mouse_motion(x=452, y=189, dx=-4, dy=7)
# on_draw()
# on_mouse_leave(x=120, y=485)
# on_draw()
# on_deactivate()
# on_draw()


pyglet.app.run()
