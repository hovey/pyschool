import pyglet

# Refacotor to include Image viewer lesson:
# https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html#image-viewer
#
# code:
# https://github.com/pyglet/pyglet/blob/pyglet-1.5-maintenance/examples/programming_guide/image_viewer.py
# examples/programming_guide/image_viewer.py.

window = pyglet.window.Window()

image = pyglet.resource.image("pyglet_kitten.jpg")


# An on_draw() event is dispatched to the window to give it a chance to redraw its
# contents.  A simple way to attach event handlers to objects is to use a decorator:
@window.event
def on_draw():
    window.clear()  # cleared to the default background color (black)
    image.blit(0, 0)  # draw image at pixel coordinates (0, 0), the lower left corner


# Enter pyglet's default event loop, and let pyglet respond to application events such
# as the mouse and keyboard.  The even handlers will now be called if/when required,
# and the run() method will return only when all the application windows have been
# closed.
pyglet.app.run()
