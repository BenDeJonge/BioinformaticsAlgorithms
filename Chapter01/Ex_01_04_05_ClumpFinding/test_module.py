# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 23:50:03 2022

@author: dejong71
"""

#==============================================================================

import os
import file_reader as fr
import unittest

from Chapter01.Ex_01_04_05_ClumpFinding.clump_finding import clump_finding as fun

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
            genome, numbers = f.read().splitlines()
            length, window, counts = [ int(i) for i in numbers.split() ]
            result.append(fun(genome, length, window, counts))
    # result = ' '.join([ str(i) for i in result ])
    # Testing equality.
    unittest.main()
    
#==============================================================================