# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 23:30:19 2022

@author: dejong71
"""

#==============================================================================

import os
import file_reader as fr
import unittest

#==============================================================================

class TestListEquality(unittest.TestCase):
    '''
    Unittest for equality of counts.
    '''
    def test_counts_outputs(self):
        self.assertEqual(counts, control)

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

if __name__ == '__main__':
    # Grabbing files.
    path = os.path.dirname(__file__)
    inputs = fr.read_folder(os.path.join(path, 'inputs'))
    outputs = fr.read_folder(os.path.join(path, 'outputs'))
    # Reading outputs.
    control = []
    for file in outputs:
        with open(file, 'r') as f:
            control.append( int(f.read() ))
    # Calculating counts.
    counts = []
    for file in inputs:
        with open(file, 'r') as f:
            text, pattern = f.read().splitlines()
            counts.append(pattern_count(text, pattern))
    # Testing equality.
    unittest.main()
    
#==============================================================================