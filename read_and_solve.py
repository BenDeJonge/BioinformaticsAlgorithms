# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:40:12 2022

@author: dejong71
"""

#==============================================================================

import os
import tkinter as tk
from tkinter.filedialog import askopenfile

def read_and_solve(fun : callable):
    root = tk.Tk()
    try:
        with askopenfile() as f:
            folder = os.path.dirname(f.name)
            args = f.read().split()
            for i, arg in enumerate(args):
                try:
                    args[i] = int(arg)
                except ValueError:
                    pass
        sol = fun(*args)
        with open(os.path.join(folder, 'output.txt'), 'w') as f:
            f.write(' '.join(str(s) for s in sol ))
    except AttributeError:
        pass
    root.destroy()
    
#==============================================================================