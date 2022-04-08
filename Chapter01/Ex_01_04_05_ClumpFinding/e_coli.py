# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 00:45:45 2022

@author: dejong71
"""

#==============================================================================

from Chapter01.Ex_01_04_05_ClumpFinding.clump_finding import clump_finding
import os
import time

#==============================================================================

path = os.path.dirname(__file__)
with open( os.path.join(path, 'e_coli.txt'), 'r' ) as f:
    genome = f.read().strip()

length = 9
window = 500
counts = 3

#==============================================================================

# NAIVE: we loop over every window individually, which is too cumbersome for 
# long genomes. By tracking the start indices of all patterns in one go, we can
# then simply select for patterns that occur a sufficient amount of times. 
# Finally, we need to select for non-overllaping patterns that fall within a 
# single window, to end up with clumps.

# FINDS 1904 CLUMPS IN 925.97 s.
# start = time.time()
# clumps = clump_finding(genome, length, window, counts)
# end = time.time()
# print(f'Found {len(clumps)} clumps in {end - start :.2f} s.')

#==============================================================================

def positions_table(genome : str, length : int) -> dict[str, list[int]]:
    '''
    Given a genome, return the starting positions of all fragments with a given 
    length as a dictionary.

    Parameters
    ----------
    genome : str
        The genome to search in.
    length : int
        The exact fragment length to search for.

    Returns
    -------
    dict[str, list[int]]
        A table of all fragments of a given length and their starting indices.
    '''
    table = {}
    for i in range(len(genome) - length + 1):
        pattern = genome[ i : i + length]
        try:
            table[pattern].append(i)
        except KeyError:
            table[pattern] = [i]
    return table

#==============================================================================

def is_clump(positions : list[int], length : int,
             window    : int,       counts : int) -> bool:
    '''
    Check if any subset of the positions, of size equal to the expected counts,
    falls inside the same window of the genome.
    
    Example: 4 positions [p1, p2, p3, p4], indicating patterns of length L.
              Looking for 3 counts inside window of size W.
              Loop 4 - 3 + 1 = 2 times.
    
    Loop0 : Check if [p1, p2, p3] are inside the same window.
    positions[0 + 3 - 1] = p3 vs positions[0] = p1
    Check if p3 - p1 <= W - L
    If ok, the positions correspond to a clump. If not, try the next loop.
    
    Loop1 : Check if [p2, p3, p4] are inside the same window.
    positions[1 + 3 - 1] = p4 vs positions[1] = p2
    Check if p4 - p1 <= W - L
    If ok, the positions correspond to a clump. If not, they dont.
    
    
    Parameters
    ----------
    positions : list[int]
        A list of all starting indices of the pattern.
    length : int
        The length of the pattern.
    window : int
        The window size to search inside the genome.
    counts : int
        The minimal amount of occurences of the pattern in the window.

    Returns
    -------
    bool
        If the pattern is a clump (True) or not (False).
    '''
    for i in range(len(positions) - counts + 1):
        if positions[i + counts - 1] - positions[i] <= window - length:
            return True
    return False

#==============================================================================

def fast_clump_finding(genome : str, length : int, 
                       window : int, counts : int) -> set[str]:
    '''
    Given a genome, look for patterns of a given length inside a genome window
    that appear at least a given amount of counts.

    Parameters
    ----------
    genome : str
        The genome to search in.
    length : int
        The exact fragment length to search for.
    window : int
        The window size to search inside the genome.
    counts : int
        The minimal amount of occurences of the pattern in the window.

    Returns
    -------
    set[str]
        A set of all patterns that are found as clumps in the genome.
    '''
    pt = positions_table(genome, length)
    clumps = set()
    for pattern, positions in pt.items():
        if len(positions) >= counts:
            if is_clump(positions, length, window, counts):
                clumps.add(pattern)
    return clumps

#==============================================================================

# FINDS 1904 CLUMPS IN 3.23 s (287x faster!).
start = time.time()
clumps = fast_clump_finding(genome, length, window, counts)
end = time.time()
print(f'Found {len(clumps)} clumps in {end - start :.2f} s.')

#==============================================================================