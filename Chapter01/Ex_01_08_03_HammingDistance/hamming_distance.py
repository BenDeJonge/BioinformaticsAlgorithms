# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 22:14:17 2022

@author: dejong71
"""

#==============================================================================

import tkinter as tk
from tkinter.filedialog import askopenfile

#==============================================================================

def hamming_distance(s1 : str, s2 : str) -> int:
    '''
    Given 2 strings of equal length, return the amount of characters in which
    they differ.

    Parameters
    ----------
    s1 : str
        The first string.
    s2 : str
        The second string.

    Returns
    -------
    int
        The Hamming distance between both strings.
    '''
    distance = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            distance += 1
    return distance

#==============================================================================

if __name__ == '__main__':
    root = tk.Tk()
    try:
        with askopenfile() as f:
            s1, s2 = f.readlines()
            hd = hamming_distance(s1, s2)
            print(hd)
    except AttributeError:
        pass
    root.destroy()
    
#==============================================================================