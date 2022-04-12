# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:07:35 2022

@author: dejong71
"""

#==============================================================================

import os
import file_reader as fr
import unittest

from Chapter01.Ex_01_11_04_Neighborhood.neighbors import neighbors as fun

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
            control.append( sorted(f.read().split()) )
    # Calculating counts.
    result = []
    for file in inputs:
        with open(file, 'r') as f:
            pattern, mismatches = f.readlines()
        r = fun(pattern.strip(), int(mismatches))
        result.append( sorted(r) )
    # Testing equality.
    unittest.main()
    
#==============================================================================