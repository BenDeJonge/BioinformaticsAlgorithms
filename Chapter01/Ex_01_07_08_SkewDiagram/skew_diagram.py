# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 15:41:38 2022

@author: dejong71
"""

def skew_diagram(genome : str) -> list[int]:
    '''
    Given a genome, calculate the GC-skew along the whole sequence.

    Parameters
    ----------
    genome : str
        The sequence for which to calculate the GC-skew.

    Returns
    -------
    list[int]
        The current GC-skew at each individual index.
    '''
    skews = [0]
    for base in genome:
        if base == 'C':
            skews.append(skews[-1] - 1)
        elif base == 'G':
            skews.append(skews[-1] + 1)
        else: 
            skews.append(skews[-1])
    return skews

genome = 'GAGCCACCGCGATA'
skews = skew_diagram(genome)