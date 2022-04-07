# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 15:41:11 2022

@author: dejong71
"""

#==============================================================================

import os
import file_reader as fr
import unittest

path = os.path.dirname(__file__)
os.chdir(path)
from reverse_complement import reverse_complement as fun

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
            strand = f.read()
            result.append(fun(strand))
    # Testing equality.
    unittest.main()
    
#==============================================================================