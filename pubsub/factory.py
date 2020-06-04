"""
Implements Factory
"""

from importlib import import_module
from typing import Callable


class Factory:
    """
    Provides a constructor of various classes.
    """
    def __init__(self):
        """
        The init method of the Factory class.
        """
        pass

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
        class_constructor = getattr(module, 'Reader')

        return class_constructor

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
