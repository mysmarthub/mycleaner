My cleaner
===

>A package of modules and CLI utility for destroying, zeroing, and deleting files.
> 
>Author and developer: Aleksandr Suvorov
> 
>BSD 3-Clause License

[![PyPI - Downloads](https://img.shields.io/pypi/dm/mycleaner?label=pypi%20downloads)](https://pypi.org/project/mycleaner/)
[![PyPI](https://img.shields.io/pypi/v/mycleaner)](https://pypi.org/project/mycleaner/)
[![PyPI - Format](https://img.shields.io/pypi/format/mycleaner)](https://pypi.org/project/mycleaner/)
[![GitHub repo size](https://img.shields.io/github/repo-size/mysmarthub/mycleaner)](https://github.com/mysmarthub/mycleaner/)
[![GitHub all releases](https://img.shields.io/github/downloads/mysmarthub/mycleaner/total?label=github%20downloads)](https://github.com/mysmarthub/mycleaner/)
[![GitHub](https://img.shields.io/github/license/mysmarthub/mycleaner?style=flat-square)](https://github.com/mysmarthub/mycleaner/)
[![GitHub Repo stars](https://img.shields.io/github/stars/mysmarthub/mycleaner?style=social)](https://github.com/mysmarthub/mycleaner)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/mycleaner)](https://github.com/mysmarthub/mycleaner/)


---
[![Download mycleaner](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/mycleaner-package/files/latest/download)
[![Download mycleaner](https://img.shields.io/sourceforge/dt/mycleaner-package.svg)](https://sourceforge.net/projects/mycleaner-package/files/latest/download)
---

![Mycleaner](https://github.com/mysmarthub/mycleaner/raw/master/images/my_cleaner_logo.png)

---

Help the project financially:
---
>[Yandex Money](https://yoomoney.ru/to/4100115206129186)

    Visa:    4048 4150 0400 5852

>[Paypal](https://paypal.me/myhackband)

---

What's new?
---
> The program code has been completely redesigned. 
> The interface has been completely changed, 
> bugs have been fixed, new features have been added, 
> and work has been accelerated.

---
Termux support:
---

> You can easily use the utility with Termux 
> on mobile phones and tablets.

    1. Download and install Termux https://play.google.com/store/apps/details?id=com.termux&hl=ru&gl=US
    2. pkg install python
    3. pip install mycleaner
    4. mycleaner --help
    5. To access the file storage: 
        termux-setup-storage
        cd ~/storage
    
    Files are destroyed even without root access and sudo.
    Read more about how to use the utility.
---
Description:
---
>A package of modules and console utilities for destroying, 
> zeroing, and deleting files.

>With this package, you can develop graphical, 
> console , and cross-platform applications to destroy, 
> reset data in a file, and delete files 
> so that they are difficult or impossible to recover. 
> 
>You can also use a ready-made console utility for destruction, 
> reset and delete files.
>
>The utility allows you to destruct files, 
> reset them to zero and delete them, 
> for complete or partial difficulty in 
> restoring them after deletion.
> 
> >Be careful! When adding folders, all files from all subfolders 
will be added recursively.
>

---
Help:
---
```text
Usage: mycleaner.py [OPTIONS]

  My Cleaner - CLI utility for destroying, zeroing, and deleting files.

Options:
  --paths, --p TEXT   Paths to a files or folder with files, all attached
                      files and folders will be taken into account! Be
                      extremely careful and attentive when adding.
                      
  --num, --n INTEGER  Number of overwrites. If you use the shred method, each
                      file will be overwritten the specified number of times
                      before being destroyed.
                      
  --dirs, --d         Delete the folders?
  
  --yes, --y          Auto Mode, be very careful with this parameter, if you
                      specify it, the program will start and start destroying
                      files automatically.
                      
  --shred             Overwrites random data, renames and deletes the file,
                      used by default.
                      
  --zero              Resets and does not delete the file.
  
  --del               Resets and deletes the file.
  
  --version, --v      Displays the version of the program and exits.
  
  --help              Show this message and exit.


```
---
Use:
---

>Package installation:

`pip install mycleaner`

`mycleaner --paths /path/ --paths /path2/ --num 100 --dirs --yes --shred`

>Git Clone:

`git clone https://github.com/mysmarthub/mycleaner.git`

`cd mycleaner`

`pip install -r requirements.txt`

`python mycleaner/mycleaner.py --paths /path/ --p /path2/ --n 100 --d --yes --shred`


---

>To delete some files, you may need administrator rights. 
To do this, install the package with the command:

`sudo pip install mycleaner`

`sudo mycleaner --paths /path/ --paths /path2/ --num 100 --dirs --yes --shred`

>or:

`git clone https://github.com/mysmarthub/mycleaner.git`

`cd mycleaner`

`sudo pip install -r requirements.txt`

`sudo python mycleaner/mycleaner.py --paths /path/ --p /path2/ --n 100 --d --yes --shred`

---
Links:
---
>[GitHub](https://github.com/mysmarthub/mycleaner)

>[PyPi](https://pypi.org/project/mycleaner/)
 
>[Sourceforge](https://sourceforge.net/projects/mycleaner-package/files/latest/download)
---

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
---
    Email: myhackband@yandex.ru
    Copyright © 2020-2021 Aleksandr Suvorov
