"""
Reference: https://refactoring.guru/design-patterns/decorator/python/example

This example is creating a basic app and then using decorators to add functionality to it.

Decorator Design Pattern != Python decorators. See
https://stackoverflow.com/questions/8328824/what-is-the-difference-between-python-decorators-and-the-decorator-pattern
"""

from abc import abstractmethod


class App:
    """Basic app"""

    def __init__(self):
        pass

    def __call__(self, **kwargs):
        return "Basic app"


class AppDecorator(App):
    """App decorator base class"""
    _app: App = None

    def __init__(self, app: App):
        self._app = app

    @property
    def app(self):
        return self._app

    @abstractmethod
    def __call__(self, **kwargs):
        pass


class AppHomeScreen(AppDecorator):

    """Adds home screen to app"""
    def __call__(self, **kwargs):
        return self.app(**kwargs) + kwargs.get("home", " home page")


class AppLoginPage(AppDecorator):

    """Adds login page to app"""
    def __call__(self, **kwargs):
        return self.app(**kwargs) + kwargs.get("login", " login page")


if __name__ == "__main__":
    app = App()
    # Basic app
    print(app())

    home_screen_app = AppHomeScreen(app)
    # Basic app with a home screen
    print(home_screen_app(home=" with a home screen"))

    login_app = AppLoginPage(home_screen_app)
    # Basic app with a home screen and a login page
    print(login_app(home=" with a home screen", login=" and a login page"))
