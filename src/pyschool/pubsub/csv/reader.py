"""
Implements json.Reader
"""

import numpy as np

from pubsub.reader_base import ReaderBase


class Reader(ReaderBase):
    """
    A reader for json data.

    Attributes:
        file_path (str): The path to the file containing the data.
        _data (dict): The data read from the file.
    """

    def __init__(self, file_path: str):
        """
        The init method of the csv.Reader class.

        Arguments:
            file_path (str): The path to the file to be read.
        """
        super().__init__(file_path=file_path)

    def _read_data(self) -> np.ndarray:
        """
        Reads the data from the specified file path.

        Raises:
            NotImplementedError: If _read_data has not been
                implemented in the child class.
            FileNotFoundError: If the provided file_path does not
                exist.
            dicom.errors.InvalidDicomError: If the provided file_path
                does not contain a valid dicom file.
        """
        # Read the data from the file
        with open(self.file_path) as fin:
            self._data = np.genfromtxt(fin, dtype=float, comments="#", delimiter=",")

        # return data  # <-- no need to return, just set member data
