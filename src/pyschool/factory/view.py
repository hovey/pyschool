"""
This module defines the View object for our shapes.
"""

from importlib import import_module

class View:
    """
    The View class creates and stores the models

    Attributes:
        _models ([model_base.Shape]): The shapes managed by the View
    """
    def __init__(self,
                 config=None):
        """
        The init method of the View class

        Args:
            config (dict): The config for the models
        """
        if config is None:
            config = {}

        self._models = self._create_models(config)

    @staticmethod
    def _create_models(config):
        """
        This method creates the models

        Args:
            config (dict): The config parameters of the shapes.

        Returns:
            models ([model_base.Shape]): A list of the created models
        """
        models = []
        for k, v in config.items():
            model_module = import_module(f'{k}.model')
            model_class = getattr(model_module, 'Model')
            models.append(model_class(**v))

        return models

    def area(self):
        """
        This method prints out the areas of all shapes
        """
        for model in self._models:
            print(f"The area of {model._shape_params['name']} is {model.area()}")
