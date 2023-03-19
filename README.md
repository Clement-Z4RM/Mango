# 🥭 Mango

Mango is an improved and skinned Epitech Banana coding style checker.

## 🔧 Installation

You need to have [**Docker**](https://www.docker.com/) installed: [install docker](https://docs.docker.com/engine/install/).
```bash
sudo wget https://raw.githubusercontent.com/Clement-Lnrd/Mango/main/mango.py -O /bin/mango && sudo chmod +x /bin/mango
```

## ⚙ Usage

```bash
mango
```

For a detailed usage, type:
```bash
mango -h, --help
```

If you want to excludes the files contained in your *.gitignore*, type:
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
`-u`; `--update`: update **Mango** to newest version

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
main.c:1: C-G1
File header
C files and every Makefile must always start with the standard header of the school.

main.c:3: C-F6
Functions without parameters
A function taking no parameters must take void as a parameter in the function declaration.

main.c:6: C-A3
Line break at the end of file
Files must end with a line break.

1 Major | 1 Minor | 1 Info
```

<br/>

```bash
>$ mango --exclude-errors C-F6
```
```
main.c:1: C-G1
File header
C files and every Makefile must always start with the standard header of the school.

main.c:6: C-A3
Line break at the end of file
Files must end with a line break.

0 Major | 1 Minor | 1 Info
```

<br/>

```bash
>$ mango --exclude-files main.c
```
```
✅ There isn't coding style error
```
You can also exclude an entire folder (e.g. *mango --exclude-files src/*).

## ➕ Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## 👨‍⚖️ License

[GNU General Public](https://choosealicense.com/licenses/gpl-3.0/)
