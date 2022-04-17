# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:09:57 2022

@author: dejong71
"""

#==============================================================================

from read_and_solve import read_and_solve
from Chapter01.Ex_01_11_04_Neighborhood.neighbors import neighbors

#==============================================================================

def get_freq_map_neighbors(genome : str, length : int, 
                              mismatches : int) -> dict[str]:
    '''
    Given a genome, generate the a frequency map of all patterns of a given
    length and all its similars, with at most the given number of mismatches.

    Parameters
    ----------
    genome : str
        The genome to search for mismatched patterns.
    length : int
        The length of the pattern to look for.
    mismatches : int
        The maximal amount of mismatches.

    Returns
    -------
    dict[str]
        A frequency map of all patterns with at most the given number of
        mismatches.
    '''
    freq_map = dict()
    for i in range(len(genome) - length + 1):
        # For every pattern, generate the all similars with mismatches.
        pattern = genome[i : i + length]
        neighborhood = neighbors(pattern, mismatches)
        for neighbor in neighborhood:
            try:
                freq_map[neighbor] += 1
            except KeyError:
                freq_map[neighbor] = 1
    return freq_map


def frequent_words_mismatches(genome : str, length : int, 
                              mismatches : int) -> set[str]:
    '''
    Given a genome, generate the pattern of a given length that occurs most, 
    and all it's similars, with at most the given number of mismatches.

    Parameters
    ----------
    genome : str
        The genome to search for mismatched patterns.
    length : int
        The length of the pattern to look for.
    mismatches : int
        The maximal amount of mismatches.

    Returns
    -------
    set[str]
        The most frequent pattern(s) with at most the given number of
        mismatches, listed in alphabetical order.
    '''
    # Data storage.
    patterns = set()
    freq_map = get_freq_map_neighbors(genome, length, mismatches)
    # Find all patterns with maximal frequency.
    freq_max = max(freq_map.values())
    for pattern, freq in freq_map.items():
        if freq == freq_max:
            patterns.add(pattern)
    return sorted(patterns)

#==============================================================================

if __name__ == '__main__':
    read_and_solve(frequent_words_mismatches)
    
#==============================================================================