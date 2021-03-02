My cleaner
==========
A package of modules and CLI utility for shredding,
erasing, and deleting files.

Author and developer:
---------------------
Aleksandr Suvorov
BSD 3-Clause License

Help the project financially:
-----------------------------
https://yoomoney.ru/to/4100115206129186
Visa:    4048 0250 0089 5923
https://paypal.me/myhackband

What's new?
-----------
Bugs fixed, new classes added.


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


Use:
----

Package installation:
---------------------
    `pip install mycleaner`

To create applications:
-----------------------
    from mycleaner import smart, cleaner

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

sudo pip install mycleaner

sudo mycleaner -y -dd shred /path/ /path2/ /pathN/file.file -n 100
sudo mycleaner -y -dd erase /path/ /path2/ /pathN/file.file
sudo mycleaner -y -dd delete /path/ /path2/ /pathN/file.file

Links:
------
https://github.com/mysmarthub/mycleaner
https://pypi.org/project/mycleaner
https://sourceforge.net/projects/mycleaner-package/files/latest/download

Disclaimer of liability:
------------------------
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

Support:
--------
    Email: mysmarthub@ya.ru
    Copyright © 2020-2021 Aleksandr Suvorov
