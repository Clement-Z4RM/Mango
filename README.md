# 🥭 Mango

## 🤔 What is Mango?

**Mango** is an improved and skinned [**C**](https://github.com/Epitech/coding-style-checker) and **Haskell** Epitech coding style checker.

> [!TIP]
> By default, **Mango** will ignore the files contained in your `.gitignore`.

> I decline all responsibility if you have a coding style error not detected by Mango (there is no reason for this to happen). 😉

#### How does it work?

**For C:**
> **Mango** uses the [Epitech coding style](https://github.com/Epitech/coding-style-checker) (that use the [Epitech banana coding style checker](https://github.com/Epitech/banana-coding-style-checker)).\
It executes the coding style checker on your files and then parses the output to display it in a more readable way.

**For Haskell:**
> **Mango** uses **lambdananas** and parses its output to display it in a more readable way.\
> The arguments that **Mango** uses for **lambdananas** are the current directory (`./`) and all `.hs` files in hidden directories.

**lambdananas** is only checking `.hs` files, but if you have another file(s) like `Makefike`, you should also use `mango` (without `-H` flag) to check them.

## 🔧 Installation

You must have these packages installed - if you are on the [official Epitech dump](https://github.com/Epitech/dump) you will have them by default:
 - [**Docker**](https://www.docker.com) ([install docker](https://docs.docker.com/engine/install))
 - [**Python 3**](https://www.python.org) ([install python](https://www.python.org/downloads))
 - [**wget**](https://www.gnu.org/software/wget) or [**curl**](https://curl.se/) (optional)

> [!WARNING]  
> If you have already an executable named `mango` in `/bin`, it will be replaced by this one.
>
> If you have an executable named `mango` in a folder other than `/bin`, it might take over. You can check this with `which mango` or `whereis mango` and delete it/them if so.

### With wget
```bash
sudo rm /bin/mango; sudo wget https://raw.githubusercontent.com/Clement-Z4RM/Mango/main/mango.py -O /bin/mango && sudo chmod +x /bin/mango
```
### With curl
```bash
sudo rm /bin/mango; sudo curl https://raw.githubusercontent.com/Clement-Z4RM/Mango/main/mango.py -o /bin/mango && sudo chmod +x /bin/mango
```
### Manually
 - Copy the content of [mango.py](https://raw.githubusercontent.com/Clement-Z4RM/Mango/main/mango.py) in `/bin/mango`
 - Execute this command:
```bash
sudo chmod +x /bin/mango
```
### For Haskell
To use **Mango** with **Haskell**, you can use it just like that, but it's better to have **lambdananas** (faster than **coding-style**) and maybe detect more errors.\
You can get it on the [intranet](https://intra.epitech.eu/file/Public/technical-documentations/Haskell/lambdananas.tar.gz).\
Don't forget to add it to your *PATH*.

## ⚙ Usage

**For C:**
```bash
mango
```

**For Haskell:**
```bash
mango -H
# I advise you to make an alias, like "mhango"
alias mhango="mango -H"
```

For a detailed usage, type:
```bash
mango -h, --help
```

## 📋 Arguments

`-H` `--haskell` `--lambdananas`\
Check coding style for **Haskell** (use **lambdananas** instead of **coding-style**). Some **Haskell** errors are detected by **coding-style**, but since Epitech uses **lambdananas**, it is better to use this flag for **Haskell**

`-i` `--ignore` `--gitignore`\
Don't ignore *.gitignore* content

`-l` `--list`\
List all errors (with descriptions)

`-Sl` `--short-list`\
List all errors (without descriptions)

`-s <error>` `--show <error>`\
Show description of an error

`-Ee <error(s)>` `-Eerrors <error(s)>` `--exclude-errors <error(s)>`\
Exclude error(s) from **Mango** report

`-Ef <file(s)>` `-Efiles <file(s)>` `--exclude-files <file(s)>`\
Exclude file(s) and folder(s) from **Mango** report

`-w <time>` `--watch <time>`\
Relaunch **Mango** every *time* seconds (warning, this will clear the terminal)

`-q` `--quiet`\
Don’t output anything, just set exit status

`-v` `--version`\
Print currently installed **Mango** version

`-u` `--update`\
Update **Mango** to the newest version (*not working at the moment, it will maybe re-introduced in a future version*)

## ➡ Examples

With this C file:
```c
#include <stdio.h>

int main()
{
    printf("Hello world!");
}
```

<br/>

```bash
> mango
```
```
main.c
MINOR C-G1: File header
C files and every Makefile must always start with the standard header of the school.

main.c at line 3
MAJOR C-F6: Functions without parameters
A function taking no parameters must take void as a parameter in the function declaration.

main.c at line 6
INFO C-A3: Line break at the end of file
Files must end with a line break.

1 Major | 1 Minor | 1 Info
```

<br/>

```bash
> mango -Ee C-F6
```
```
main.c
MINOR C-G1: File header
C files and every Makefile must always start with the standard header of the school.

main.c at line 6
INFO C-A3: Line break at the end of file
Files must end with a line break.

0 Major | 1 Minor | 1 Info | 1 excluded
```

<br/>

```bash
> mango -Ef main.c
```
```
✅ There is no coding style error

Be careful, you still have 3 excluded errors
```
You can also exclude an entire folder (e.g. `mango -Ef src/`).

## ❓ Support

For support, [open an issue](https://github.com/Clement-Z4RM/Mango/issues/new).

## ➕ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 👨‍⚖️ License

[GNU General Public](https://choosealicense.com/licenses/gpl-3.0)
