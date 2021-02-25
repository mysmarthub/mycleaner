# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE.txt for details)
# https://github.com/mysmarthub/
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""The smart module is used for working with paths, storing, receiving, adding, deleting."""
import os


def print_status(status):
    if status:
        print('[Successfully!]')
    else:
        print('[Error!]')


def get_count_dirs(path: str) -> int:
    """
    Counting the number of folder recursively nested in a directory

    :param path: <str> Path to the directory
    :return: <int> Counting the number of folders recursively nested in a directory
    """
    if os.path.isdir(path):
        return sum([len(folders) for _, folders, _ in os.walk(path)])
    else:
        return 0


def get_count_files(path: str) -> int:
    """
    Counting the number of files recursively nested in a directory

    :param path: <str> Path to the directory
    :return: <int> Counting the number of files recursively nested in a directory
    """
    if os.path.isfile(path):
        return 1
    elif os.path.isdir(path):
        return sum([len(files) for _, _, files in os.walk(path)])
    else:
        return 0


def get_files_gen(path):
    if path and os.path.exists(path):
        for p, _, files in os.walk(path):
            for f in files:
                yield os.path.join(p, f)


def get_folders_gen(path):
    if path and os.path.exists(path):
        for p, folders, _ in os.walk(path):
            for f in folders:
                yield os.path.join(p, f)


class PathObj:
    """Creates a path object for the file or folder"""

    @staticmethod
    def files_path_gen(path: str) -> iter:
        """
        Generator of paths to files recursively nested in a directory

        :param path: <str> Path to the directory
        :return: <generator> paths to files recursively nested in a directory
        """
        return (os.path.join(p, file) for p, _, files in os.walk(path) for file in files)

    @staticmethod
    def dirs_path_gen(path: str):
        """
        Generator of paths to folders recursively nested in a directory

        :param path: <str> Path to the directory
        :return: <generator> paths to folders recursively nested in a directory
        """
        return (os.path.join(p, d) for p, dirs, _ in os.walk(path) for d in dirs)

    @staticmethod
    def get_num_of_dirs(path: str):
        """
        Counting the number of folders recursively nested in a directory

        :param path: <str> Path to the directory
        :return: <int> Counting the number of folders recursively nested in a directory
        """
        return sum([len(dirs) for _, dirs, _ in os.walk(path)])

    @staticmethod
    def get_num_of_files(path):
        """
        Counting the number of files recursively nested in a directory

        :param path: <str> Path to the directory
        :return: <int> Counting the number of files recursively nested in a directory
        """
        return sum([len(files) for _, _, files in os.walk(path)])

    def __init__(self, path: str):
        """When creating an object, you must specify a path that is checked for existence."""
        self.__path = path

    @property
    def path(self):
        """Path to the file or folder"""
        return self.__path

    def get_files(self) -> iter:
        """Returns the file path generator"""
        if os.path.isfile(self.__path):
            return [self.__path]
        elif os.path.isdir(self.__path):
            return (os.path.join(p, file) for p, _, files in os.walk(self.__path) for file in files)
        else:
            return []

    def get_dirs(self) -> iter:
        """Returns the folder path generator"""
        if os.path.isdir(self.path):
            return self.dirs_path_gen(self.__path)
        return []

    @property
    def num_of_files(self):
        """Counting the number of files recursively nested in a directory"""
        return 1 if os.path.isfile(self.__path) else self.get_num_of_files(self.__path)

    @property
    def num_of_dirs(self):
        """Counting the number of dirs recursively nested in a directory"""
        return self.get_num_of_dirs(self.__path)

    def __str__(self):
        return f'PathObj({self.__path})'


class DataObj:

    def __init__(self):
        self.__objects = {}

    def get_obj_gen(self):
        return (obj for obj in self.__objects.values())

    def get_obj_dict(self):
        return self.__objects

    def add_path(self, path: str) -> bool:
        if os.path.exists(path) and not self.search_for_duplicates(path) and not os.path.islink(path):
            self.__objects[path] = PathObj(path)
            return True
        return False

    def search_for_duplicates(self, path: str) -> bool:
        """Checking for duplicates"""
        return True if path in self.__objects else False

    def del_path(self, path: str) -> bool:
        """Deleting a path object"""
        if self.search_for_duplicates(path):
            del self.__objects[path]
            return True
        return False

    def get_files(self) -> iter:
        """Returns a generator with file paths from all objects"""
        return (file for obj in self.__objects.values() for file in obj.get_files())

    def get_dirs(self) -> iter:
        """Getting folders"""
        return reversed(sorted(path for obj in self.__objects.values() for path in obj.get_dirs()))

    @property
    def is_any_data(self) -> bool:
        """Checking for data in repositories"""
        return True if self.__objects else False

    @property
    def count(self):
        return len(self.__objects)

    def clear_data(self) -> None:
        """Clearing storage"""
        self.__objects.clear()
