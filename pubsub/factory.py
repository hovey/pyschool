"""
Implements Factory
"""

from importlib import import_module
from typing import Callable

from pubsub.ipublisher import IPublisher
from pubsub.isubscriber import ISubscriber

class Factory:
    """
    Provides a constructor of various classes.
    """
    def __init__(self, build_specification):
        """
        The init method of the Factory class.
        """
        _reader_interface = self.reader_factory(mode='json')
        _reader = _reader_interface(build_specification)

        _objects = []  # empty roster of objects, fill is a value Object is created
        for item in _reader.data:
            class_kwargs = _reader.data[item]
            module_name = class_kwargs.get("module", None)
            if module_name is not None:
                module_dict = dict(name=f'.{module_name}', package='pubsub')
                try: 
                    the_module = import_module(**module_dict)
                    try:
                        the_class = getattr(the_module, module_name.capitalize())
                        if the_class:
                            _objects.append(the_class(**class_kwargs))
                    except AttributeError:
                        print(f'Skipping module {the_module.__name__}; class {module_name.capitalize()} not found.')
                except ModuleNotFoundError:
                    print(f'Skipping module {module_dict["package"] + module_dict["name"]}; module not found.')

        # connect the publish-subscribe mechanism
        subscribers = [item for item in _objects if isinstance(item, ISubscriber)]
        for item in subscribers: 
            print(f'{item.name} has an ISubscriber interface')

        publishers = [item for item in _objects if isinstance(item, IPublisher)]
        for item in publishers: 
            print(f'{item.name} has an IPublisher interface')
            for who in subscribers:
                item.connect(who)

        for item in publishers:
            print(f'{item.name} responds to a command and pubishes:')
            item.publish()

    @staticmethod
    def reader_factory(mode: str = 'json') -> Callable:
        """
        Imports the correct reader class.

        Arguments:
            mode (str): The type of reader to import. Defaults to
                'json'.

        Returns:
            class_constructor (pubsub.reader.IReader): The reader
                class contructor.

        Raises:
            ModuleNotFoundError: If the requested reader does not
                exist.
        """
        module_dict = dict(name=f'.{mode}.reader', package='pubsub')
        module = import_module(**module_dict)
        class_constructor = getattr(module, 'Reader')

        return class_constructor
