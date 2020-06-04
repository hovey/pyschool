"""
Implements Factory
"""

from importlib import import_module
from typing import Callable

# from pubsub.command import Command
# from pubsub.ireader import IReader

class Factory:
    """
    Provides a constructor of various classes.
    """
    def __init__(self, command_file):
        """
        The init method of the Factory class.
        """
        # pass
        # _reader = _reader_type(config_file)
        # _data = _reader.data
        _reader_interface = self.reader_factory(mode='json')
        _reader = _reader_interface(command_file)
        # _commands = _reader.data
        # self._command_guids = []  # empty roster of commands, fill if a valid Command is created

        # for item in _commands:
        #     command_kwargs = _commands[item]
        #     i = Command(item, **command_kwargs)
        #     if i:
        #         self._command_guids.append(item)
        #     else:
        #         print(f'Skipping command {i}, no valid Command implementation.')

        _objects = []  # empty roster of objects, fill is a value Object is created
        for item in _reader.data:
            class_name = _reader.data[item]["class"]
            module_dict = dict(name=f'.{class_name}', package='pubsub')
            try: 
                # the_module = import_module(name=f'.{class_name}', package='pubsub')
                the_module = import_module(**module_dict)
                try:
                    the_class = getattr(the_module, class_name.capitalize())
                    if the_class:
                        _objects.append(the_class)
                except AttributeError:
                    print(f'Skipping module {the_module.__name__}; class {class_name.capitalize()} not found.')
            except ModuleNotFoundError:
                a = 4
                print(f'Skipping module {module_dict["package"] + module_dict["name"]}; module not found.')


    @staticmethod
    # def reader_factory(mode: str = 'dicom') -> Callable:
    def reader_factory(mode: str = 'json') -> Callable:
        """
        Imports the correct reader class.

        Arguments:
            mode (str): The type of reader to import. Defaults to
                # 'dicom'.
                'json'.

        Returns:
            # class_constructor (ptm.data.reader.IReader): The reader
            class_constructor (pubsub.reader.IReader): The reader
                class contructor.

        Raises:
            ModuleNotFoundError: If the requested reader does not
                exist.
        """
        # module = import_module(name=f'.{mode}',
        #                        package='ptm.data.reader')
        # module = import_module(name=f'.{mode}',
        #                        package='pubsub')
        module = import_module(name=f'.{mode}.reader',
                               package='pubsub')
        # module = import_module(name=f'{mode}.reader',
        #                        package='pubsub')
        class_constructor = getattr(module, 'Reader')

        return class_constructor

    @property
    def items(self):
        """
        Returns:
            The array of strings of guids created from client commands.

        Raises:
            To be determined.  
        """
        return self._command_guids



    # @staticmethod
    # def writer_factory(mode: str = 'numpy') -> Callable:
    #     """
    #     Imports the correct writer class.

    #     Arguments:
    #         mode (str): The type of writer to import. Defaults to
    #             'numpy'.

    #     Returns:
    #         class_constructor (ptm.data.reader.IWriter): The writer
    #             class contructor.

    #     Raises:
    #         ModuleNotFoundError: If the requested writer does not
    #             exist.
    #     """
    #     module = import_module(name=f'.{mode}',
    #                            package='ptm.data.writer')
    #     class_constructor = getattr(module, 'Writer')

    #     return class_constructor

    # @staticmethod
    # def example_factory(mode: str = 'train') -> Callable:
    #     """
    #     Imports the correct example class.

    #     Arguments:
    #         mode (str): The type of writer to import. Defaults to
    #             'train'.

    #     Returns:
    #         class_constructor (ptm.example.IExample): The example
    #             class contructor.

    #     Raises:
    #         ModuleNotFoundError: If the requested writer does not
    #             exist.
    #     """
    #     module = import_module(name=f'.{mode}',
    #                            package='ptm.example')
    #     class_constructor = getattr(module, 'Example')

    #     return class_constructor
