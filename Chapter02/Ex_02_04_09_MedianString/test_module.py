# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:23:31 2022

@author: dejong71
"""

#==============================================================================

import os
import Utility.file_reader as fr
import unittest

from Chapter02.Ex_02_04_09_MedianString.median_string \
    import median_string as fun

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
    # result, control = fr.read_and_solve_all(fun, path)
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
            lines = f.readlines()
            length = lines[0].strip()
            strings = lines[1].strip().split()
        r = fun(int(length), strings)
        if isinstance(r, str) or isinstance(r, int) or isinstance(r, float):
            result.append([str(r)])
        elif isinstance(r, list) and len(r) > 0:
            result.append( sorted(r) )
        else:
            result.append(['nan'])
    # Testing equality.
    unittest.main()
    
#===============================================================================