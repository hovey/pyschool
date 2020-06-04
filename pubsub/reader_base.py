"""
Implements ReaderBase
"""

import numpy as np

# from ptm.data.reader import IReader
# from pyschool.pubsub import IReader
from pubsub.ireader import IReader

class ReaderBase(IReader):
    """
    The Base class for readers.

    Attributes:
        file_path (str): The path to the file containing the data.
        # _data (np.ndarray): The data read from the file.
        _data (dict or np.ndarray): The data read from the file.
    """
    def __init__(self,
                 file_path: str):
        """
        The init method of the ReaderBase class.

        Arguments:
            file_path (str): The path to the file to be read.
        """
        super().__init__(file_path=file_path)

        self.file_path = file_path
        self._data = None

    @property
    def data(self) -> np.ndarray:
        """
        Reads the file if not already read. Else returns it.

        Returns:
            self._data (np.ndarray): The data read from the file.

        Raises:
            NotImplementedError: If _read_data has not been
                implemented in the child class.
            FileNotFoundError: If the provided file_path does not
                exist.
            dicom.errors.InvalidDicomError: If the provided file_path
                does not contain a valid dicom file.
        """
        if self._data is None:
            # self._data = self._read_data()  # <-- avoid passing back the data, just set the data
            self._read_data()

        return self._data  # <-- now data can be passed back to the client

    # def _read_data(self) -> np.ndarray:
    def _read_data(self):
        """
        Reads the data from the specified file path.

        Returns:
            # data (np.ndarray): The data read from the file.
            no return

        Raises:
            NotImplementedError: If _read_data has not been
                implemented in the child class.
            FileNotFoundError: If the provided file_path does not
                exist.
            dicom.errors.InvalidDicomError: If the provided file_path
                does not contain a valid dicom file.
        """
        raise NotImplementedError
