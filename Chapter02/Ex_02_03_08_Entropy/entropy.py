# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 01:35:03 2022

@author: dejong71
"""

#==============================================================================

import math

#==============================================================================

motifs = ['TCGGGGGTTTTT', 'CCGGTGACTTAC', 'ACGGGGATTTTC', 'TTGGGGACTTTT',
          'AAGGGGACTTCC', 'TTGGGGACTTCC', 'TCGGGGATTCAT', 'TCGGGGATTCCT',
          'TAGGGGAACTAC', 'TCGGGTATAACC']

def get_counts(motifs : list[str]) -> dict[dict[str, float]]:
    counts = dict()
    for i, bases in enumerate(zip(*motifs)):
        acgt = { b : 0 for b in tuple('ACGT') }
        for base in bases:
            acgt[base] += 1/len(motifs)
        counts[i] = acgt
    return counts

def column_entropy(column : list) -> float:
    entropy = 0
    for val in column:
        try:
            entropy -= val * math.log2(val)
        except ValueError:
            pass
    return entropy

def entropy(motifs : list[str]) -> float:
    counts = get_counts(motifs)
    entropy = 0
    for i, column in counts.items():
        entropy += column_entropy(column.values())
    return entropy

e = entropy(motifs)

#==============================================================================