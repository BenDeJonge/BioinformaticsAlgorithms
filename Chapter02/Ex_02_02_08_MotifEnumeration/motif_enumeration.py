# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:33:44 2022

@author: dejong71
"""

#==============================================================================

from read_and_solve import read_and_solve
from Chapter01.Ex_01_08_09_FrequentWordsMismatches.frequent_words_mismatches \
    import get_freq_map_neighbors

#==============================================================================

def motif_enumeration(length : int, mismatches : int, 
                      genes : list[str], ) -> set[str]:
    '''
    Given a list of genes, find all patterns of a given length that appear in 
    all genes with at most a given number of mismatches.

    Parameters
    ----------
    genes : list[str]
        List of genes in string format.
    length : int
        The length of the pattern to look for.
    mismatches : int
        The maximal amount of mismatches a found pattern can have.

    Returns
    -------
    set[str]
        All found patterns that satisfy the criteria.
    '''
    candidates = dict()
    for gene in genes:
        freq_map = get_freq_map_neighbors(gene, length, mismatches)
        candidates[gene] = set(freq_map.keys())
    return candidates[genes[0]].intersection(*candidates.values())

#==============================================================================

if __name__ == '__main__':
    read_and_solve(motif_enumeration)
    
#==============================================================================