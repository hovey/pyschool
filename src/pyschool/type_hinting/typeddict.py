"""Experiments with type hinting."""

from typing import TypedDict, Union


class BaseConfig(TypedDict):
    """foo (int): Foo docstring."""

    foo: int


class BarConfig(BaseConfig):
    """bar (str): Bar docstring."""

    bar: str


class BazConfig(BaseConfig):
    """baz (bool): Baz docstring."""

    baz: bool


ClientConfig = Union[BarConfig, BazConfig]


class Foo:
    """Base class doc.

    Attributes:
        foo (int): Foo docstring

    Keyword Arguments:
        config (BaseConfig): The base config.
    """

    def __init__(self, *, config: BaseConfig):
        self.foo = config["foo"]


class Bar(Foo):
    """Bar concretion doc.

    Attributes:
        bar (str): Bar docstring.

    Keyword Arguments:
        config (BarConfig): The bar config.
    """

    def __init__(self, *, config: BarConfig):
        super().__init__(config=config)

        self.bar = config["bar"]


class Baz(Foo):
    """Baz concretion doc.

    Attributes:
        bar (bool): Baz docstring.

    Keyword Arguments:
        config (BazConfig): The baz config.
    """

    def __init__(self, *, config: BazConfig):
        super().__init__(config=config)

        self.baz = config["baz"]


if __name__ == "__main__":
    client_config: ClientConfig = {
        "foo": 0,
        "bar": "a",
        # "baz": "a",
    }
