"""
Implements Controller
"""

import os
from typing import List, Dict
from pathlib import Path

# from sklearn.model_selection import train_test_split

# from ptm.data.controller import IController
# from ptm.factory import Factory
# from icontroller import IController
from pubsub.icontroller import IController


class Controller(IController):
    """
    Handles examples and writers for setting up the dataset.

    Attributes:
        organs (list[str]): The list of organs read.
        write_loc (str): The parent directory to which the data will
            be written.
        read_loc (str): The parent directory from which the data will
            be read.
        read_mode (str): The type of data file to be read.
        write_mode (str): The type of file to which to write.
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

    def __init__(
        self,
        organs: List[str] = None,
        train_split: float = 0.7,
        val_split: float = 0.15,
        test_split: float = 0.15,
        write_loc: str = "/data/wg-p2m/ptm/data",
        read_loc: str = "/data/wg-p2m/IRCAD/3Dircadb1",
        random_seed: int = 42,
        read_mode: str = "dicom",
        write_mode: str = "numpy",
    ):
        """
        The init method of the Controller class

        Arguments:
            organs (list[str]): The list of organs read. Defaults to
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
            read_mode (str): The type of data file to be read.
                Defaults to 'dicom'.
            write_mode (str): The type of file to which to write.
                Defaults to 'numpy'.
        """
        super().__init__(
            organs=organs,
            train_split=train_split,
            val_split=val_split,
            test_split=test_split,
            write_loc=write_loc,
            read_loc=read_loc,
            random_seed=random_seed,
        )
        # read_mode=read_mode)

        # Set values of mutable arguments
        if not organs:
            organs = ["bone", "skin"]

        # Set class attributes
        self._factory = Factory()
        self.organs = organs
        self._train_split = train_split
        self._val_split = val_split
        self._test_split = test_split
        self.write_loc = write_loc
        self.read_loc = read_loc
        self.__filenames = None
        self._rs = random_seed
        self.read_mode = read_mode
        self.write_mode = write_mode

    def data(self):
        """
        Handles data reading and writing
        """
        # Make the directories to which the data will be written
        self._make_dirs()

        # Split the filenames into train, test, val
        dsets = self.datasets

        # Loop over dsets, saving fnames to the path.
        for path, fnames in dsets.items():
            self._write(path=path, filenames=fnames)

    @property
    def datasets(self) -> Dict[str, List[str]]:
        """
        Splits self._filenames into train, test, val sets.

        Returns:
            dsets (Dict[str, List[str]]): A dictionary mapping
                the write location to a list of paths to files to
                be read.
        """
        # Split train, test, val sets
        test_size = self._test_split / (
            self._train_split + self._val_split + self._test_split
        )
        val_size = self._val_split / (self._train_split + self._val_split)

        f_tv, fnames_test = train_test_split(
            self._filenames, test_size=test_size, random_state=self._rs
        )
        fnames_train, fnames_val = train_test_split(
            f_tv, test_size=val_size, random_state=self._rs
        )

        # Get paths to storage directories and set up dictionary
        dsets = {
            os.path.join(self.write_loc, "train"): fnames_train,
            os.path.join(self.write_loc, "validation"): fnames_val,
            os.path.join(self.write_loc, "test"): fnames_test,
        }

        return dsets

    @property
    def _filenames(self) -> List[str]:
        """
        Compiles a list of files to be read and returns it.

        Returns:
            self.__filenames (List[str]): A list of paths to scan
                dicoms for all patients.
        """
        # Search through the directory tree looking for directories
        # matching 3Dircadb1.*
        if not self.__filenames:
            filenames = []
            for path in Path(self.read_loc).rglob("3Dircadb1.*"):
                if not path.is_dir():
                    continue

                # Get the files in the directory
                path = os.path.join(path, "PATIENT_DICOM")
                filenames.extend(
                    [os.path.join(path, fname) for fname in os.listdir(path)]
                )

            self.__filenames = filenames

        return self.__filenames

    def _make_dirs(self):
        """
        Creates the directories to which the data will be written.
        """
        datasets = ["train", "test", "validation"]
        data_types = ["scans", "masks"]
        for dset in datasets:
            for dtype in data_types:
                # Make the directory. If it exists, delete it and
                # recreate it. Else, just create it.
                path = os.path.join(self.write_loc, dset, dtype)
                if os.path.exists(path):
                    self._rmdir(path=path)
                os.makedirs(path)

    def _rmdir(self, path: str):
        """
        Recursively removes a directory and its contents.

        Arguments:
            path (str): The path to the parent directory to be deleted.
        """
        directory = Path(path)
        for item in directory.iterdir():
            if item.is_dir():
                self._rmdir(item)
            else:
                item.unlink()
        directory.rmdir()

    def _write(self, path: str, filenames: List[str]):
        """
        Writes the masks and scans to the provided path.

        Arguments:
            path (str): The path to the parent directory to which to
                write the data.
            filenames (List[str]): A list of paths to the files to be
                read.
        """
        # Create a writer constructor
        writer_constructor = self._factory.writer_factory(mode=self.writer_mode)
