# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 23:19:18 2022

@author: dejong71
"""

import os
import glob
import tkinter as tk
from tkinter.filedialog import askopenfilename

#==============================================================================

def read_folder(path, ext='txt'):
    '''Simple function to return all files with some extention in a folder.'''
    files = glob.glob(os.path.join(os.path.abspath(path), 
                                   f'*.{ext}'))
    return files

#==============================================================================
   
def grab_args_from_file(fpath):
    '''Grab text from file and format as arguments to pass onto a callable.'''
    with open(fpath, 'r') as f:
        args = []
        lines = [l.strip() for l in f.readlines()]
        for i, l in enumerate(lines):
            # For lines with only numbers, add the numbers as arguments.
            if l.replace(' ', '').isnumeric():
                for arg in l.split():
                    args.append(int(arg))
            # For lines with only strings, if a single string is listed add it
            # as argument. If a list of strings is given, add set as argument.
            else:
                text = l.split()
                if len(text) > 1:
                    print('making set')
                    args.append(text)
                else:
                    args.append(text[0])
    return args

#==============================================================================

def read_and_solve(fun : callable):
    '''GUI to select a file to solve.'''
    root = tk.Tk()
    fpath = askopenfilename()
    try:
        args = grab_args_from_file(fpath)
        sol = fun(*args)
        with open(os.path.join(fpath, 'output.txt'), 'w') as f:
            f.write(' '.join(str(s) for s in sol ))
    except AttributeError:
        pass
    root.destroy()
    
#==============================================================================

def read_and_solve_all(fun : callable, path):
    '''Solve all files in folder.'''
    # Grabbing files.
    inputs = read_folder(os.path.join(path, 'inputs'))
    outputs = read_folder(os.path.join(path, 'outputs'))
    # Reading outputs.
    control = []
    for file in outputs:
        args = grab_args_from_file(file)
        control.append(args)
    # Calculating counts.
    result = []
    for file in inputs:
        args = grab_args_from_file(file)
        result.append(fun(*args))
    return control, result

#==============================================================================