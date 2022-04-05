# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 23:30:19 2022

@author: dejong71
"""

#==============================================================================

def pattern_count(text : str, pattern : str) -> int:
    '''
    Given a text and pattern string, return the amount of times the pattern is
    found in the text. Overlapping sequences count double.

    Parameters
    ----------
    text : str
        The text to match to.
    pattern : str
        The pattern to look for.

    Returns
    -------
    int
        The amount of times the pattern is found in the text.
    '''
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i : i + len(pattern)] == pattern:
            count += 1
    return count

#==============================================================================