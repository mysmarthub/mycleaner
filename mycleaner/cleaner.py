# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE.txt for details)
# https://github.com/mysmarthub/mycleaner/
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""
Module for destruction, erasing, and deleting files.

Used to create applications for destruction, erasing, and deleting files.
Delete a folder. After being reset or destroyed, file recovery is impossible or
extremely difficult.
To destroy it, use the utility shred.

The cleaner module is used to destroy files,
reset them, and delete them.
Also for deleting folders.
It has counters and collects and stores information
about errors in the course of its work.
"""
import os
import shlex


class Shredder:
    def shred(self, file, rew=30, verbose=False):
        file = shlex.quote(file)
        command = f'shred {"-zvuf" if verbose else "-zuf"} -n {abs(rew)} {file}'
        status = os.system(command)
        if not status:
            return True
        return False


class Eraser:
    def __init__(self):
        self.count_zero_files = 0

    def erase(self, file):
        try:
            with open(file, 'wb') as f:
                f.write(bytes(0))
        except OSError:
            return False
        self.count_zero_files += 1
        return True


class FileDeleter:
    def __init__(self):
        self.count_del_files = 0

    def file_delete(self, file):
        try:
            os.remove(file)
        except (OSError, FileExistsError, FileNotFoundError):
            return False
        self.count_del_files += 1
        return True


class FolderDeleter:
    def __init__(self):
        self.count_del_dirs = 0

    def folder_delete(self, folder):
        try:
            os.rmdir(folder)
        except (OSError, FileExistsError, FileNotFoundError):
            return False
        self.count_del_dirs += 1
        return True


class LinkDeleter:
    def __init__(self):
        self.count_delete_link = 0

    def link_delete(self, link):
        try:
            os.unlink(link)
        except (OSError, FileExistsError, FileNotFoundError):
            return False

        self.count_delete_link += 0
        return True


class Remover(FileDeleter, FolderDeleter, LinkDeleter):
    def delete(self, path):
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                os.rmdir(path)
            else:
                os.unlink(path)
        except (OSError, FileExistsError, FileNotFoundError):
            return False
        return True


class Cleaner(Shredder, Eraser, FileDeleter, LinkDeleter, FolderDeleter):
    """
    Creates an object for working with file and folder paths

    for further destruction, erasing, deleting files. Delete a folder.
    """
    def __init__(self, shreds=30):
        """Accepts an optional parameter when creating an object shred:

        the number of passes to overwrite the file. By default, 30 passes.
        """
        Shredder.__init__(self)
        Eraser.__init__(self)
        FileDeleter.__init__(self)
        LinkDeleter.__init__(self)
        FolderDeleter.__init__(self)
        self.errors = []
        self.shreds = shreds

    @staticmethod
    def replace_path(path: str) -> str:
        """
        Solving the problem with spaces in the path in Linux

        :param path: <str> Path to the file or directory
        :return: <str> Corrected path
        """
        return shlex.quote(path)

    @staticmethod
    def check_exist(path):
        if os.path.exists(path):
            return True
        return False

    def zero_file(self, file: str) -> bool:
        """
        Resets the file

        :param file: <str> Path to the file
        :return: <bool> The logical status of the operation of erasing the file
        """
        status = self.erase(file)
        if not status:
            self.errors.append(f'erasing error: {file}')
        return status

    def shred_file(self, file: str, verbose=True) -> bool:
        """Overwrites and deletes the file at the specified path
        :param verbose: <bool> Show complete progress
        :param file: <str> Path to the file
        :return: <bool> The logical status of the operation of destruction the file
        """
        if os.name == 'posix':
            status = self.shred(file=file, rew=self.shreds, verbose=verbose)
            if not status:
                self.errors.append(f'Do not shred, os error: {file}')
        else:
            status = self.del_file(file)
        return status

    def del_file(self, file: str) -> bool:
        """Deletes the file at the specified path using normal deletion

        :param file: <str> Path to the file
        :return: <bool> The logical status of the operation of deletes the file
        """
        if os.path.isfile(file):
            status = self.file_delete(file)
        elif os.path.islink(file):
            status = self.link_delete(file)
        else:
            status = False
        if not status:
            self.errors.append(f'Os error! Do not delete: {file}')
            return False
        return True

    def del_dir(self, path: str) -> bool:
        """Deletes an empty folder at the specified path

        :param path: <str> Path to the directory
        :return: The logical status of the operation of deletes the folder
        """
        status = self.folder_delete(path)
        if not status:
            self.errors.append(f'Os error! Do not delete: {path}')
            return False
        return True

    def reset_count(self) -> None:
        """Resetting counters"""
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

    def reset_error_list(self):
        """Resetting error list"""
        self.errors.clear()
