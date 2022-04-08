# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 23:22:37 2022

@author: dejong71
"""

#==============================================================================

from Chapter01.Ex_01_02_13_FrequentWords.frequent_words import get_frequency_table

#==============================================================================

def clump_finding(genome : str, length : int, 
                  window : int, counts : int) -> list:
    '''
    Given a genome and a window size, find all substrings of a given length
    that occur at least a given amount.

    Parameters
    ----------
    genome : str
        The full genome.
    length : int
        The length of the substrings to be found.
    window : int
        The slice of the genome to actually search in.
    counts : int
        The minimal amount of occurences of the substring.

    Returns
    -------
    list
        All substrings that satisfy the length and counts criteria inside the 
        window slice of the genome.
    '''
    clumps = set()
    for i in range( len(genome) - window + 1):
        table = get_frequency_table(text = genome[ i : i + window], 
                                    k = length)
        for fragment, count in table.items():
            if count >= counts:
                clumps.add(fragment)
    return clumps

#==============================================================================

if __name__ == '__main__':
    genome = 'TAGTAACCTCAAAGGATCGTGCAACCCTCGTAGTAGTAAGGTATTTTATTGCGGTAGGTTAGGGCTGTTTACTAGCCCATGACGCTCACTGTATCTGAGTGATTTGCCTGTCAAAACGCTTAGGGGCCTCAAAGGGTATCCCTAGTTAATATGCTGGAACAAGTGACTAATTAAACTTCGTATCGGCGTCTCCCTTAGCCCTACAATATCGTGTGGGGCTCCGGGCGGGGCTCCGGGCTCCCCTAAACCAGTAACGTCAACTGTACCTGGGTGGGTGGCGATATGGTGGCGATGCGATGTTTGGTTGTTACAACGTCGGGGAGACACAGAAGGCGTGGTCACCCACGAGACGGAGGTCGCCCCGGATACCGGTCATGTATATAATAATGCCGGGTAAGCCGGCCTTTCCCATGAGAGGTTGATCTAAGGTGTAAAGCGAAATGCTAGTCCGACAGCTCAAATATGCTCAGGTACGGGCGATGAGACGCACCACTGATGTAGGATACCAGTGGGCTTAATGTAAGGAACCAACCGACCGAGCACATTTGTTGAGCTCCCGGCAGATTCCTTGTTAGGTTGGGGCACGAGCTTGTGCCGGCCTAGATTGAATCAGGAGGCATCCGTTGGGGTCAGCCCGTCTGTATCACAGTGAACCCCCCACCTATTTACAGTCTAGAGTGGATCGGAAGCAGACTTGGGGACAGTCAAGCCATATACCACAAGCAACTGAGGCCCACCGGCACGTTCCCCCAACACGAGGTCGCTTGCGGTCGCTTTCGCTTACATGCCCCGACAAAGGCATTGGGCGCTCACTGCGATATTCCAAATCGTAGAGATTGTAACCGGCCGTGCCAATTCGTACTCCGATGGCTGGCCATCTAATGATTGTGGCGAGACAACTTAATACTTTGCTAATCCTAATGCTAATCTCCTAATCTTGCCTTACTTCCGAGCAGTAGCCCGCTGTTTAACCGGGGGGATTACCGTTTTCGTCTAGGTGTCTGCTGACAGCAAGCAAGATCCGCGCAAGATCCATAAGAGCCCATCGTCTAGGTCGACTAGATGAGAAGCCGTTCAGGTCACAGTATAGACAAACTACTCGACCTTAAGAAGCGAGGGCGCCACAATGTTACTATGCGAGCACTGAATGGGTTGTTTCTGGTGGTAATGGTCTCCTAGTTCTGACCGAGAACAGCGAGTGTGGTCGATAAAATAAAGGCTAAAGGCTAGTACGAACTGTTACAATTGGACGTGTAACAGTTTGACTTAGTTTGACAGTTTGAGGTGATGAGTGGGTGGGTGATGAATGATGAGTATGGCCAACTGCCGAATTTTCCTTGTTTTGTGCAACCACTATTGTTTCTACATCCTCCCGGCTGGATCGATTGATACGCCTCATTTTCTGCTTCACTTAAAGCATGTGTGAGGAGTTCTGTGGAGTATTCTGAAAACCCATACACCCCGCGTTGTTATTATGGCTCAGGCGCTCAGGCGCCAGGCATGTAAAACCAATTCTCATGCGGGATAACCGCAGAATGTCCTGACAGGAGTTCGCCACAAACGTTACTTTAAATCGTCGTGTATATTCCATACGTTTCACAAGTTCATGGTATACCAATCTTGGCTTTGAGTATTCTGGACCCATGAAGCATGTTACGATTAATAATCGGGGAGGATACGGGGGGGATAACGTAGTGCGTAGTACGTAGTGGTCGCGAATTGGCGGTGCCGGTACCGGGACGACACAAGTCTCACGGAGGACAGGAATCAGGTTAGGCCAATGGTAACGGCAACCTCGCTATGTAGATTGGTTTTTACACACAGTGAAAGCCAAATAGGTGTAGTTCTTACGTGGGTAACACGTGACGTGGGTGTGGGT'
    length = 8
    window = 29
    counts = 4
    
    clumps = clump_finding(genome, length, window, counts)