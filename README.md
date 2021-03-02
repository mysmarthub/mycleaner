My cleaner
===
---
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/mycleaner)](https://github.com/mysmarthub/mycleaner/)
[![Python](https://img.shields.io/static/v1?label=Python&message=3.6/3.7/3.8/3.9&color=yellow)](https://python.org)
[![GitHub](https://img.shields.io/github/license/mysmarthub/mycleaner?style=flat-square)](https://github.com/mysmarthub/mycleaner/)
---
>A package of modules, and CLI utility for shredding, erasing, and deleting files.
> 
>Author and developer: Aleksandr Suvorov
> 
>BSD 3-Clause License

---
[![PyPI - Downloads](https://img.shields.io/pypi/dm/mycleaner?label=pypi%20downloads)](https://pypi.org/project/mycleaner/)
[![PyPI](https://img.shields.io/pypi/v/mycleaner)](https://pypi.org/project/mycleaner/)
[![PyPI - Format](https://img.shields.io/pypi/format/mycleaner)](https://pypi.org/project/mycleaner/)

[![GitHub Repo stars](https://img.shields.io/github/stars/mysmarthub/mycleaner?style=social)](https://github.com/mysmarthub/mycleaner/)
[![GitHub forks](https://img.shields.io/github/forks/mysmarthub/mycleaner?style=social)](https://github.com/mysmarthub/mycleaner/)
[![GitHub watchers](https://img.shields.io/github/watchers/mysmarthub/mycleaner?style=social)](https://github.com/mysmarthub/mycleaner/)

[![Donate](https://img.shields.io/static/v1?label=donate&message=paypal&color=green)](https://paypal.me/myhackband)
[![Donate](https://img.shields.io/static/v1?label=donate&message=yandex&color=yellow)](https://yoomoney.ru/to/4100115206129186)

---
My Cleaner + Windows version download

[![Download mycleaner](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/mycleaner-package/files/latest/download)
[![Download mycleaner](https://img.shields.io/sourceforge/dt/mycleaner-package.svg)](https://sourceforge.net/projects/mycleaner-package/files/latest/download)
---

![Mycleaner](https://github.com/mysmarthub/mycleaner/raw/master/images/my_cleaner_logo.png)

---

Help the project financially:
---
>https://yoomoney.ru/to/4100115206129186

    Visa:    4048 0250 0089 5923

>https://paypal.me/myhackband

---
Warninig!
---

> You can see information about earlier versions on the release page:
> https://github.com/mysmarthub/mycleaner/releases.

---
What's new?
-----------
Bugs fixed, new classes added.

---------------
Termux support:
---------------

You can easily use the utility with Termux
on mobile phones and tablets.

    1. Install Termux
    2. pkg install python
    3. pip install mycleaner
    4. mycleaner --help
    5. To access the file storage:
        termux-setup-storage
        cd ~/storage

    Files are destroyed even without root access and sudo.
    Read more about how to use the utility.

------------
Description:
------------
A package of modules and console utilities for shredding,
erasing, and deleting files.

With this package, you can develop graphical,
console , and cross-platform applications to shredding,
erasing , and deleting files
so that they are difficult or impossible to recover.

You can also use a ready-made console utility for destruction,
reset and delete files - mycleaner.py

The utility allows you to shred files,
erase files, for complete or partial difficulty
their recovery after removal.

Be careful! When adding folders, all files from all subfolders
will be added recursively.

We recommend that you run the program on Linux, mount the disks,
and work with them, because then you will have access to
the destroy method with the function of overwriting files.

-----
Help:
-----

    Usage: mycleaner.py [OPTIONS] COMMAND [ARGS]...

      My Cleaner - CLI utility for shredding, erasing, and deleting files.

      [ARGS]... - Paths to files and/or folders with files cli.py -y -dd
      shred /path/ /path2/ /pathN/file.file

      mycleaner.py -y -dd shred /path/ /path2/ /pathN/file.file -n 100
      mycleaner.py -y -dd erase /path/ /path2/ /pathN/file.file
      mycleaner.py -y -dd delete /path/ /path2/ /pathN/file.file

    Options:
      -v, --version    Displays the version of the program and exits.
      -y, --yes        Auto Mode
      -dd, --del-dirs  Delete the folders?
      --help           Show this message and exit.

    Commands:
      delete  Deleting files
      erase   Erasing files
      shred   Shredding files

----
Use:
----

Package installation:
---------------------
    `pip install mycleaner`

To create applications:
-----------------------
    from mycleaner import smart, cleaner

--------------------------------------
Launch and use the ready-made utility:
--------------------------------------
    - After installation, you can run the utility using its name.
        mycleaner --help

    - See the help page to understand how to work with the utility

      mycleaner.py -y -dd shred /path/ /path2/ /pathN/file.file -n 100
      mycleaner.py -y -dd erase /path/ /path2/ /pathN/file.file
      mycleaner.py -y -dd delete /path/ /path2/ /pathN/file.file

    - To delete empty folders after work, use the parameter --del-dirs или -dd

    - You can also run the utility in automatic execution mode
        (for example, use it to start and run at a certain time
        using the task scheduler). To do this, you should send an additional message
        the --yes or -y parameter. Be careful using this parameter,
        after all, the utility will start working automatically.


To delete some files, you may need administrator rights.
To do this, install the package with the command:

`sudo pip install mycleaner`

`sudo mycleaner -y -dd shred /path/ /path2/ /pathN/file.file -n 100`

`sudo mycleaner -y -dd erase /path/ /path2/ /pathN/file.file`

`sudo mycleaner -y -dd delete /path/ /path2/ /pathN/file.file`

Links:
------
https://github.com/mysmarthub/mycleaner

https://pypi.org/project/mycleaner

https://sourceforge.net/projects/mycleaner-package/files/latest/download

------------------------
Disclaimer of liability:
------------------------
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

-------------
Requirements:
-------------

[Click](https://github.com/pallets/click) by [license](https://github.com/pallets/click/blob/master/LICENSE.rst)

Python 3+ : https://python.org

--------
Support:
--------
    Email: mysmarthub@ya.ru
    Copyright © 2020 Aleksandr Suvorov
    
    -----------------------------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details)
    https://github.com/mysmarthub
    Copyright © 2020-2021 Aleksandr Suvorov
    -----------------------------------------------------------------------------
