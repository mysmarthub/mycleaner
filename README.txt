My cleaner
==========
A package of modules and CLI utility for destroying,
zeroing, and deleting files.
Author and developer: Aleksandr Suvorov
BSD 3-Clause License

Help the project financially:
=============================
https://yoomoney.ru/to/4100115206129186
Visa:    4048 4150 0400 5852
https://paypal.me/myhackband

What's new?
===========
The program code has been completely redesigned.
The interface has been completely changed,
bugs have been fixed, new features have been added,
and work has been accelerated.

Termux support:
===============

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
============
A package of modules and console utilities for destroying,
zeroing, and deleting files.

With this package, you can develop graphical,
console , and cross-platform applications to destroy,
reset data in a file, and delete files
so that they are difficult or impossible to recover.

You can also use a ready-made console utility for destruction,
reset and delete files.

The utility allows you to destruct files,
reset them to zero and delete them,
for complete or partial difficulty in
restoring them after deletion.

Be careful! When adding folders, all files from all subfolders
will be added recursively.

Help:
=====

Usage: mycleaner.py [OPTIONS] [PATHS]...

  My Cleaner - CLI utility for destroying, zeroing, and deleting files.

  PATHS - these are the paths to files and folders with files separated by a
  space, if there are spaces in the path name, escape them, or put them in
  quotation marks.

  - Console utility for destruction, zeroing, and deleting files.

  - The utility allows you to destruct files, reset them to zero and delete
  them, for complete or partial difficulty in restoring them after deletion.

  - Be careful! When adding folders, all files from all subfolders will be
  added recursively.

  -Use:
    mycleaner /path1 /path2 /pathN/file.file --shred -n 30 -dd -y

  https://github.com/mysmarthub/mycleaner mysmarthub@ya.ru

Options:
  -v, --version      Displays the version of the program and exits.
  -y, --yes          Auto Mode, be very careful with this parameter, if you
                     specify it, the program will start and start destroying
                     files automatically.

  -n, --num INTEGER  Number of overwrites. If you use the shred method, each
                     file will be overwritten the specified number of times
                     before being destroyed.

  -s, --shred        Overwrites random data, renames and deletes the file,
                     used by default.

  -z, --zero         Resets and does not delete the file.
  -d, --del          Resets and deletes the file.
  -t, --test         The test method, files and folders will remain unchanged.
  -dd, --del-dirs    Delete the folders?
  --help             Show this message and exit.

Use:
====

Package installation:
---------------------
    `pip install mycleaner`

To create applications:
-----------------------
    from mycleaner import smart, cleaner

Launch and use the ready-made utility:
--------------------------------------
    - After installation, you can run the utility using its name.
        mycleaner

    - See the help page to understand how to work with the utility

    - After the name, specify the paths to files and folders separated by a space,
        on some systems if the path contains spaces or others
        forbidden characters, and the system itself does not escape such a path,
        either escape such a path or enclose it in quotation marks.
        mycleaner /path1 /path2 /pathN/file.file

    - Next, you should specify the method for the utility to work. At the moment
        there are 4 methods available: --shred, --zero, --del, --test.
    --shred: [destroy] - overwrites and deletes the file.
    --zero: [zeroing] - completely destroys the information inside the file,
        but does not delete the file.
    --del: [delete] - First applies [zeroing], then deletes the file.
    --test: [test] - Running the program in test mode, no
        files or folders will not be deleted
    mycleaner /path1 /path2 /pathN/file.file --shred

    - When using the method --shred ([destroy])
        you can specify the number of file overwrites
        using the parameter --num 100 или -n 100,
        with any number separated by a space.
    mycleaner /path1 /path2 /pathN/file.file --shred -n 30

    - To delete empty folders after work, use the parameter --del-dirs или -dd

    - You can also run the utility in automatic execution mode
        (for example, use it to start and run at a certain time
        using the task scheduler). To do this, you should send an additional message
        the --yes or-y parameter. Be careful using this parameter,
        after all, the utility will start working automatically.

        To start automatically, you must pass all the necessary parameters:
            be sure the existing path, and the method (if you do not pass default
            [destroy] is triggered, and the --yes or-y parameter is used.
            The parameters -dd and --num can be used as desired.
        mycleaner /path1 /path2 /pathN/file.file --shred -n 30 -dd -y

Git Clone:
----------

git clone https://github.com/mysmarthub/mycleaner.git
cd mycleaner
pip install -r requirements.txt
python mycleaner/mycleaner.py /path1 /path2 /pathN/file.file --shred -n 30 -dd


To delete some files, you may need administrator rights.
To do this, install the package with the command:

sudo pip install mycleaner
sudo mycleaner /path1 /path2 /pathN/file.file --shred -n 30 -dd

or:

git clone https://github.com/mysmarthub/mycleaner.git
cd mycleaner
sudo pip install -r requirements.txt
sudo python mycleaner/mycleaner.py /path1 /path2 /pathN/file.file --shred -n 30 -dd

Links:
======
https://github.com/mysmarthub/mycleaner
https://pypi.org/project/mycleaner
https://sourceforge.net/projects/mycleaner-package/files/latest/download

Disclaimer of liability:
========================
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

Support:
========
    Email: mysmarthub@ya.ru
    Copyright © 2020-2021 Aleksandr Suvorov
