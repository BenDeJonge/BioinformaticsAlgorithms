# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:07:58 2022

@author: dejong71
"""

#==============================================================================

from Chapter01.Ex_01_08_03_HammingDistance.hamming_distance \
    import hamming_distance
from math import inf
from Utility.file_reader import read_and_solve

#==============================================================================

def distance_between_pattern_and_strings(pattern : str,
                                         strings : list[str]) -> int:
    '''
    Given a pattern and a set of strings, find the total distance the set has
    to the pattern. E.g. pattern = 'AAA', strings = ['AATCGT', 'AAATCG']
    Distance pattern-strings[0] = 1. Distance pattern strings[1] = 0.
    Total distance = 1 + 0 = 1.

    Parameters
    ----------
    pattern : str
        The pattern to look for.
    strings : list[str]
        List of genes to look inside for the pattern.

    Returns
    -------
    tot_dist : int
        The total distance the strings are from the pattern.
    '''
    length = len(pattern)
    tot_dist = 0
    for string in strings:
        best_dist = inf
        for i in range(len(string) - length + 1):
            window = string[i : i + length]
            curr_dist = hamming_distance(pattern, window) 
            if curr_dist < best_dist:
                best_dist = curr_dist
        tot_dist += best_dist
    return tot_dist

#==============================================================================

if __name__ == '__main__':
    read_and_solve(distance_between_pattern_and_strings)
    
#==============================================================================