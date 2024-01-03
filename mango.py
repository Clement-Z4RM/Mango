#!/usr/bin/env python3

from sys import exit
from os import ttyname, system, path, walk, remove
from argparse import ArgumentParser as parseArgs
from re import sub
from shutil import which
from time import sleep

VERSION = "v1.9.3"

LAMBDANANAS = "lambdananas"
CODING_STYLE = "coding-style"

CODING_STYLE_URL = f"https://raw.githubusercontent.com/Epitech/{CODING_STYLE}-checker/main/{CODING_STYLE}.sh"

# BEIGE/BROWN
B0 = "\33[48;5;003m"
B1 = "\33[48;5;094m"
B2 = "\33[48;5;130m"
B3 = "\33[48;5;136m"
B4 = "\33[48;5;215m"
B5 = "\33[48;5;222m"

# GREEN
G0 = "\33[48;5;058m"
G1 = "\33[48;5;064m"
G2 = "\33[48;5;100m"
G3 = "\33[48;5;106m"
G4 = "\33[48;5;112m"
G5 = "\33[48;5;142m"

# ORANGE
O0 = "\33[48;5;166m"
O1 = "\33[48;5;172m"
O2 = "\33[48;5;202m"
O3 = "\33[48;5;208m"

# YELLOW
Y0 = "\33[48;5;178m"
Y1 = "\33[48;5;214m"
Y2 = "\33[48;5;220m"
Y3 = "\33[48;5;221m"

MANGO_ASCII = f"""{' ' * 54}{B2} {B1}  \33[0m
{' ' * 31}{O0}{' ' * 19}\33[0m   {O0} {B2} {B1} \33[0m
{' ' * 27}{O2}          {O0}{' ' * 16}{G0}      \33[0m
{' ' * 24}{O3}        {O2}         {O0}          {G1}   {G0}         \33[0m
{' ' * 22}{O3}{' ' * 15}{O2}      {O0}       {G3}  {G1}   {G0}          \33[0m
{' ' * 20}{O3}{' ' * 21}{O2}   {O0}      {G3}    {G1}   {G0}         \33[0m
{' ' * 19}{Y1}      {B4}     {Y1} {O3}{' ' * 12}{O2} {O0}     {G5} {G3}     {G1}   {G0}         \33[0m
{' ' * 17}{Y1}    {B4}          {Y1}  {O3}{' ' * 11}{O1}  {O0}   {O1} {G3}      {G1}  {G0}          \33[0m
{' ' * 16}{Y1}    {B4}  {Y3}  {B5}   {Y3} {B4}    {Y1}  {O3}         {O1}   {O0}    {G4}  {G3}     {G1}  {G0}         \33[0m
{' ' * 15}{Y1}    {Y3}   {B5}     {Y3}  {B4}  {Y1}     {O3}      {O1}     {O0}   {G5} {G4} {G3}     {G1}   {G0}        \33[0m
{' ' * 14}{Y1}  {Y2}  {Y3}    {B5}    {Y3}   {B4} {Y1}        {O3}    {O1}     {O0}    {G4}  {G3}     {G1}  {G0}        \33[0m
{' ' * 12}{Y1}    {Y2}  {Y3}          {Y1}          {O3}  {O1}       {O0}  {B2}    {G3}     {G1}  {G0}        \33[0m
          {Y1}      {Y2}   {Y3}     {Y2}   {Y1}         {Y0}  {O1}        {O0} {B2}      {B3} {G3}   {G1}   {G0}       \33[0m
         {Y0}       {Y1}{' ' * 18}{Y0}     {O1}       {B3} {B2}        {B1}  {G3} {G1}   {G0}       \33[0m
       {Y0}{' ' * 16}{Y1}      {Y0} {Y1} {Y0}       {O1}      {B3}  {B2}       {B1}      \33[0m   {G0}       \33[0m
      {G5}  {Y0}{' ' * 28}{O1}      {B3}   {B2}      {B1}      \33[0m          {G0}  \33[0m
    {B3}  {G5}         {Y0}{' ' * 19}{O1}    {B3}     {B2}     {B1}       \33[0m
    {B3}         {G5}      {Y0}{' ' * 11}{O1}     {B3}       {B2}    {B1}       \33[0m
    {G2}       {B3}{' ' * 29}{B2}   {B1}       \33[0m
     {B0}    {G2}      {B3}{' ' * 23}{B2}  {B1}      \33[0m
       {B0}      {G2}     {B3}{' ' * 16}{B2}  {B1}      \33[0m
          {B0}       {G2}      {B3} {B2}   {B1}      \33[0m

    ✅ There is no coding style error"""

MANGO_TTY = """    Sad TTY not handle well colors :(
                                                        %
                                                      (#%
                               (((((((((((((######   (#%
                           ((((((((((((((((((((######%%%%%%
                        (//((((((((((((((((((((((####%%%%%%%%%%
                      /////////////(((((((((((((((####%%%%%%%%%%%
                    //////////////////((((((((((((((####%%%%%%%%%%
                  %/////******///////////((((((((((((####%%%%%%%%%%
                 ///******,*****//////////((((((((((((####%%%%%%%%%&
                //****,,,,,,,***///////////((((((((((((###%%%%%%%%%%
               /****,,,,..,,,***///////////(((((((((((((###%%%%%%%%&
             %*****,,,,,,,,,****///////////(((((((((((((###%%%%%%%%&
            ////****,,,,,,****////////////((((((((###(((####%%%%%%%%
          ///////************////////////((((((((######(####%%%%%%%%
        %//////////******///////////////((((((((########%###%%%%%%%%
       ///////////////////////////////(((((((((#######%%%%   %%%%%%%&
     ((((////////////////////////////((((((((########%%%%          %%
    ((((((((((((//////////////////(((((((((########%%%%
    (((((((((((((((((((////(/((((((((((((########%%%%
    #######(((((((((((((((((((((((((((#########%%%
     ##########(((((((((((((((((((##########%%#
      %###############(((((##############%
          #########################(

    but you have no coding style error :)"""

colors = {
    " INFO": "\33[36m",
    " MINOR": "\33[33m",
    " MAJOR": "\33[31m",
    " FATAL": "\33[31m"
}

__descriptions = {
    "O1": [
        "Contents of the repository",
        "The repository should contain only files required for compilation and must not contain compiled (\33[3m.o, .hi, .a, .so, ...\33[0m), temporary or unnecessary files  (\33[3m*~ * #, *.d, toto, ...\33[0m)."
    ]
}

descriptions = {
    # C
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

    # Haskell
    "H-P1": ["File is not parsable", None],
    "H-O1": __descriptions["O1"],
    "H-O2": [
        "File extension",
        "Sources in a Haskell program should only have extension \33[3m.hs\33[0m."
    ],
    "H-O3": [
        "File coherence",
        "A Haskell project must be organised in \33[1mmodules\33[0m, each of which should match a \33[1mlogical entity\33[0m, and group all the functions and data structures associated with that entity. Every haskell file (including Main) should declare a module."
    ],
    "H-O4": [
        "Naming files",
        "The name of a file should match the name of its module. Therefore, files and modules must be named in \33[3mUpperCamelCase\33[0m and in English."
    ],
    "H-O5": [
        "Module exports",
        "All modules should explicitly declare their exported definitions. Except the Main module, all modules are expected to export at least one definition."
    ],
    "H-G1": [
        "Epitech header",
        "Every Haskell file should start with a standard Epitech header."
    ],
    "H-E1": [
        "Language extensions",
        "All language extensions are forbidden except if the project's subject says otherwise."
    ],
    "H-T1": [
        "Top level bindings signatures",
        "All top level bindings must have an accompanying type signature."
    ],
    "H-M1": [
        "Mutable variables",
        "Mutable variables are strictly forbidden."
    ],
    "H-M2": [
        "Unsafe functions",
        "Functions performing unsafe operations are strictly forbidden."
    ],
    "H-M3": [
        "Forbidden Module Imports",
        """In order to enforce rules \33[1mH-M1\33[0m and \33[1mH-M2\33[0m, importing any of the following module is strictly forbidden:
\33[1m • Data.IORef
 • Data.STRef
 • Control.Concurrent.STM.TVar
 • System.IO.Unsafe\33[0m"""
    ],
    "H-F1": [
        "Coherence of functions",
        "A function should only do one thing, not mix the different levels of abstraction and respect the principle of single responsibility (a function must only be changed for one reason)."
    ],
    "H-F2": [
        "Naming function",
        "The name of a function should define the task it executes and should contain a verb. All function names should be in English, according to the \33[3mlowerCamelCase\33[0m convention. Special characters are tolerated as long as they are justified and used sparingly."
    ],
    "H-F3": [
        "Line length",
        "A Line must be less than 80 characters long."
    ],
    "H-F4": [
        "Function length",
        "A function body must be 10 lines or less."
    ],
    "H-V1": [
        "Naming identifiers",
        "All identifier names should be in English, according to the \33[3mlowerCamelCase\33[0m convention. The type names and constructors should be in English, according to the \33[3mUpperCamelCase\33[0m convention."
    ],
    "H-C4": [
        "Conditional branching",
        "Nested If statements are strictly forbidden."
    ],
    "H-C5": [
        "Guards and ifs expressed as pattern matching",
        "Guards and if statements which can be expressed as pattern matchings must be expressed as such.."
    ],
    "H-D1": [
        "Useless do",
        "The \33[1mDo\33[0m notation is forbidden unless it contains a generator (a statement with a left arrow)."
    ]
}


def set_arguments():
    parser = parseArgs()
    parser.add_argument(
        "-H", "--haskell", "--lambdananas",
        action="store_true",
        help=f"Check coding style for Haskell (use {LAMBDANANAS} instead of {CODING_STYLE}). Some Haskell errors are detected by {CODING_STYLE}, but since Epitech uses {LAMBDANANAS}, it is better to use this flag for Haskell"
    )
    parser.add_argument(
        "-i", "--ignore", "--gitignore",
        action="store_true",
        help="Don't exclude .gitignore content from coding style checking"
    )
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List all errors (with description)"
    )
    parser.add_argument(
        "-Sl", "--short-list",
        action="store_true",
        help="List all errors (without description)"
    )
    parser.add_argument(
        "-s", "--show",
        nargs=1,
        help="Show description of an error"
    )
    parser.add_argument(
        "-Ee", "-Eerrors", "--exclude-errors",
        nargs="+",
        metavar="ERROR",
        help="Exclude coding style errors from report"
    )
    parser.add_argument(
        "-Ef", "-Efiles", "--exclude-files",
        nargs="+",
        metavar="FILE",
        help="Exclude files from coding style checking"
    )
    parser.add_argument(
        "-w", "--watch",
        nargs=1,
        metavar="SECONDS",
        type=int,
        help="Watch for changes in the repository every x seconds. Ctrl + C to exit"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Don’t output anything, just set exit status"
    )
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show Mango version"
    )
    parser.add_argument(
        "-u", "--update",
        action="store_true",
        help="Update Mango to last version (actually not working, you should do it manually)"
    )
    return parser.parse_args()


def download_coding_style(is_lambdananas):
    if is_lambdananas:
        print(f"""You are using \33[1mHaskell\33[0m, so you need to download \33[3m{LAMBDANANAS}\33[0m
You can get it on the intranet (https://intra.epitech.eu/file/Public/technical-documentations/Haskell/lambdananas.tar.gz)
Don't forget to add it to your PATH""")
        exit(1)

    download_command = which("wget") or which("curl")

    print(f"\33[3m{CODING_STYLE}\33[0m command not found,", end="")
    if download_command is None:
        print(" and neither \33[3wget\33[0m nor \33[3curl\33[0m were found on your computer,"
              f" so please download \33[3m{CODING_STYLE}\33[0m here: {CODING_STYLE_URL}"
              f" and/or add it to your PATH")
    print(" download it? [Y/n] ", end="")
    if input().lower() not in ("", "y", "yes", "o", "oui"):
        print(f"You must have the \33[3m{CODING_STYLE}\33[0m command to be able to use \33[1mMango\33[0m")
        exit(1)
    print(f"Downloading \33[3m{CODING_STYLE}\33[0m...")

    if system(f"sudo {download_command} {CODING_STYLE_URL} -{'O' if download_command.endswith('wget') else 'o'} /bin/{CODING_STYLE} 2> /dev/null"):
        print(f"Error while downloading \33[3m{CODING_STYLE}\33[0m")
        exit(1)
    if system(f"sudo chmod +x /bin/{CODING_STYLE}"):
        print(f"Error while setting permissions for \33[3m{CODING_STYLE}\33[0m")
        exit(1)
    print(f"\33[3m{CODING_STYLE}\33[0m downloaded\n")
    return which(CODING_STYLE)


def list_errors(color, short=False):
    bold = "\33[1m" if color else ""
    italic = "\33[3m" if color else ""
    reset = "\33[0m" if color else ""

    print(f"Errors with code starting with {italic}C{reset} are for {bold}C{reset}, and {italic}H{reset} for {bold}Haskell{reset}\n")
    for description in descriptions.items():
        if not color:
            __description = [sub('\33\\[[0-9;]+m', '', description[1][0]), sub('\33\\[[0-9;]+m', '', description[1][1] or '')]
        else:
            __description = description[1]

        if short:
            print(description[0])
        else:
            print(f"{bold}{description[0]}{reset}: {__description[0]}{reset}: {__description[1]}\n")
    exit(0)


def show_error(color, error):
    bold = "\33[1m" if color else ""
    reset = "\33[0m" if color else ""

    try:
        if not color:
            description = [sub('\33\\[[0-9;]+m', '', descriptions[error][0]), sub('\33\\[[0-9;]+m', '', descriptions[error][1] or '')]
        else:
            description = descriptions[error]

        print(f"{bold}{error}{reset}: {description[0]}{reset}")
        if description[1]:
            print(f"{description[1]}")
    except KeyError:
        print(f"Error {bold}{error}{reset} not found")
    exit(0)


def print_version():
    print(f"Mango {VERSION}")
    exit(0)


def update():
    print("""Updating not working at the moment, it will be re-introduced in a future version.
In the meantime, you can do the same command as the one used to install Mango to update it => https://github.com/Clement-Z4RM/Mango?tab=readme-ov-file#with-wget""")
    exit(0)


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


def coding_style(checker):
    if checker.endswith(LAMBDANANAS):
        all_files = []

        for root, _dirs, files in walk("./"):
            if root.startswith(("./.git", "./test", "./tests", "./bonus")) or not root.startswith("./."):
                continue
            for name in files:
                if not name.endswith(".hs"):
                    continue
                full_path = path.join(root, name)
                all_files.append(full_path)
        if not all_files:
            return []
        all_files_joined = " ".join(["'{}'".format(element) for element in all_files])
        system(f"{checker} './' {all_files_joined} > ./{CODING_STYLE}-reports.log 2>&1")
    else:
        system(f"{checker} . ./ > /dev/null")
    with open(f"./{CODING_STYLE}-reports.log", "r", encoding="utf-8") as file:
        out = file.read()
        file.close()
    remove(f"./{CODING_STYLE}-reports.log")
    return out.split("\n")


def print_error(line, rule, strings):
    color = f"\33[0m{colors[line[2]]}" if strings["RESET"] else ""
    if not strings["RESET"]:
        rule = [sub('\33\\[[0-9;]+m', '', rule[0]), sub('\33\\[[0-9;]+m', '', rule[1] or '')]

    print(f"{color}{strings['BOLD']}{line[0]}", end="")
    if int(line[1]) > 1:
        print(f" at line {line[1]}", end="")
    print(f"\n{line[2][1:]} {line[3]}: {color}{rule[0]}{strings['RESET']}")
    if rule[1]:
        print(f"{rule[1]}")
    print()


def print_errors_number(errors, strings):
    if errors["INFO"] or errors["MINOR"] or errors["MAJOR"] or errors["FATAL"] or errors["UNKNOWN"]:
        if errors["FATAL"]:
            print(f"{strings['RED']}{errors['FATAL']} Fatal{strings['RESET']} | ", end="")
        print(
            f"{strings['RED']}{errors['MAJOR']} Major{strings['RESET']} | {strings['YELLOW']}{errors['MINOR']} Minor{strings['RESET']} | {strings['BLUE']}{errors['INFO']} Info{strings['RESET']}",
            end="")
        if errors["UNKNOWN"]:
            print(f" | {strings['GRAY']}{errors['UNKNOWN']} Unknown{strings['RESET']}", end="")
        if errors["EXCLUDED"]:
            print(f" | {strings['GRAY']}{errors['EXCLUDED']} excluded{strings['RESET']}", end="")
        if errors["IGNORED"]:
            print(f" | {strings['GRAY']}{errors['IGNORED']} ignored{strings['RESET']}", end="")
        print()
        return 1
    print(strings["MANGO"])
    if errors["EXCLUDED"] or errors["IGNORED"]:
        print(f"\nBe careful, you still have", end="")
        if errors["EXCLUDED"]:
            print(f" {errors['EXCLUDED']} excluded", end="")
        if errors["EXCLUDED"] and errors["IGNORED"]:
            print(" and", end="")
        if errors["IGNORED"]:
            print(f" {errors['IGNORED']} ignored", end="")
        print(" errors")
    return 0


def mango(checker, exclude_files, exclude_errors, git, quiet, should_clear=False):
    out = coding_style(checker)
    errors = {
        "INFO": 0,
        "MINOR": 0,
        "MAJOR": 0,
        "FATAL": 0,
        "UNKNOWN": 0,
        "EXCLUDED": 0,
        "IGNORED": 0
    }
    strings = {
        "MANGO": MANGO_TTY,
        "BOLD": "",
        "RED": "",
        "YELLOW": "",
        "BLUE": "",
        "GRAY": "",
        "RESET": ""
    }
    try:
        if "tty" not in ttyname(1):
            strings["MANGO"] = MANGO_ASCII
        strings["BOLD"] = "\33[1m"
        strings["RED"] = "\33[1;31m"
        strings["YELLOW"] = "\33[1;33m"
        strings["BLUE"] = "\33[1;36m"
        strings["GRAY"] = "\33[1;37m"
        strings["RESET"] = "\33[0m"
    except OSError:
        pass

    if should_clear:
        system("clear")
    if not out:
        if not quiet:
            print(strings["MANGO"])
        return 0
    for line in out:
        backup_line = line
        if line == "":
            continue
        line = line.split(":")
        if line[0].endswith("contains forbidden extensions"):
            line = [line[0].split(" ")[0], "1", " MAJOR", "H-O2"]
        line[3] = line[3].split(" #")[0]
        if line[0][0:2] == "./":
            line[0] = line[0][2:]
        try:
            if path.abspath(line[0]) in exclude_files or line[3] in exclude_errors:
                errors["EXCLUDED"] += 1
                continue
            if git and not system(f"{git} check-ignore -q '{line[0]}' > /dev/null 2>&1"):
                errors["IGNORED"] += 1
                continue
            rule = descriptions[line[3]]
        except:
            if not quiet:
                print(f"{backup_line}\n")
            errors["UNKNOWN"] += 1
            continue
        errors[line[2][1:]] += 1
        if not quiet:
            print_error(line, rule, strings)
    if not quiet:
        return print_errors_number(errors, strings)
    else:
        errors_values = errors.values()
        return int(not all(value == 0 for value in errors_values))


def main():
    args = set_arguments()
    # 0: not a tty, 1: tty, 2: error (maybe redirected)
    try:
        is_a_tty = 1 if "tty" in ttyname(1) else 0
    except OSError:
        is_a_tty = 2

    if args.list or args.short_list:
        list_errors(is_a_tty != 2, args.short_list)
    if args.show:
        show_error(is_a_tty != 2, args.show[0].upper())
    if args.version:
        print_version()
    if args.update:
        update()

    checker = which(LAMBDANANAS if args.haskell else CODING_STYLE)

    if checker is None:
        checker = download_coding_style(args.haskell)
    if checker is None:
        exit(1)

    exclude_files = get_exclude_files(args)
    exclude_errors = get_exclude_errors(args)
    git = None if args.ignore else which("git")

    if args.watch:
        to_return = 0
        sleep_duration = int(args.watch[0])
        while True:
            try:
                to_return = mango(checker, exclude_files, exclude_errors, git, args.quiet, True)
                sleep(sleep_duration)
            except KeyboardInterrupt:
                exit(to_return)
    else:
        exit(mango(checker, exclude_files, exclude_errors, git, args.quiet))


if __name__ == "__main__":
    main()
