# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:47:39 2022

@author: dejong71
"""

#==============================================================================

import tkinter as tk
from tkinter.filedialog import askopenfile
import os
from Chapter01.Ex_01_08_03_HammingDistance.hamming_distance import hamming_distance

#==============================================================================

def neighbors(pattern : str, mismatches : int) -> set[str]:
    '''
    Given a pattern and a maximal number of mismatches, construct a set of all
    patterns of which the Hamming distance is at equal or smaller than the 
    number of mismatches.

    Parameters
    ----------
    pattern : str
        The pattern to construct the neighborhood of.
    mismatches : int
        The maximal amount of mismatches any given neighbor can have.

    Returns
    -------
    set[str]
        The neighborhood of the pattern, containing all strings with at most
        the given number of mismatches.
    '''
    # Recursion boundary conditions.
    if mismatches == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    # Proceed with recursion.
    else:
        neighborhood = set()
        # Recursively loop through the pattern, always removing the first base.
        suffix_neighbors = neighbors(pattern[1:], mismatches)
        for neighbor in suffix_neighbors:
            # The suffix does not exceed the number of mismatches.
            # Put any base at start.
            if hamming_distance(pattern[1:], neighbor) <  mismatches:
                for base in tuple('ACGT'):
                    neighborhood.add(base + neighbor)
            # The suffix has the max amount of mismatches.
            # Put the first base of the pattern at the start.
            else:
                neighborhood.add(pattern[0] + neighbor)
        return neighborhood
    
#==============================================================================

if __name__ == '__main__':
    root = tk.Tk()
    try:
        with askopenfile() as f:
            folder = os.path.dirname(f.name)
            pattern, mismatches = f.read().split()
            mismatches = int(mismatches)
        ns = neighbors(pattern, mismatches)
        with open(os.path.join(folder, 'output.txt'), 'w') as f:
            f.write( ' '.join( str(n) for n in ns) )
    except AttributeError:
        pass
    root.destroy()
    
#==============================================================================