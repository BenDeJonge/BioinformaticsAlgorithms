# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 13:43:15 2022

@author: dejong71
"""

#==============================================================================

genes = ["atgaccgggatactgataaaaaaaagggggggggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccg",
         "acccctattttttgagcagatttagtgacctggaaaaaaaatttgagtacaaaacttttccgaataaaaaaaaaggggggga",
         "tgagtatccctgggatgacttaaaaaaaagggggggtgctctcccgatttttgaatatgtaggatcattcgccagggtccga",
         "gctgagaattggatgaaaaaaaagggggggtccacgcaatcgcgaaccaacgcggacccaaaggcaagaccgataaaggaga",
         "tcccttttgcggtaatgtgccgggaggctggttacgtagggaagccctaacggacttaataaaaaaaagggggggcttatag",
         "gtcaatcatgttcttgtgaatggatttaaaaaaaaggggggggaccgcttggcgcacccaaattcagtgtgggcgagcgcaa",
         "cggttttggcccttgttagaggcccccgtaaaaaaaagggggggcaattatgagagagctaatctatcgcgtgcgtgttcat",
         "aacttgagttaaaaaaaagggggggctggggcacatacaagaggagtcttccttatcagttaatgctgtatgacactatgta",
         "ttggcccattggctaaaagcccaacttgacaaatggaagatagaatccttgcataaaaaaaagggggggaccgaaagggaag",
         "ctggtgagcaacgacagattcttacgtgcattagctcgcttccggggatctaatagcacgaagcttaaaaaaaaggggggga"]
length = 15

#==============================================================================

def find_common_patterns(genes : set, length : int) -> set:
    '''
    Given a set of genes, return a set of patterns found in all genes.

    Parameters
    ----------
    genes : set
        The set of genes to look for common patterns.
    length : int
        The length of the pattern to look for.

    Returns
    -------
    set
        The found common patterns.
    '''
    total = dict()
    for gene in genes:
        patterns = set()
        for i in range(len(gene) - length):
            patterns.add( gene[ i : i + length] )
        total[gene] = patterns    
    return total[genes[0]].intersection(*total.values())

#==============================================================================

common = find_common_patterns(genes, length)

#==============================================================================