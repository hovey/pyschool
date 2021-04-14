# minimum working example of decorating with a class method
from time import sleep
from pyglet.window import Window


class View:
    _window: Window = Window()

    # def __init__(self, size: int = 800):
    def __init__(self, size: int = 1000):
        # View._window.set_size(width=size, height=size)
        self.__class__._window.set_size(width=size, height=0.5 * size)

    @_window.event
    def on_draw():
        pass


if __name__ == "__main__":
    view = View()
    sleep(2)
