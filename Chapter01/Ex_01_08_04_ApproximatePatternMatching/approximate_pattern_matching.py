# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 22:52:02 2022

@author: dejong71
"""

#==============================================================================

from Chapter01.Ex_01_08_03_HammingDistance.hamming_distance import hamming_distance
import os
import tkinter as tk
from tkinter.filedialog import askopenfile

#==============================================================================

def approximate_pattern_matching(pattern : str, genome : str, 
                                 mismatches : int) -> list[int]:
    '''
    Given a genome and a pattern, return the starting indices of fragments in 
    the genome, that closely resemble the pattern, with at most a given number
    of mismatches.

    Parameters
    ----------
    pattern : str
        The approixmate pattern to look for.
    genome : str
        The genome to look in.
    distance : int
        The maximal Hamming distance between found fragments and the defined 
        pattern.

    Returns
    -------
    list[int]
        Starting indices of all found fragments.
    '''
    starts = []
    for i in range(len(genome) - len(pattern) + 1):
        fragment = genome[i : i + len(pattern)]
        if hamming_distance(fragment, pattern) <= mismatches:
            starts.append(i)
    return starts

#==============================================================================

if __name__ == '__main__':
    root = tk.Tk()
    try:
        with askopenfile() as f:
            folder = os.path.dirname(f.name)
            pattern, genome, mismatches = f.readlines()
            pattern, genome, mismatches = pattern.strip(), genome.strip(), int(mismatches)
        apm = approximate_pattern_matching(pattern, genome, mismatches)
        with open(os.path.join(folder, 'output.txt'), 'w') as f:
            f.write( ' '.join(str(i) for i in apm) )
    except AttributeError:
        pass
    root.destroy()

#==============================================================================