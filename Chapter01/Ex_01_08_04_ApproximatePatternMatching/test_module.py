# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:07:24 2022

@author: dejong71
"""

#==============================================================================

import os
import file_reader as fr
import unittest

from Chapter01.Ex_01_08_04_ApproximatePatternMatching.approximate_pattern_matching import approximate_pattern_matching as fun

#==============================================================================

class TestEquality(unittest.TestCase):
    '''
    Unittest for equality of counts.
    '''
    def test_counts_outputs(self):
        self.assertEqual(result, control)

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
        res = ' '.join(str(i) for i in r)
        result.append( res )
    # Testing equality.
    unittest.main()
    
#==============================================================================