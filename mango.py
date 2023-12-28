#!/usr/bin/env python3

import sys
from sys import argv, stderr
from os import ttyname, system, path, walk, remove
from argparse import ArgumentParser as parseArgs
from shutil import which
from time import sleep

VERSION = "v1.8.1"

CODING_STYLE_URL = "https://raw.githubusercontent.com/Epitech/coding-style-checker/main/coding-style.sh"

MANGO_ASCII = """                                                      \33[48;5;130m \33[48;5;094m  \33[0m
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
          \33[48;5;214m      \33[48;5;220m \33[48;5;220m \33[48;5;220m \33[48;5;221m     \33[48;5;220m \33[48;5;220m \33[48;5;220m \33[48;5;214m         \33[48;5;178m  \33[48;5;172m        \33[48;5;166m \33[48;5;130m      \33[48;5;136m \33[48;5;106m   \33[48;5;064m   \33[48;5;058m       \33[0m
         \33[48;5;178m       \33[48;5;214m                  \33[48;5;178m     \33[48;5;172m       \33[48;5;136m \33[48;5;130m        \33[48;5;094m  \33[48;5;106m \33[48;5;064m   \33[48;5;058m       \33[0m
       \33[48;5;178m                \33[48;5;214m      \33[48;5;178m \33[48;5;214m \33[48;5;178m       \33[48;5;172m      \33[48;5;136m  \33[48;5;130m       \33[48;5;094m      \33[0m   \33[48;5;058m       \33[0m
      \33[48;5;142m  \33[48;5;178m                            \33[48;5;172m      \33[48;5;136m   \33[48;5;130m      \33[48;5;094m      \33[0m          \33[48;5;058m  \33[0m
    \33[48;5;136m  \33[48;5;142m         \33[48;5;178m                   \33[48;5;172m    \33[48;5;136m     \33[48;5;130m     \33[48;5;094m       \33[0m
    \33[48;5;136m         \33[48;5;142m      \33[48;5;178m           \33[48;5;172m     \33[48;5;136m       \33[48;5;130m    \33[48;5;094m       \33[0m
    \33[48;5;100m       \33[48;5;136m                             \33[48;5;130m   \33[48;5;094m       \33[0m
     \33[48;5;003m    \33[48;5;100m      \33[48;5;136m                       \33[48;5;130m  \33[48;5;094m      \33[0m
       \33[48;5;003m      \33[48;5;100m     \33[48;5;136m                \33[48;5;130m  \33[48;5;094m      \33[0m
          \33[48;5;003m       \33[48;5;100m      \33[48;5;136m \33[48;5;130m   \33[48;5;094m      \33[0m

MANGO_TTY = "    Sad TTY not handle well colors :(\n" \
            "                                                        %\n" \
            "                                                      (#%\n" \
            "                               (((((((((((((######   (#%\n" \
            "                           ((((((((((((((((((((######%%%%%%\n" \
            "                        (//((((((((((((((((((((((####%%%%%%%%%%\n" \
            "                      /////////////(((((((((((((((####%%%%%%%%%%%\n" \
            "                    //////////////////((((((((((((((####%%%%%%%%%%\n" \
            "                  %/////******///////////((((((((((((####%%%%%%%%%%\n" \
            "                 ///******,*****//////////((((((((((((####%%%%%%%%%&\n" \
            "                //****,,,,,,,***///////////((((((((((((###%%%%%%%%%%\n" \
            "               /****,,,,..,,,***///////////(((((((((((((###%%%%%%%%&\n" \
            "             %*****,,,,,,,,,****///////////(((((((((((((###%%%%%%%%&\n" \
            "            ////****,,,,,,****////////////((((((((###(((####%%%%%%%%\n" \
            "          ///////************////////////((((((((######(####%%%%%%%%\n" \
            "        %//////////******///////////////((((((((########%###%%%%%%%%\n" \
            "       ///////////////////////////////(((((((((#######%%%%   %%%%%%%&\n" \
            "     ((((////////////////////////////((((((((########%%%%          %%\n" \
            "    ((((((((((((//////////////////(((((((((########%%%%\n" \
            "    (((((((((((((((((((////(/((((((((((((########%%%%\n" \
            "    #######(((((((((((((((((((((((((((#########%%%\n" \
            "     ##########(((((((((((((((((((##########%%#\n" \
            "      %###############(((((##############%\n" \
            "          #########################(\n\n"

types = [" INFO", " MINOR", " MAJOR", " FATAL"]

colors = ["\33[36m", "\33[33m", "\33[31m", "\33[31m"]

colors = {
    " INFO": "\33[36m",
    " MINOR": "\33[33m",
    " MAJOR": "\33[31m",
    " FATAL": "\33[31m"
}

descriptions = [
    ["Contents of the repository",
     "The repository must not contain compiled, temporary or unnecessary files."],
    ["File coherence",
     "A source file mustn't contain more than 10 functions (including at most 5 non-static functions)."],
    ["Naming files and folders",
     "All files names and folders must be in English, according the \33[3msnake_case\33[0m convention."],
    ["File header",
     "C files and every Makefile must always start with the standard header of the school."],
    ["Separation of functions",
     "Inside a source file, implementations of functions must be separated by one and only one empty line."],
    ["Indentation of reprocessor directives",
     "The preprocessor directives must be indented according to the level of indirection."],
    ["Global variables",
     "Global variables must be avoided as much as possible. Only global constants should be used."],
    ["\33[3minclude", "\33[3minclude\33[0m directive must only include C header files."],
    ["Line endings", "Line endings must be done in UNIX style (with \33[3m\\n\33[0m)."],
    ["Trailing spaces", "No trailing spaces must be present at the end of a line."],
    ["Leading/trailing lines",
     "No leading empty lines must be present. No more than 1 trailing empty line must be present."],
    ["Inline assembly",  # Celui qui a cette erreur s'est perdu MDR
     "Inline assembly must never be used. Programming in C must be done... in C."],
    ["Naming functions",
     "The name of a function must define the task it executes and must contain a verb. All function names must be in English, according to the \33[3msnake_case\33[0m convention."],
    ["Number of columns", "The length of a line must not exceed 80 columns."],
    ["Number of lines",
     "The body of a function should be as short as possible, and must not exceed 20 lines."],
    ["Number of parameters", "A function must not have more than 4 parameters."],
    ["Functions without parameters",
     "A function taking no parameters must take void as a parameter in the function declaration."],
    ["Structures as parameters",
     "Structures must be passed to functions using a pointer, not by copy."],
    ["Comments inside a function", "There must be no comment within a function."],
    ["Nested functions", "Nested functions are not allowed."],
    ["Code line content", "A line must correspond to only one statement."],
    ["Indentation",
     "Each indentation level must be done by using 4 spaces. No tabulations may be used for indentation."],
    ["Spaces",
     "When using a space as a separator, one and only one space character must be used."],
    ["Curly brackets",
     "Opening curly brackets must be at the end of the line, after the content it precedes, except for functions definitions where they must be placed alone on their line. Closing curly brackets must be alone on their line, except in the case of \33[3melse\33[0m/\33[3melse if\33[0m control structures, \33[3menum\33[0m declarations, or structure declarations."],
    ["Variable declarations",
     "Variables must be declared at the beginning of the function. Only one variable must be declared per statement."],
    ["Blank lines",
     "A blank line must separate the variable declarations from the remainder of the function. No other blank lines must be present in the function."],
    ["Naming identifiers",
     "All identifier names must be in English, according to the \33[3msnake_case\33[0m convention. The type names defined with \33[3mtypedef\33[0m must end with \33[3m_t\33[0m. The names of macros and global constants and the content of enums must be written in \33[3mUPPER_SNAKE_CASE\33[0m."],
    ["Pointers",
     "The pointer symbol (*) must be attached to the associated variable, with no spaces in between. It must also be preceded by a space, except when it is itself preceded by another asterisk. When used in a cast, the asterisk must have a space on its left side, but not on its right side."],
    ["Conditional branching", "A conditionnal block must not contain more than 3 branches."],
    ["Ternary operators",
     "The use of ternary operators is allowed as far as it is kept simple and readable, and if it does not obfuscate code. You must never use nested or chained ternary operators. You must always use the value produced by a ternary operator (by assigning it to a variable or returning it for example)."],
    ["\33[3mgoto", "Using the \33[3mgoto\33[0m keyword if forbidden."],
    ["Content",
     "Header files must only contain \33[1mfunctions prototypes\33[0m, \33[1mtypes declarations\33[0m, \33[1mglobal variable/constant declarations\33[0m, \33[1mmacros\33[0m, \33[1mstatic inline functions\33[0m. All these elements must only be found in header files, and thus not in source files."],
    ["Include guard", "Headers must be protected from double inclusion."],
    ["Macros", "Macros must match only one statement, and fit on a single line."],
    ["Line break at the end of file", "Files must end with a line break."]
]
__descriptions = {
    "O1": [
        "Contents of the repository",
        "The repository should contain only files required for compilation and must not contain compiled (\33[3m.o, .hi, .a, .so, ...\33[3m), temporary or unnecessary files  (\33[3m*~ * #, *.d, toto, ...\33[3m)."
    ]
}

descriptions = {
    "C-O1": __descriptions["O1"],
    "C-O3": [
        "File coherence",
        "A source file mustn't contain more than 10 functions (including at most 5 non-static functions)."
    ],
    "C-O4": [
        "Naming files and folders",
        "All files names and folders must be in English, according the \33[3msnake_case\33[0m convention."
    ],
    "C-G1": [
        "File header",
        "C files and every Makefile must always start with the standard header of the school."
    ],
    "C-G2": [
        "Separation of functions",
        "Inside a source file, implementations of functions must be separated by one and only one empty line."
    ],
    "C-G3": [
        "Indentation of reprocessor directives",
        "The preprocessor directives must be indented according to the level of indirection."
    ],
    "C-G4": [
        "Global variables",
        "Global variables must be avoided as much as possible. Only global constants should be used."
    ],
    "C-G5": ["\33[3minclude", "\33[3minclude\33[0m directive must only include C header files."],
    "C-G6": ["Line endings", "Line endings must be done in UNIX style (with \33[3m\\n\33[0m)."],
    "C-G7": ["Trailing spaces", "No trailing spaces must be present at the end of a line."],
    "C-G8": [
        "Leading/trailing lines",
        "No leading empty lines must be present. No more than 1 trailing empty line must be present."
    ],
    "C-G10": [
        "Inline assembly",  # Celui qui a cette erreur s'est perdu MDR
        "Inline assembly must never be used. Programming in C must be done... in C."
    ],
    "C-F2": [
        "Naming functions",
        "The name of a function must define the task it executes and must contain a verb. All function names must be in English, according to the \33[3msnake_case\33[0m convention."
    ],
    "C-F3": ["Number of columns", "The length of a line must not exceed 80 columns."],
    "C-F4": [
        "Number of lines",
        "The body of a function should be as short as possible, and must not exceed 20 lines."
    ],
    "C-F5": ["Number of parameters", "A function must not have more than 4 parameters."],
    "C-F6": [
        "Functions without parameters",
        "A function taking no parameters must take void as a parameter in the function declaration."
    ],
    "C-F7": [
        "Structures as parameters",
        "Structures must be passed to functions using a pointer, not by copy."
    ],
    "C-F8": ["Comments inside a function", "There must be no comment within a function."],
    "C-F9": ["Nested functions", "Nested functions are not allowed."],
    "C-L1": ["Code line content", "A line must correspond to only one statement."],
    "C-L2": [
        "Indentation",
        "Each indentation level must be done by using 4 spaces. No tabulations may be used for indentation."
    ],
    "C-L3": [
        "Spaces",
        "When using a space as a separator, one and only one space character must be used."
    ],
    "C-L4": [
        "Curly brackets",
        "Opening curly brackets must be at the end of the line, after the content it precedes, except for functions definitions where they must be placed alone on their line. Closing curly brackets must be alone on their line, except in the case of \33[3melse\33[0m/\33[3melse if\33[0m control structures, \33[3menum\33[0m declarations, or structure declarations."
    ],
    "C-L5": [
        "Variable declarations",
        "Variables must be declared at the beginning of the function. Only one variable must be declared per statement."
    ],
    "C-L6": [
        "Blank lines",
        "A blank line must separate the variable declarations from the remainder of the function. No other blank lines must be present in the function."
    ],
    "C-V1": [
        "Naming identifiers",
        "All identifier names must be in English, according to the \33[3msnake_case\33[0m convention. The type names defined with \33[3mtypedef\33[0m must end with \33[3m_t\33[0m. The names of macros and global constants and the content of enums must be written in \33[3mUPPER_SNAKE_CASE\33[0m."
    ],
    "C-V3": [
        "Pointers",
        "The pointer symbol (*) must be attached to the associated variable, with no spaces in between. It must also be preceded by a space, except when it is itself preceded by another asterisk. When used in a cast, the asterisk must have a space on its left side, but not on its right side."
    ],
    "C-C1": [
        "Conditional branching",
        "A conditionnal block must not contain more than 3 branches."
    ],
    "C-C2": [
        "Ternary operators",
        "The use of ternary operators is allowed as far as it is kept simple and readable, and if it does not obfuscate code. You must never use nested or chained ternary operators. You must always use the value produced by a ternary operator (by assigning it to a variable or returning it for example)."
    ],
    "C-C3": ["\33[3mgoto", "Using the \33[3mgoto\33[0m keyword if forbidden."],
    "C-H1": [
        "Content",
        "Header files must only contain \33[1mfunctions prototypes\33[0m, \33[1mtypes declarations\33[0m, \33[1mglobal variable/constant declarations\33[0m, \33[1mmacros\33[0m, \33[1mstatic inline functions\33[0m. All these elements must only be found in header files, and thus not in source files."
    ],
    "C-H2": ["Include guard", "Headers must be protected from double inclusion."],
    "C-H3": ["Macros", "Macros must match only one statement, and fit on a single line."],
    "C-A3": ["Line break at the end of file", "Files must end with a line break."],


def set_arguments():
    parser = parseArgs()
    parser.add_argument("-Ee", "-Eerrors", "--exclude-errors", nargs='+',
    parser.add_argument("-Ee", "-Eerrors", "--exclude-errors", nargs="+",
                        help="Exclude coding style errors from report")
    parser.add_argument("-Ef", "-Efiles", "--exclude-files", nargs="+",
                        help="Exclude files from coding style checking")
    parser.add_argument("-w", "--watch", nargs=1,
                        help="Watch for changes in the repository every x seconds")
    parser.add_argument("-v", "--version", action="store_true",
                        help="Show Mango version")
    parser.add_argument("-u", "--update", action="store_true",
                        help="Update Mango to last version (actually not working)")
    return parser.parse_args()


def download_coding_style():
    download_command = which("wget") or which("curl")

    print("\33[3mcoding-style\33[0m command not found,", end='')
    if download_command is None:
        print(" and neither \33[3wget\33[0m nor \33[3curl\33[0m were found on your computer,"
              f" so please download \33[3mcoding-style\33[0m here: {CODING_STYLE_URL}"
              f" and/or add it to your path")
    print(" download it? [Y/n] ", end="")

    key = input().lower()

    if key not in ('', 'y', 'yes', 'o', 'oui'):
        print("You must have the \33[3mcoding-style\33[0m command to be able to use \33[1mMango\33[0m")
    if key not in ("", "y", "yes", "o", "oui"):
        sys.exit(1)
    print("Downloading \33[3mcoding-style\33[0m...")

    system(f"sudo {download_command} {CODING_STYLE_URL}"
           f" -{'O' if 'wget' in download_command  else 'o'} /bin/coding-style 2> /dev/null")
    system("sudo chmod +x /bin/coding-style")
    print("\33[3mcoding-style\33[0m downloaded\n")


def update():
    print("Updating not working at the moment, it will be re-introduced in a future version.")
    sys.exit(0)


def print_version():
    print(f"Mango {VERSION}")
    sys.exit(0)


def get_exclude_files(args):
    exclude = []
    if not args.exclude_files:
        return exclude
    for file in args.exclude_files:
        if path.isdir(file):
            for root, _dirs, files in walk(file):
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
    if not args.exclude_errors:
        return exclude
    for error in args.exclude_errors:
        exclude.append(error.strip())
    return exclude


def coding_style():
    system("sudo rm -f /tmp/coding-style-reports.log")
    system("coding-style . /tmp/ > /dev/null")
    try:
        with open("/tmp/coding-style-reports.log", "r", encoding="utf-8") as file:
            out = file.read()
            file.close()
    except:
        print(f"{argv[0]}: Cannot open log file.", file=stderr)
        sys.exit(1)
    try:
        remove(f"./{CODING_STYLE}-reports.log")
    except:
        print(f"{argv[0]}: Cannot remove log file.", file=stderr)
        sys.exit(1)
    out = out.split("\n")
    return out


def print_error(line, rule):
    color = f"\33[0m{colors[line[2]]}"
    print(f"{color}\33[1m{line[0]}", end="")
    if int(line[1]) > 1:
        print(f" at line {line[1]}", end="")
    print(f"\n{line[2][1:]} {line[3]}: {color}{rule[0]}\33[0m\n{rule[1]}\n")


def print_errors_number(err_nb, is_a_tty):
    if err_nb[3] or err_nb[2] > 0 or err_nb[1] > 0 or err_nb[0] or err_nb[4] > 0:
        if err_nb[3]:
            print(f"\33[1;31m{err_nb[3]} Fatal\33[0m | ", end="")
        print(f"\33[1;31m{err_nb[2]} Major\33[0m | \33[1;33m{err_nb[1]} Minor\33[0m | \33[1;36m{err_nb[0]} Info\33[0m",
              end="")
        if err_nb[4] > 0:
            print(f" | \33[1;37m{err_nb[4]} Unknown\33[0m", end="")
        if err_nb[5] > 0:
            print(f" | \33[1;37m{err_nb[5]} excluded\33[0m", end="")
        print()
    elif not is_a_tty:
        print(f"{MANGO_ASCII}    ✅ There is no coding style error")
        if err_nb[5] > 0:
            print(f"\nBe careful, you still have {err_nb[5]} excluded errors")
    else:
        print(f"{MANGO_TTY}    but you have no coding style error :)")
        if err_nb[5] > 0:
            print(f"\nBe careful, you still have {err_nb[5]} excluded errors")


def mango(exclude_files, exclude_errors):
    out = coding_style()
    # [INFO, MINOR, MAJOR, FATAL, UNKNOWN, EXCLUDED]
    err_nb = [0, 0, 0, 0, 0, 0]
    try:
        is_a_tty = "tty" in ttyname(1)
    except:
        is_a_tty = True

    if not out:
        if not is_a_tty:
            print(f"{MANGO_ASCII}    ✅ There is no coding style error")
        else:
            print(f"{MANGO_TTY}    but you have no coding style error :)")
        return
    for line in out:
        backup_line = line
        if line == "":
            continue
        line = line.split(':')
        if path.abspath(line[0]) in exclude_files or line[3] in exclude_errors:
            err_nb[5] += 1
            continue
        try:
            index = rules.index(line[3])
            rule = descriptions[line[3]]
        except:
            print(f"{backup_line}\n")
            err_nb[4] += 1
            continue
        if line[0][0:2] == "./":
            line[0] = line[0][2:]
        match line[2]:
            case " INFO":
                err_nb[0] += 1
            case " MINOR":
                err_nb[1] += 1
            case " MAJOR":
                err_nb[2] += 1
            case " FATAL":
                err_nb[3] += 1
        print_error(line, rule)
    print_errors_number(err_nb, is_a_tty)


def main():
    args = set_arguments()

    if args.version:
        print_version()
    if args.update:
        update()
    if which("coding-style") is None:
        download_coding_style()

    exclude_files = get_exclude_files(args)
    exclude_errors = get_exclude_errors(args)

    if args.watch:
        sleep_duration = int(args.watch[0])
        while True:
            try:
                system("clear")
                mango(exclude_files, exclude_errors)
                sleep(sleep_duration)
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                sys.exit(1)
    else:
        mango(exclude_files, exclude_errors)


if __name__ == "__main__":
    main()
