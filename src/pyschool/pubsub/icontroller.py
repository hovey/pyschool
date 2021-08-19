"""
Implements IController
"""

from abc import ABC, abstractmethod
from typing import List


class IController(ABC):
    """
    The Interface class for data controllers.

    Attributes:
        organs (list[str]): The list of organs read.
        write_loc (str): The parent directory to which the data will
            be written.
        read_loc (str): The parent directory from which the data will
            be read.
        _factory (ptm.factory.Factory): The factory class.
        _train_split (float): The percentage of examples to use for
            training.
        _val_split (float): The percentage of examples to use for
            validation.
        _test_split (float): The percentage of examples to use for
            test.
        _rs (int): The random seed used to seed random number
            generators.
        __filenames (List[str]): A list of paths to scan dicoms for
            all patients.
    """
    # def __init__(self,
    #              organs: List[str] = None,
    #              train_split: float = 0.7,
    #              val_split: float = 0.15,
    #              test_split: float = 0.15,
    #              write_loc: str = '/data/wg-p2m/ptm/data',
    #              read_loc: str = '/data/wg-p2m/IRCAD/3Dircadb1',
    #              random_seed: int = 42):
    def __init__(self):
        """
        The init method of the IController class

        Arguments:
            organs (List[str]): The list of organs read. Defaults to
                ['bone', 'skin']
            train_split (float): The percentage of examples to use for
                training. Defaults to 0.7.
            val_split (float): The percentage of examples to use for
                validation. Defaults to 0.15.
            test_split (float): The percentage of examples to use for
                test. Defaults to 0.15.
            write_loc (str): The parent directory to which the data
                will be written. Defaults to '/data/wg-p2m/ptm/data'.
            read_loc (str): The parent directory from which the data
                will be read. Defaults to '/data/wg-p2m/IRCAD/
                3Dircadb1'.
            random_seed (int): The random seed used to seed random
                number generators. Defaults to 42.
        """
        super().__init__()

    @abstractmethod
    def data(self):
        """
        Handles data reading and writing
        """
        pass
