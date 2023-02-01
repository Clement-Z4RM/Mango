#!/bin/python3

import sys
import os
import argparse
from shutil import which
import subprocess
import requests

types = [" INFO", " MINOR", " MAJOR"]

colors = ["\033[36m", "\033[33m", "\033[31m"]

rules = ["C-O1", "C-O3", "C-O4", "C-G1", "C-G2", "C-G3", "C-G4", "C-G5", "C-G6", "C-G7", "C-G8", "C-F2", "C-F3", "C-F4", "C-F5", "C-F6", "C-F8", "C-F9", "C-L2", "C-L3", "C-L4", "C-V1", "C-C1", "C-C3", "C-H1", "C-H2", "C-A3"]

descriptions = [
    ["Contents of the repository\033[0m", "The repository must not contain compiled, temporary or unnecessary files."],
    ["File coherence\033[0m", "A source file mustn't contain more than 5 functions."],
    ["Naming files and folders\033[0m", "All files names and folders must be in English, according the \033[3msnake_case\033[0m convention."],
    ["File header\033[0m", "C files and every Makefile must always start with the standard header of the school."],
    ["Separation of functions\033[0m", "Inside a source file, implementations of functions must be separated by one and only one empty line."],
    ["Indentation of reprocessor directives\033[0m", "The preprocessor directives must be indented according to the level of indirection."],
    ["Global variables\033[0m", "Global variables must be avoided as much as possible. Only global constants should be used."],
    ["\033[3minclude\033[0m", "\033[3minclude\033[0m directive must only include C header files."],
    ["Line endings\033[0m", "Line endings must be done in UNIX style (with \033[3m\\n\033[0m)."],
    ["Trailing spaces\033[0m", "No trailing spaces must be present at the end of a line."],
    ["Leading/trailing lines\033[0m", "No leading empty lines must be present. No more than 1 trailing empty line must be present."],
    ["Naming functions\033[0m", "The name of a function must define the task it executes and must contain a verb. All function names must be in English, according to the \033[3msnake_case\033[0m convention."],
    ["Number of columns\033[0m", "The length of a line must not exceed 80 columns."],
    ["Number of lines\033[0m", "The body of a function should be as short as possible, and must not exceed 20 lines."],
    ["Number of parameters\033[0m", "A function must not have more than 4 parameters."],
    ["Functions without parameters\033[0m", "A function taking no parameters must take void as a parameter in the function declaration."],
    ["Comments inside a function\033[0m", "There must be no comment within a function."],
    ["Nested functions\033[0m", "Nested functions are not allowed."],
    ["Indentation\033[0m", "Each indentation level must be done by using 4 spaces. No tabulations may be used for indentation."],
    ["Spaces\033[0m", "When using a space as a separator, one and only one space character must be used."],
    ["Curly brackets\033[0m", "Opening curly brackets must be at the end of the line, after the content it precedes, except for functions definitions where they must be placed alone on their line. Closing curly brackets must be alone on their line, except in the case of \033[3melse\033[0m/\033[3melse if\033[0m control structures, \033[3menum\033[0m declarations, or structure declarations."],
    ["Naming identifiers\033[0m", "All identifier names must be in English, according to the \033[3msnake_case\033[0m convention. The type names defined with \033[3mtypedef\033[0m must end with \033[3m_t\033[0m. The names of macros and global constants and the content of enums must be written in \033[3mUPPER_SNAKE_CASE\033[0m."],
    ["Conditional branching\033[0m", "A conditionnal block must not contain more than 3 branches."],
    ["\033[3mgoto\033[0m", "Using the \033[3mgoto\033[0m keyword if forbidden."],
    ["Content\033[0m", "Header files must only contain \033[1mfunctions prototypes\033[0m, \033[1mtypes declarations\033[0m, \033[1mglobal variable/constant declarations\033[0m, \033[1mmacros\033[0m, \033[1mstatic inline functions\033[0m. All these elements must only be found in header files, and thus not in source files."],
    ["Include guard\033[0m", "Headers must be protected from double inclusion."],
    ["Line break at the end of file\033[0m", "Files must end with a line break."]
]

bin_path = (f"/home/{os.getenv('SUDO_USER')}/.local/bin/")

def execute_as_sudo():
    args = (['sudo'] + sys.argv + [os.environ])
    os.execlpe('sudo', *args)

def set_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-Ee", "--exclude-errors", nargs = '+', help = "Exclude coding style errors from report")
    parser.add_argument("-Ef", "--exclude-files", nargs = '+', help = "Exclude files from coding style checking")
    parser.add_argument("-v", "--version", action = "store_true", help = "Show Mango version")
    parser.add_argument("-u", "--update", action = "store_true", help = "Update Mango to last version")
    return parser.parse_args()

def download_coding_style():
    print("Downloading coding-style...\n")
    os.system(f"wget https://raw.githubusercontent.com/Epitech/coding-style-checker/main/coding-style.sh -O {bin_path}coding-style 2> /dev/null")
    os.system(f"chmod +x {bin_path}coding-style")

def update(args):
    response = requests.get("https://api.github.com/repos/Clement-Lnrd/Mango/releases/latest")
    if (response):
        version = response.json()["name"]
    if (args.update):
        os.system(f"wget https://api.github.com/repos/Clement-Lnrd/Mango/tarball/{version} -O {bin_path}Mango-{version}.tar.gz 2> /dev/null")
        os.system(f"tar -xzf {bin_path}Mango-{version}.tar.gz -C {bin_path}")
        os.system(f"mv -f {bin_path}Clement-Lnrd-Mango-*/mango.py {bin_path}mango")
        os.system(f"chmod +x {bin_path}mango")
        os.system(f"rm -rf {bin_path}Mango-{version}.tar.gz {bin_path}Clement-Lnrd-Mango-*")
        exit()
    if (response and version != "v1.0.2"):
        print("New version of Mango available. You can update it doing \"\033[3mmango -u, --update\033[0m\".\n")

def print_version():
    print("Mango v1.0.2")
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
    process = subprocess.Popen(["cat", "/tmp/coding-style-reports.log"], stdout = subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode('utf-8')
    out = out.split('\n')
    os.system("rm -f /tmp/coding-style-reports.log")
    return out

def print_error(line, index):
    color = ("\033[0m" + colors[types.index(line[2])])
    print(f"{color}\033[1m{line[0]}:{line[1]}: {line[3]}{color}\n{descriptions[index][0]}\n{descriptions[index][1]}\n")

def mango(exclude_files, exclude_errors):
    out = coding_style()
    err_nb = [0, 0, 0]
    if (not out):
        print("✅ There isn't coding style error")
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
        print(f"\033[1;31m{err_nb[2]} Major\033[0m | \033[1;33m{err_nb[1]} Minor\033[0m | \033[1;36m{err_nb[0]} Info\033[0m")
    else:
        print("✅ There isn't coding style error")

def main():
    args = set_arguments()
    if (os.geteuid() != 0):
        execute_as_sudo()
    os.environ["PATH"] += (os.pathsep + bin_path)
    update(args)
    if (args.version):
        print_version()
    if (which("coding-style") is None):
        download_coding_style()
    mango(get_exclude_files(args), get_exclude_errors(args))

if __name__ == "__main__":
    main()
