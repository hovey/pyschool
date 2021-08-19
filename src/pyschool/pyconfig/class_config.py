"""This config uses a config class to specify settable parameters."""


class Config:
    """A config class.

    Attributes:
        string_key (str): string key
        ...
    """

    def __init__(self):
        self.string_key = "string value"
        self.int_key = 42
        self.bool_key = True
        self.person = {
            "name": "Jason Smith",
            "age": 26,
            "hobbies": ["hockey", "cooking", "quilting"],
        }


config = Config()
