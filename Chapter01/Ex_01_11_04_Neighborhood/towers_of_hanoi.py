# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 01:04:12 2022

@author: dejong71
"""

def towers_of_hanoi(disks : int, start : int, destination : int, count : int) -> int:
    '''
    Algorithm to solve the Towers of Hanoi puzzle.

    Parameters
    ----------
    disks : int
        The amount of disks not yet in the destination.
    start : int
        The starting peg.
    destination : int
        The destination peg.
    count : int
        The current move count.
        
    Returns
    -------
    int
        The amount of required moves.
    '''
    # Recursion boundary condition.
    if disks > 0:
        count += 1
        # Move top disk from start to transit.
        count = towers_of_hanoi(disks-1, start, destination, count)
        transit = 6 - start - destination
        # Move top disk from transit to destination.
        count = towers_of_hanoi(disks-1, transit, destination, count)
    return count

m = towers_of_hanoi(3, 1, 3, 0)
print(m)
