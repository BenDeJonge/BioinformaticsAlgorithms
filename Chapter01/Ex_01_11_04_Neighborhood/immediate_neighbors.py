# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 00:04:28 2022

@author: dejong71
"""

def immediate_neighbors(pattern : str) -> list[str]:
    '''
    Given a pattern, generate a list of all neighbors that have exactly one 
    mismatch with the original pattern.

    Parameters
    ----------
    pattern : str
        The string to generate neighbors from.

    Returns
    -------
    list[str]
        A list of neighbors with exactly one mismatch from the pattern.
    '''
    pattern = pattern.upper()
    neighborhood = []
    alphabet = 'ACGT'
    for i, base in enumerate(pattern):
        for replace in alphabet.replace(base, ''):
            neighbor = pattern[:i] + replace + pattern[i+1:]
            neighborhood.append(neighbor)
    return neighborhood

nbh = immediate_neighbors('acgt')