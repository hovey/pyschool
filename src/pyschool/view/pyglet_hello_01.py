import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label(
    "Hello, world",
    font_name="Times New Roman",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)


# An on_draw() event is dispatched to the window to give it a chance to redraw its
# contents.  A simple way to attach event handlers to objects is to use a decorator:
@window.event
def on_draw():
    window.clear()  # cleared to the default background color (black)
    label.draw()


# Enter pyglet's default event loop, and let pyglet respond to application events such
# as the mouse and keyboard.  The even handlers will now be called if/when required,
# and the run() method will return only when all the application windows have been
# closed.
pyglet.app.run()
