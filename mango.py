#!/usr/bin/env python3

from sys import argv, stderr
from os import ttyname, system, path, walk
from argparse import ArgumentParser as parseArgs
from shutil import which
from requests import get
from time import sleep

version = "v1.7.0"

mango_ascii = """                                                      \33[48;5;130m \33[48;5;094m  \33[0m
                               \33[48;5;166m                   \33[0m   \33[48;5;166m \33[48;5;130m \33[48;5;094m \33[0m
                           \33[48;5;202m          \33[48;5;166m                \33[48;5;058m      \33[0m
                        \33[48;5;208m        \33[48;5;202m         \33[48;5;166m          \33[48;5;064m   \33[48;5;058m         \33[0m
                      \33[48;5;208m               \33[48;5;202m      \33[48;5;166m       \33[48;5;106m  \33[48;5;064m   \33[48;5;058m          \33[0m
                    \33[48;5;208m                     \33[48;5;202m   \33[48;5;166m      \33[48;5;106m    \33[48;5;064m   \33[48;5;058m         \33[0m
                   \33[48;5;214m      \33[48;5;215m     \33[48;5;214m \33[48;5;208m            \33[48;5;202m \33[48;5;166m     \33[48;5;142m \33[48;5;106m     \33[48;5;064m   \33[48;5;058m         \33[0m
                 \33[48;5;214m    \33[48;5;215m          \33[48;5;214m  \33[48;5;208m           \33[48;5;172m  \33[48;5;166m   \33[48;5;172m \33[48;5;106m      \33[48;5;064m  \33[48;5;058m          \33[0m
                \33[48;5;214m    \33[48;5;215m  \33[48;5;221m  \33[48;5;222m   \33[48;5;221m \33[48;5;215m    \33[48;5;214m  \33[48;5;208m         \33[48;5;172m   \33[48;5;166m    \33[48;5;112m  \33[48;5;106m     \33[48;5;064m  \33[48;5;058m         \33[0m
               \33[48;5;214m    \33[48;5;221m   \33[48;5;222m     \33[48;5;221m  \33[48;5;215m  \33[48;5;214m     \33[48;5;208m      \33[48;5;172m     \33[48;5;166m   \33[48;5;142m \33[48;5;112m \33[48;5;106m     \33[48;5;064m   \33[48;5;058m        \33[0m
              \33[48;5;214m  \33[48;5;220m \33[48;5;220m \33[48;5;221m    \33[48;5;222m    \33[48;5;221m   \33[48;5;215m \33[48;5;214m        \33[48;5;208m    \33[48;5;172m     \33[48;5;166m    \33[48;5;112m  \33[48;5;106m     \33[48;5;064m  \33[48;5;058m        \33[0m
            \33[48;5;214m    \33[48;5;220m \33[48;5;220m \33[48;5;221m          \33[48;5;214m          \33[48;5;208m  \33[48;5;172m       \33[48;5;166m  \33[48;5;130m    \33[48;5;106m     \33[48;5;064m  \33[48;5;058m        \33[0m
          \33[48;5/\33[48;5;214m      \33[48;5;220m \33[48;5;220m \33[48;5;220m \33[48;5;221m     \33[48;5;220m \33[48;5;220m \33[48;5;220m \33[48;5;214m         \33[48;5;178m  \33[48;5;172m        \33[48;5;166m \33[48;5;130m      \33[48;5;136m \33[48;5;106m   \33[48;5;064m   \33[48;5;058m       \33[0m
         \33[48;5;178m       \33[48;5;214m                  \33[48;5;178m     \33[48;5;172m       \33[48;5;136m \33[48;5;130m        \33[48;5;094m  \33[48;5;106m \33[48;5;064m   \33[48;5;058m       \33[0m
       \33[48;5;178m                \33[48;5;214m      \33[48;5;178m \33[48;5;214m \33[48;5;178m       \33[48;5;172m      \33[48;5;136m  \33[48;5;130m       \33[48;5;094m      \33[0m   \33[48;5;058m       \33[0m
      \33[48;5;142m  \33[48;5;178m                            \33[48;5;172m      \33[48;5;136m   \33[48;5;130m      \33[48;5;094m      \33[0m          \33[48;5;058m  \33[0m
    \33[48;5;136m  \33[48;5;142m         \33[48;5;178m                   \33[48;5;172m    \33[48;5;136m     \33[48;5;130m     \33[48;5;094m       \33[0m
    \33[48;5;136m         \33[48;5;142m      \33[48;5;178m           \33[48;5;172m     \33[48;5;136m       \33[48;5;130m    \33[48;5;094m       \33[0m
    \33[48;5;100m       \33[48;5;136m                             \33[48;5;130m   \33[48;5;094m       \33[0m
     \33[48;5;003m    \33[48;5;100m      \33[48;5;136m                       \33[48;5;130m  \33[48;5;094m      \33[48;5#\33[0m
       \33[48;5;003m      \33[48;5;100m     \33[48;5;136m                \33[48;5;130m  \33[48;5;094m      \33[0m
          \33[48;5;003m       \33[48;5;100m      \33[48;5;136m \33[3 \33[3 \33[3 \33[48;5;130m   \33[48;5;094m      \33[0m\n\n"""

mango_tty = "    Sad TTY not handle well colors :(\n"\
"                                                        %\n"\
"                                                      (#%\n"\
"                               (((((((((((((######   (#%\n"\
"                           ((((((((((((((((((((######%%%%%%\n"\
"                        (//((((((((((((((((((((((####%%%%%%%%%%\n"\
"                      /////////////(((((((((((((((####%%%%%%%%%%%\n"\
"                    //////////////////((((((((((((((####%%%%%%%%%%\n"\
"                  %/////******///////////((((((((((((####%%%%%%%%%%\n"\
"                 ///******,*****//////////((((((((((((####%%%%%%%%%&\n"\
"                //****,,,,,,,***///////////((((((((((((###%%%%%%%%%%\n"\
"               /****,,,,..,,,***///////////(((((((((((((###%%%%%%%%&\n"\
"             %*****,,,,,,,,,****///////////(((((((((((((###%%%%%%%%&\n"\
"            ////****,,,,,,****////////////((((((((###(((####%%%%%%%%\n"\
"          ///////************////////////((((((((######(####%%%%%%%%\n"\
"        %//////////******///////////////((((((((########%###%%%%%%%%\n"\
"       ///////////////////////////////(((((((((#######%%%%   %%%%%%%&\n"\
"     ((((////////////////////////////((((((((########%%%%          %%\n"\
"    ((((((((((((//////////////////(((((((((########%%%%\n"\
"    (((((((((((((((((((////(/((((((((((((########%%%%\n"\
"    #######(((((((((((((((((((((((((((#########%%%\n"\
"     ##########(((((((((((((((((((##########%%#\n"\
"      %###############(((((##############%\n"\
"          #########################(\n\n"

types = [" INFO", " MINOR", " MAJOR"]

colors = ["\33[36m", "\33[33m", "\33[31m"]

rules = ["C-O1", "C-O3", "C-O4", "C-G1", "C-G2", "C-G3", "C-G4", "C-G5", "C-G6", "C-G7", "C-G8", "C-F2", "C-F3", "C-F4", "C-F5", "C-F6", "C-F8", "C-F9", "C-L2", "C-L3", "C-L4", "C-V1", "C-C1", "C-C3", "C-H1", "C-H2", "C-A3"]

descriptions = [
    ["Contents of the repository\33[0m", "The repository must not contain compiled, temporary or unnecessary files."],
    ["File coherence\33[0m", "A source file mustn't contain more than 5 functions."],
    ["Naming files and folders\33[0m", "All files names and folders must be in English, according the \33[3msnake_case\33[0m convention."],
    ["File header\33[0m", "C files and every Makefile must always start with the standard header of the school."],
    ["Separation of functions\33[0m", "Inside a source file, implementations of functions must be separated by one and only one empty line."],
    ["Indentation of reprocessor directives\33[0m", "The preprocessor directives must be indented according to the level of indirection."],
    ["Global variables\33[0m", "Global variables must be avoided as much as possible. Only global constants should be used."],
    ["\33[3minclude\33[0m", "\33[3minclude\33[0m directive must only include C header files."],
    ["Line endings\33[0m", "Line endings must be done in UNIX style (with \33[3m\\n\33[0m)."],
    ["Trailing spaces\33[0m", "No trailing spaces must be present at the end of a line."],
    ["Leading/trailing lines\33[0m", "No leading empty lines must be present. No more than 1 trailing empty line must be present."],
    ["Naming functions\33[0m", "The name of a function must define the task it executes and must contain a verb. All function names must be in English, according to the \33[3msnake_case\33[0m convention."],
    ["Number of columns\33[0m", "The length of a line must not exceed 80 columns."],
    ["Number of lines\33[0m", "The body of a function should be as short as possible, and must not exceed 20 lines."],
    ["Number of parameters\33[0m", "A function must not have more than 4 parameters."],
    ["Functions without parameters\33[0m", "A function taking no parameters must take void as a parameter in the function declaration."],
    ["Comments inside a function\33[0m", "There must be no comment within a function."],
    ["Nested functions\33[0m", "Nested functions are not allowed."],
    ["Indentation\33[0m", "Each indentation level must be done by using 4 spaces. No tabulations may be used for indentation."],
    ["Spaces\33[0m", "When using a space as a separator, one and only one space character must be used."],
    ["Curly brackets\33[0m", "Opening curly brackets must be at the end of the line, after the content it precedes, except for functions definitions where they must be placed alone on their line. Closing curly brackets must be alone on their line, except in the case of \33[3melse\33[0m/\33[3melse if\33[0m control structures, \33[3menum\33[0m declarations, or structure declarations."],
    ["Naming identifiers\33[0m", "All identifier names must be in English, according to the \33[3msnake_case\33[0m convention. The type names defined with \33[3mtypedef\33[0m must end with \33[3m_t\33[0m. The names of macros and global constants and the content of enums must be written in \33[3mUPPER_SNAKE_CASE\33[0m."],
    ["Conditional branching\33[0m", "A conditionnal block must not contain more than 3 branches."],
    ["\33[3mgoto\33[0m", "Using the \33[3mgoto\33[0m keyword if forbidden."],
    ["Content\33[0m", "Header files must only contain \33[1mfunctions prototypes\33[0m, \33[1mtypes declarations\33[0m, \33[1mglobal variable/constant declarations\33[0m, \33[1mmacros\33[0m, \33[1mstatic inline functions\33[0m. All these elements must only be found in header files, and thus not in source files."],
    ["Include guard\33[0m", "Headers must be protected from double inclusion."],
    ["Line break at the end of file\33[0m", "Files must end with a line break."]
]

def set_arguments():
    parser = parseArgs()
    parser.add_argument("-Ee", "-Eerrors", "--exclude-errors", nargs = '+', help = "Exclude coding style errors from report")
    parser.add_argument("-Ef", "-Efiles", "--exclude-files", nargs = '+', help = "Exclude files from coding style checking")
    parser.add_argument("-w", "--watch", nargs = 1, help = "Watch for changes in the repository every x seconds")
    parser.add_argument("-v", "--version", action = "store_true", help = "Show Mango version")
    parser.add_argument("-u", "--update", action = "store_true", help = "Update Mango to last version")
    return parser.parse_args()

def download_coding_style():
    print("Downloading coding-style...\n")
    system(f"sudo wget https://raw.githubusercontent.com/Clement-Z4RM/coding-style-checker/main/coding-style.sh -O /bin/coding-style 2> /dev/null && sudo chmod +x /bin/coding-style")

def check_for_update(args):
    try:
        response = get("https://api.github.com/repos/Clement-Z4RM/Mango/releases/latest")
        if (response):
            new_version = response.json()["name"]
        if (not args.update and new_version != version):
            print("New version of Mango available. You can update it doing \"\33[3mmango -u, --update\33[0m\".\n")
    except:
        if (args.update):
            print("Cannot get latest version, please verify your internet connection.\n", file=stderr)
        else:
            print("Cannot check for update, please verify your internet connection.\n", file=stderr)

def update():
    system("sudo wget https://raw.githubusercontent.com/Clement-Z4RM/Mango/main/mango.py -O /bin/mango 2> /dev/null && sudo chmod +x /bin/mango")
    system("curl -s https://pastebin.com/raw/baCbaUqU")
    exit()

def print_version():
    print(f"Mango {version}")
    exit()

def get_exclude_files(args):
    exclude = []
    if (not args.exclude_files):
        return exclude
    for file in args.exclude_files:
        if (path.isdir(file)):
            for root, subdirs, files in walk(file):
                for filename in files:
                    file = path.join(root, filename)
                    file = path.abspath(file)
                    exclude.append(file.strip())
        else:
            file = path.abspath(file)
            exclude.append(file.strip())
    return exclude

def get_exclude_errors(args):
    exclude = []
    if (not args.exclude_errors):
        return exclude
    for error in args.exclude_errors:
        exclude.append(error.strip())
    return exclude

def coding_style():
    system("sudo rm -f /tmp/coding-style-reports.log")
    system("coding-style . /tmp/ > /dev/null")
    try:
        with open("/tmp/coding-style-reports.log", "r") as file:
            out = file.read()
            file.close()
    except:
        print(f"{argv[0]}: Cannot open log file.", file=stderr)
        exit(84)
    out = out.split('\n')
    return out

def print_error(line, index):
    color = ("\33[0m" + colors[types.index(line[2])])
    print(f"{color}\33[1m{line[0]}", end = '')
    if (int(line[1]) > 1):
        print(f" at line {line[1]}", end = '')
    print(f"\n{line[2][1:]} {line[3]}: {color}{descriptions[index][0]}\n{descriptions[index][1]}\n")

def print_errors_number(err_nb):
    if (err_nb[2] > 0 or err_nb[1] > 0 or err_nb[0] or err_nb[3] > 0):
        print(f"\33[1;31m{err_nb[2]} Major\33[0m | \33[1;33m{err_nb[1]} Minor\33[0m | \33[1;36m{err_nb[0]} Info\33[0m", end = '')
        if (err_nb[3] > 0):
            print(f" | \33[1;37m{err_nb[3]} Unknown\33[0m", end = '')
        if (err_nb[4] > 0):
            print(f" | \33[1;37m{err_nb[4]} excluded\33[0m", end = '')
        print()
    elif (not is_a_tty):
        print(f"{mango_ascii}    ✅ There is no coding style error")
        if (err_nb[4] > 0):
            print(f"\nBe careful, you still have {err_nb[4]} excluded errors")
    else:
        print(f"{mango_tty}    but you have no coding style error :)")
        if (err_nb[4] > 0):
            print(f"\nBe careful, you still have {err_nb[4]} excluded errors")

def mango(exclude_files, exclude_errors, watch):
    out = coding_style()
    if (watch):
        system("clear")
    err_nb = [0, 0, 0, 0, 0]
    if (not out):
        if (not is_a_tty):
            print(f"{mango_ascii}    ✅ There is no coding style error")
        else:
            print(f"{mango_tty}    but you have no coding style error :)")
        return
    for line in out:
        backup_line = line
        if (line == ''):
            continue
        line = line.split(':')
        if (path.abspath(line[0]) in exclude_files or line[3] in exclude_errors):
            err_nb[4] += 1
            continue
        try:
            index = rules.index(line[3])
        except:
            print(f"{backup_line}\n")
            err_nb[3] += 1
            continue
        if (line[0][0:2] == "./"):
            line[0] = line[0][2:]
        match line[2]:
            case " INFO":
                err_nb[0] += 1
            case " MINOR":
                err_nb[1] += 1
            case " MAJOR":
                err_nb[2] += 1
        print_error(line, index)
    print_errors_number(err_nb)

def main():
    args = set_arguments()
    if (args.version):
        print_version()
    check_for_update(args)
    if (args.update):
        update()
    if (which("coding-style") is None):
        download_coding_style()
    if (args.watch):
        while (True):
            try:
                mango(get_exclude_files(args), get_exclude_errors(args), args.watch)
                sleep(int(args.watch[0]))
            except KeyboardInterrupt:
                exit()
            except:
                exit(84)
    else:
        mango(get_exclude_files(args), get_exclude_errors(args), args.watch)

if __name__ == "__main__":
    is_a_tty = ttyname(1).split('/')[-1].startswith("tty")
    main()
