# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:36:57 2022

@author: dejong71
"""

#==============================================================================

from Chapter01.Ex_01_08_03_HammingDistance.hamming_distance import hamming_distance
import os
import tkinter as tk
from tkinter.filedialog import askopenfile

#==============================================================================

def approximate_pattern_count(pattern : str, genome : str, 
                              mismatches : int) -> int:
    '''
    Given a genome, count the number a given pattern with a maximal amount of 
    mismatches is present.

    Parameters
    ----------
    pattern : str
        The pattern to look for.
    genome : str
        The genome to search in.
    mismatches : int
        The maximal amount of mismatches.

    Returns
    -------
    int
        The count the pattern.
    '''
    count = 0
    for i in range(len(genome) - len(pattern) + 1):
        fragment = genome[i : i + len(pattern)]
        if hamming_distance(fragment, pattern) <= mismatches:
            count += 1
    return count

#==============================================================================

if __name__ == '__main__':
    root = tk.Tk()
    try:
        with askopenfile() as f:
            folder = os.path.dirname(f.name)
            pattern, genome, mismatches = f.readlines()
            pattern, genome, mismatches = pattern.strip(), genome.strip(), int(mismatches)
        apc = approximate_pattern_count(pattern, genome, mismatches)
        with open(os.path.join(folder, 'output.txt'), 'w') as f:
            f.write(str(apc))
    except AttributeError:
        pass
    root.destroy()
    
#==============================================================================