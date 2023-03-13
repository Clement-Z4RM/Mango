#!/bin/python3

import sys
import os
import argparse
from shutil import which
import subprocess
import requests
import time

version = "v1.6.5"

changelog = "\033[1m[1.6.5] - 2022-03-13\033[0m\n"\
"--------------------------------------------------\n"\
"✨ Special Stumper update\n\n"\
"\033[1mAdded\033[0m\n"\
" · Special Mango ASCII art without colors for TTY mode\n\n"\
"\033[1mFixed\033[0m\n"\
" · Separate check of update and update to avoid \"\033[3mCannot check for update\033[0m\" error message when updating"

mango_ascii = "                                                      [48;5;130m [48;5;094m  [0m\n"\
"                               [48;5;166m                       [48;5;130m [48;5;094m [0m\n"\
"                           [48;5;202m          [48;5;166m                [48;5;058m      [0m\n"\
"                        [48;5;208m        [48;5;202m         [48;5;166m          [48;5;064m   [48;5;058m         [0m\n"\
"                      [48;5;208m               [48;5;202m      [48;5;166m       [48;5;106m  [48;5;064m   [48;5;058m          [0m\n"\
"                    [48;5;208m                     [48;5;202m   [48;5;166m      [48;5;106m    [48;5;064m   [48;5;058m         [0m\n"\
"                   [48;5;214m      [48;5;215m     [48;5;214m [48;5;208m            [48;5;202m [48;5;166m     [48;5;142m [48;5;106m     [48;5;064m   [48;5;058m         [0m\n"\
"                 [48;5;214m    [48;5;215m          [48;5;214m  [48;5;208m           [48;5;172m  [48;5;166m   [48;5;172m [48;5;106m      [48;5;064m  [48;5;058m          [0m\n"\
"                [48;5;214m    [48;5;215m  [48;5;221m  [48;5;222m   [48;5;221m [48;5;215m    [48;5;214m  [48;5;208m         [48;5;172m   [48;5;166m    [48;5;112m  [48;5;106m     [48;5;064m  [48;5;058m         [0m\n"\
"               [48;5;214m    [48;5;221m   [48;5;222m     [48;5;221m  [48;5;215m  [48;5;214m     [48;5;208m      [48;5;172m     [48;5;166m   [48;5;142m [48;5;112m [48;5;106m     [48;5;064m   [48;5;058m        [0m\n"\
"              [48;5;214m  [48;5;220m [48;5;220m [48;5;221m    [48;5;222m    [48;5;221m   [48;5;215m [48;5;214m        [48;5;208m    [48;5;172m     [48;5;166m    [48;5;112m  [48;5;106m     [48;5;064m  [48;5;058m        [0m\n"\
"            [48;5;214m    [48;5;220m [48;5;220m [48;5;221m          [48;5;214m          [48;5;208m  [48;5;172m       [48;5;166m  [48;5;130m    [48;5;106m     [48;5;064m  [48;5;058m        [0m\n"\
"          [48;5/[48;5;214m      [48;5;220m [48;5;220m [48;5;220m [48;5;221m     [48;5;220m [48;5;220m [48;5;220m [48;5;214m         [48;5;178m  [48;5;172m        [48;5;166m [48;5;130m      [48;5;136m [48;5;106m   [48;5;064m   [48;5;058m       [0m\n"\
"         [48;5;178m       [48;5;214m                  [48;5;178m     [48;5;172m       [48;5;136m [48;5;130m        [48;5;094m  [48;5;106m [48;5;064m   [48;5;058m       [0m\n"\
"       [48;5;178m                [48;5;214m      [48;5;178m [48;5;214m [48;5;178m       [48;5;172m      [48;5;136m  [48;5;130m       [48;5;094m        [48;5;058m        [0m\n"\
"      [48;5;142m  [48;5;178m                            [48;5;172m      [48;5;136m   [48;5;130m      [48;5;094m                [48;5;058m  [0m\n"\
"    [48;5;136m  [48;5;142m         [48;5;178m                   [48;5;172m    [48;5;136m     [48;5;130m     [48;5;094m       [0m\n"\
"    [48;5;136m         [48;5;142m      [48;5;178m           [48;5;172m     [48;5;136m       [48;5;130m    [48;5;094m       [0m\n"\
"    [48;5;100m       [48;5;136m                             [48;5;130m   [48;5;094m       [0m\n"\
"     [48;5;003m    [48;5;100m      [48;5;136m                       [48;5;130m  [48;5;094m      [48;5#[0m\n"\
"       [48;5;003m      [48;5;100m     [48;5;136m                [48;5;130m  [48;5;094m      [0m\n"\
"          [48;5;003m       [48;5;100m      [48;5;136m [3 [3 [3 [48;5;130m   [48;5;094m      [0m\n\n"

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

colors = ["[36m", "[33m", "[31m"]

rules = ["C-O1", "C-O3", "C-O4", "C-G1", "C-G2", "C-G3", "C-G4", "C-G5", "C-G6", "C-G7", "C-G8", "C-F2", "C-F3", "C-F4", "C-F5", "C-F6", "C-F8", "C-F9", "C-L2", "C-L3", "C-L4", "C-V1", "C-C1", "C-C3", "C-H1", "C-H2", "C-A3"]

descriptions = [
    ["Contents of the repository[0m", "The repository must not contain compiled, temporary or unnecessary files."],
    ["File coherence[0m", "A source file mustn't contain more than 5 functions."],
    ["Naming files and folders[0m", "All files names and folders must be in English, according the [3msnake_case[0m convention."],
    ["File header[0m", "C files and every Makefile must always start with the standard header of the school."],
    ["Separation of functions[0m", "Inside a source file, implementations of functions must be separated by one and only one empty line."],
    ["Indentation of reprocessor directives[0m", "The preprocessor directives must be indented according to the level of indirection."],
    ["Global variables[0m", "Global variables must be avoided as much as possible. Only global constants should be used."],
    ["[3minclude[0m", "[3minclude[0m directive must only include C header files."],
    ["Line endings[0m", "Line endings must be done in UNIX style (with [3m\\n[0m)."],
    ["Trailing spaces[0m", "No trailing spaces must be present at the end of a line."],
    ["Leading/trailing lines[0m", "No leading empty lines must be present. No more than 1 trailing empty line must be present."],
    ["Naming functions[0m", "The name of a function must define the task it executes and must contain a verb. All function names must be in English, according to the [3msnake_case[0m convention."],
    ["Number of columns[0m", "The length of a line must not exceed 80 columns."],
    ["Number of lines[0m", "The body of a function should be as short as possible, and must not exceed 20 lines."],
    ["Number of parameters[0m", "A function must not have more than 4 parameters."],
    ["Functions without parameters[0m", "A function taking no parameters must take void as a parameter in the function declaration."],
    ["Comments inside a function[0m", "There must be no comment within a function."],
    ["Nested functions[0m", "Nested functions are not allowed."],
    ["Indentation[0m", "Each indentation level must be done by using 4 spaces. No tabulations may be used for indentation."],
    ["Spaces[0m", "When using a space as a separator, one and only one space character must be used."],
    ["Curly brackets[0m", "Opening curly brackets must be at the end of the line, after the content it precedes, except for functions definitions where they must be placed alone on their line. Closing curly brackets must be alone on their line, except in the case of [3melse[0m/[3melse if[0m control structures, [3menum[0m declarations, or structure declarations."],
    ["Naming identifiers[0m", "All identifier names must be in English, according to the [3msnake_case[0m convention. The type names defined with [3mtypedef[0m must end with [3m_t[0m. The names of macros and global constants and the content of enums must be written in [3mUPPER_SNAKE_CASE[0m."],
    ["Conditional branching[0m", "A conditionnal block must not contain more than 3 branches."],
    ["[3mgoto[0m", "Using the [3mgoto[0m keyword if forbidden."],
    ["Content[0m", "Header files must only contain [1mfunctions prototypes[0m, [1mtypes declarations[0m, [1mglobal variable/constant declarations[0m, [1mmacros[0m, [1mstatic inline functions[0m. All these elements must only be found in header files, and thus not in source files."],
    ["Include guard[0m", "Headers must be protected from double inclusion."],
    ["Line break at the end of file[0m", "Files must end with a line break."]
]

bin_path = (f"/home/{os.getenv('USER')}/.local/bin/")

def set_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-Ee", "-Eerrors", "--exclude-errors", nargs = '+', help = "Exclude coding style errors from report")
    parser.add_argument("-Ef", "-Efiles", "--exclude-files", nargs = '+', help = "Exclude files from coding style checking")
    parser.add_argument("-w", "--watch", nargs = 1, help = "Watch for changes in the repository every x seconds")
    parser.add_argument("-v", "--version", action = "store_true", help = "Show Mango version")
    parser.add_argument("-u", "--update", action = "store_true", help = "Update Mango to last version")
    return parser.parse_args()

def download_coding_style():
    print("Downloading coding-style...\n")
    os.system(f"sudo wget https://raw.githubusercontent.com/Epitech/coding-style-checker/main/coding-style.sh -O {bin_path}coding-style 2> /dev/null")
    os.system(f"sudo chmod +x {bin_path}coding-style")

def update():
    os.system(f"sudo wget https://api.github.com/repos/Clement-Lnrd/Mango/tarball/{version} -O {bin_path}Mango-{version}.tar.gz 2> /dev/null")
    os.system(f"sudo tar -xzf {bin_path}Mango-{version}.tar.gz -C {bin_path}")
    os.system(f"sudo mv -f {bin_path}Clement-Lnrd-Mango-*/mango.py {bin_path}mango")
    os.system(f"sudo chmod +x {bin_path}mango")
    os.system(f"sudo rm -rf {bin_path}Mango-{version}.tar.gz {bin_path}Clement-Lnrd-Mango-*")
    print(changelog)
    exit()

def check_for_update():
    response = requests.get("https://api.github.com/repos/Clement-Lnrd/Mango/releases/latest")
    if (response):
        version = response.json()["name"]
    if (response and version != version):
        print("New version of Mango available. You can update it doing \"[3mmango -u, --update[0m\".\n")

def print_version():
    print(f"Mango {version}")
    exit()

def get_exclude_files(args):
    exclude = []
    if (not args.exclude_files):
        return exclude
    for file in args.exclude_files:
        if (os.path.isdir(file)):
            for root, subdirs, files in os.walk(file):
                for filename in files:
                    file = os.path.join(root, filename)
                    file = os.path.abspath(file)
                    exclude.append(file.strip())
        else:
            file = os.path.abspath(file)
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
    os.system("coding-style . /tmp/ > /dev/null")
    process = subprocess.Popen(["sudo", "cat", "/tmp/coding-style-reports.log"], stdout = subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode('utf-8')
    out = out.split('\n')
    os.system("sudo rm -f /tmp/coding-style-reports.log")
    return out

def print_error(line, index):
    color = ("[0m" + colors[types.index(line[2])])
    print(f"{color}[1m{line[0]}:{line[1]}: {line[3]}{color}\n{descriptions[index][0]}\n{descriptions[index][1]}\n")

def mango(exclude_files, exclude_errors, watch):
    out = coding_style()
    if (watch):
        os.system("clear")
    err_nb = [0, 0, 0]
    if (not out):
        if (not is_a_tty):
            print(f"{mango_ascii}    ✅ There is no coding style error")
        else:
            print(f"{mango_tty}    but you have no coding style error :)")
        return
    for line in out:
        if (line == ''):
            continue
        line = line.split(':')
        if (os.path.abspath(line[0]) in exclude_files or line[3] in exclude_errors):
            continue
        index = rules.index(line[3])
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
    if (err_nb[2] > 0 or err_nb[1] > 0 or err_nb[0] > 0):
        print(f"[1;31m{err_nb[2]} Major[0m | [1;33m{err_nb[1]} Minor[0m | [1;36m{err_nb[0]} Info[0m")
    elif (not is_a_tty):
        print(f"{mango_ascii}    ✅ There is no coding style error")
    else:
        print(f"{mango_tty}    but you have no coding style error :)")

def main():
    args = set_arguments()
    if (args.version):
        print_version()
    if (args.update):
        update()
    os.environ["PATH"] += (os.pathsep + bin_path)
    try:
        check_for_update()
    except:
        sys.stderr.write("Cannot check for update, please verify your internet connection.\n\n")
    if (which("coding-style") is None):
        download_coding_style()
    if (args.watch):
        while (True):
            try:
                mango(get_exclude_files(args), get_exclude_errors(args), args.watch)
                time.sleep(int(args.watch[0]))
            except KeyboardInterrupt:
                exit()
            except:
                exit(84)
    else:
        mango(get_exclude_files(args), get_exclude_errors(args), args.watch)

if __name__ == "__main__":
    is_a_tty = os.ttyname(1).split('/')[-1].startswith("tty")
    main()
