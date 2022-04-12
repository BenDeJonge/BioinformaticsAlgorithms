# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:52:46 2022

@author: dejong71
"""

#==============================================================================

from read_and_solve import read_and_solve
from Chapter01.Ex_01_03_02_ReverseComplement.reverse_complement import reverse_complement
from Chapter01.Ex_01_11_04_Neighborhood.neighbors import neighbors

#==============================================================================

def frequent_words_mismatches_reverse_complements(genome : str,
                                                  length : int,
                                                  mismatches : int) -> set[str]:
    '''
    Given a genome, generate the set of all patterns of a given length that 
    occur the most in the genome. Found instances can have at most a given 
    number of mismatches. Reverse complements are also accepted.

    Parameters
    ----------
    genome : str
        The genome to search in.
    length : int
        The length of the patterns to look for.
    mismatches : int
        The maximal amount of mismatches a pattern can have.

    Returns
    -------
    set[str]
        The most occuring patterns and their reverse complements.

    '''
    # Data storage.
    patterns = set()
    freq_map = dict()
    for strand in (genome, reverse_complement(genome)):
        for i in range(len(genome) - length + 1):
            # For every pattern, generate the all similars with mismatches.
            pattern = strand[i : i + length]
            neighborhood = neighbors(pattern, mismatches)
            for neighbor in neighborhood:
                try:
                    freq_map[neighbor] += 1
                except KeyError:
                    freq_map[neighbor] = 1
    # Find all patterns with maximal frequency.
    freq_max = max(freq_map.values())
    for pattern, freq in freq_map.items():
        if freq == freq_max:
            patterns.add(pattern)
    return sorted(patterns)

#==============================================================================

if __name__ == '__main__':
    read_and_solve(frequent_words_mismatches_reverse_complements)
    
#==============================================================================