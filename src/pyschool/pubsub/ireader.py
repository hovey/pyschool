"""
Implements IReader
"""

from abc import ABC, abstractmethod

import numpy as np


class IReader(ABC):
    """
    The Interface class for readers.

    Attributes:
        file_path (str): The path to the file containing the data.
        # _data (np.ndarray): The data read from the file.
        _data (dict or np.ndarray): The data read from the file.
    """

    def __init__(self, file_path: str):
        """
        The init method of the IReader class.

        Arguments:
            file_path (str): The path to the file to read.
        """
        super().__init__()

    @property
    @abstractmethod
    # def data(self) -> np.ndarray:
    def data(self):
        """
        Reads the file if not already read. Else returns it.

        Returns:
            # self._data (np.ndarray): The data read from the file.
            self._data (dict or np.ndarray): The data read from the file.

        Raises:
            NotImplementedError: If _read_data has not been
                implemented in the child class.
            FileNotFoundError: If the provided file_path does not
                exist.
            dicom.errors.InvalidDicomError: If the provided file_path
                does not contain a valid dicom file.
        """
        pass
