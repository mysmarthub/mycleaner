#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details)
# https://github.com/mysmarthub
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""
Module for destruction, zeroing, and deleting files.

Used to create applications for destruction, zeroing, and deleting files.
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


class Cleaner:
    """
    Creates an object for working with file and folder paths

    for further destruction, zeroing, deleting files. Delete a folder.
    """
    def __init__(self, shreds=30):
        """Accepts an optional parameter when creating an object shred:

        the number of passes to overwrite the file. By default, 30 passes.
        """
        self.errors = []
        self.shreds = shreds
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

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
        :return: <bool> The logical status of the operation of zeroing the file
        """
        try:
            with open(file, 'wb') as f:
                f.write(bytes(0))
        except OSError:
            self.errors.append(f'Zeroing error: {file}')
            return False
        else:
            self.count_zero_files += 1
            return True

    def shred_file(self, file: str) -> bool:
        """Overwrites and deletes the file at the specified path
        :param file: <str> Path to the file
        :return: <bool> The logical status of the operation of destruction the file
        """
        rep_path = self.replace_path(file)
        if os.name == 'posix':
            status = os.system(f'shred -zvuf -n {self.shreds} {rep_path}')
            if status:
                self.errors.append(f'Do not shred, os error: {file}')
                return False
            else:
                self.count_del_files += 1
                return True
        else:
            self.del_file(file)

    def del_file(self, file: str) -> bool:
        """Deletes the file at the specified path using normal deletion

        :param file: <str> Path to the file
        :return: <bool> The logical status of the operation of deletes the file
        """
        try:
            if os.path.islink(file):
                os.unlink(file)
            else:
                self.zero_file(file)
                os.remove(file)
        except OSError:
            self.errors.append(f'Os error! Do not delete: {file}')
            return False
        if self.check_exist(file):
            self.errors.append(f'Do not delete: {file}')
            return False
        else:
            self.count_del_files += 1
            return True

    def del_dir(self, path: str) -> bool:
        """Deletes an empty folder at the specified path

        :param path: <str> Path to the directory
        :return: The logical status of the operation of deletes the folder
        """
        try:
            if os.path.islink(path):
                os.unlink(path)
            else:
                os.rmdir(path)
        except OSError:
            self.errors.append(f'Os error! Do not delete: {path}')
            return False
        else:
            if self.check_exist(path):
                self.errors.append(f'Do not delete: {path}')
                return False
            else:
                self.count_del_dirs += 1
                return True

    def reset_count(self) -> None:
        """Resetting counters"""
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

    def reset_error_list(self):
        """Resetting error list"""
        self.errors.clear()


if __name__ == '__main__':
    try:
        from sfd import sfd
    except ModuleNotFoundError:
        print('Error!!!')
        print('The sfd (Smart Files Destroyer) package is not installed)!')
        print('To install, use the command: pip install sfd')
        print('Or pip install -r requirements.txt')
    else:
        sfd.cli()
