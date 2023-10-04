# 🥭 Mango

Mango is an improved and skinned Epitech Banana coding style checker.

I decline all responsibility if you have a coding style error not detected by Mango. 😉

## 🔧 Installation

You must have these packages installed - if you are on the [official Epitech dump](https://github.com/Epitech/dump) you will have them by default:
 - [**Docker**](https://www.docker.com) ([install docker](https://docs.docker.com/engine/install))
 - [**Python 3**](https://www.python.org) ([install python](https://www.python.org/downloads))
 - [**wget**](https://www.gnu.org/software/wget) or [**curl**](https://curl.se/) (optional)
### With wget
```bash
sudo wget https://raw.githubusercontent.com/Clement-Z4RM/Mango/main/mango.py -O /bin/mango && sudo chmod +x /bin/mango
```
### With curl
```bash
sudo curl https://raw.githubusercontent.com/Clement-Z4RM/Mango/main/mango.py -o /bin/mango && sudo chmod +x /bin/mango
```
### Manually
 - Copy the content of [mango.py](https://raw.githubusercontent.com/Clement-Z4RM/Mango/main/mango.py) in */bin/mango*
 - Execute this command:
```bash
sudo chmod +x /bin/mango
```

## ⚙ Usage

```bash
mango
```

For a detailed usage, type:
```bash
mango -h, --help
```

If you want to exclude the files contained in your *.gitignore*, type:
```bash
mango -Ef $(cat .gitignore)
```
<sub>"-Ef" can be replaced by "-Efiles" or "--exclude-files"</sub>

## 📋 Arguments

`-Ee <error(s)>`; `-Eerrors <error(s)>`; `--exclude-errors <error(s)>`: exclude error(s) from **Mango** report
<br/>
`-Ef <file(s)>`; `-Efiles <file(s)>`; `--exclude-files <file(s)>`: exclude file(s)/folder(s) from **Mango** report
<br/>
`-w <time>`; `--watch <time>`: relaunch **Mango** every *time* seconds (warning, this will clear the terminal)
<br/>
`-v`; `--version`: print currently installed **Mango** version
<br/>
`-u`; `--update`: update **Mango** to the newest version (*not working at the moment, it will be re-introduced in a future version*)

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
>$ mango
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
>$ mango --exclude-errors C-F6
```
```
main.c
MINOR C-G1: File header
C files and every Makefile must always start with the standard header of the school.

main.c at line 6
INFO C-A3: Line break at the end of file
Files must end with a line break.

1 Major | 1 Minor | 1 Info
```

<br/>

```bash
>$ mango --exclude-files main.c
```
```
✅ There is no coding style error
```
You can also exclude an entire folder (e.g. *mango --exclude-files src/*).

## Support

For support, [open an issue](https://github.com/Clement-Z4RM/Mango/issues/new).

## ➕ Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## 👨‍⚖️ License

[GNU General Public](https://choosealicense.com/licenses/gpl-3.0)
