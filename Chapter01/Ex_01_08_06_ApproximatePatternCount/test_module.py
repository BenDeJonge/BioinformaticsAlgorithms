# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:43:00 2022

@author: dejong71
"""

#==============================================================================

import os
import file_reader as fr
import unittest

from Chapter01.Ex_01_08_06_ApproximatePatternCount.approximate_pattern_count import approximate_pattern_count as fun

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
            control.append( f.read() )
    # Calculating counts.
    result = []
    for file in inputs:
        with open(file, 'r') as f:
            s1, s2, mismatches = f.readlines()
        r = fun(s1.strip(),s2.strip(), int(mismatches))
        result.append( str(r) )
    # Testing equality.
    unittest.main()
    
#==============================================================================