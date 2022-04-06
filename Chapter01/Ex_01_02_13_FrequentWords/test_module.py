# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 00:07:03 2022

@author: dejong71
"""

#==============================================================================

import os
import file_reader as fr
import unittest

path = os.path.dirname(__file__)
os.chdir(path)
from frequent_words import frequent_words as fun

#==============================================================================

class TestEquality(unittest.TestCase):
    '''
    Unittest for equality of counts.
    '''
    def test_counts_outputs(self):
        self.assertEqual(counts, control)

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
            control.append( f.read().split() )
    # Calculating counts.
    counts = []
    for file in inputs:
        with open(file, 'r') as f:
            text, pattern = f.read().splitlines()
            counts.append(fun(text, int(pattern)))
    # Testing equality.
    unittest.main()
    
#==============================================================================