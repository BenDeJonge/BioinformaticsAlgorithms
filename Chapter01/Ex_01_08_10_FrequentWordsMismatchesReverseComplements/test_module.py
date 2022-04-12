# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:24:34 2022

@author: dejong71
"""

#==============================================================================

import os
import file_reader as fr
import unittest

from Chapter01.Ex_01_08_10_FrequentWordsMismatchesReverseComplements.frequent_words_mismatches_reverse_complements \
    import frequent_words_mismatches_reverse_complements as fun

#==============================================================================

class TestEquality(unittest.TestCase):
    '''
    Unittest for equality of counts.
    '''
    def test_presence(self):
        self.assertTrue(bool(result), 'Check presence of result.')
        self.assertTrue(bool(control), 'Check presence of control.')
    
    def test_counts_outputs(self):
        self.assertEqual(result, control, 'Check equality of result and control.')

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
            control.append( sorted(set(f.read().split())) )
    # Calculating counts.
    result = []
    for file in inputs:
        with open(file, 'r') as f:
            genome, length, mismatches = f.read().split()
        r = fun(genome, int(length), int(mismatches))
        result.append( r )
    # Testing equality.
    unittest.main()
    
#==============================================================================