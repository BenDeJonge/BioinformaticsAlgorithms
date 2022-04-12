# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:32:45 2022

@author: dejong71
"""

#==============================================================================

from Chapter01.Ex_01_08_10_FrequentWordsMismatchesReverseComplements.frequent_words_mismatches_reverse_complements \
    import frequent_words_mismatches_reverse_complements
from Chapter01.Ex_01_07_10_MinimumSkew.minimum_skew import minimum_skew
from Chapter01.Ex_01_03_02_ReverseComplement.reverse_complement import reverse_complement
import os
   
#==============================================================================

# Load in the full genome.
path = os.path.join( os.path.dirname(__file__), 'ecoli.txt')
with open(path, 'r') as f:
    genome = f.read().strip()
# Ori located in narrow window around transition from G-rich to C-rich.
start = min(minimum_skew(genome))
end = start + 500
window = genome[start:end]
# Define parameter for ori querry.
length = 9
mismatches = 1
potential_dnaa = frequent_words_mismatches_reverse_complements(window, length, mismatches)

actual_dnaa = [ dnaa for dnaa in potential_dnaa if dnaa in window ]

print(actual_dnaa)

#==============================================================================