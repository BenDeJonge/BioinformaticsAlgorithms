# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:30:58 2022

@author: dejong71
"""

#==============================================================================

from Chapter01.Ex_01_07_08_SkewDiagram.skew_diagram import skew_diagram
import tkinter as tk
from tkinter.filedialog import askopenfile

#==============================================================================

def minimum_skew(genome: str) -> list[int]:
    '''
    Given a genome, find all locations where the skew is minimal. Skew for a
    fragment of length i is defined as the total G-C count.

    Parameters
    ----------
    genome : str
        The genome to search for skews.

    Returns
    -------
    list[int]
        The skew values for all subfragments.
    '''
    skews = skew_diagram(genome)
    min_skew = min(skews)
    indices = []
    
    i = 0
    while i < len(skews) - 1:
        fragment = skews[i:]
        try:
            i_new = i + fragment.index(min_skew)
            indices.append(i_new)
            i = i_new + 1
        except ValueError:
            return indices

#==============================================================================

if __name__ == '__main__':
    root = tk.Tk()
    try:
        with askopenfile() as f:
            genome = f.read().strip()
            ms = minimum_skew(genome)
            print(ms)
    except AttributeError:
        pass
    root.destroy()