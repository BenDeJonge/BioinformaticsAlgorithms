# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:40:12 2022

@author: dejong71
"""

#==============================================================================

import os
import tkinter as tk
from tkinter.filedialog import askopenfilename

#==============================================================================

def grab_args_from_file(fpath):
    with open(fpath, 'r') as f:
        args = []
        lines = [l.strip() for l in f.readlines()]
        for i, l in enumerate(lines):
            # For lines with only numbers, add the numbers as arguments.
            if l.replace(' ', '').isnumeric():
                for arg in l.split():
                    args.append(int(arg))
            # For lines with only strings, if a single string is listed add it
            # as argument. If a list of strings is given, add list as argument.
            else:
                text = l.split()
                if len(text) > 1:
                    args.append(text)
                else:
                    args.append(text[0])
    return args

#==============================================================================

def read_and_solve(fun : callable):
    root = tk.Tk()
    fpath = askopenfilename()
    try:
        args = grab_args_from_file(fpath)
        sol = fun(*args)
        with open(os.path.join(os.path.dirname(fpath),
                               'output.txt'), 'w') as f:
            f.write(' '.join(str(s) for s in sol ))
    except AttributeError:
        pass
    root.destroy()
    
#==============================================================================
    
#==============================================================================