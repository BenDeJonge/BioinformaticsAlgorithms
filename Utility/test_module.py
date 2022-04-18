# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:03:54 2022

@author: dejong71
"""

#==============================================================================

import unittest
import file_reader as fr

#==============================================================================



#==============================================================================

def test_module(fun : callable, path : str):
    '''
    Given a path with input and output folders and a callable, execute the 
    callable on the inputs and compare the result with the outputs.

    Parameters
    ----------
    fun : callable
        The function to execute on the input files.
    path : str
        The path containing the input and output files.

    Returns
    -------
    None.
    '''
    control, result = fr.read_and_solve_all(fun, path)
    # Testing equality.    
    class TestResultConrol(unittest.TestCase):
        '''
        Unittest for equality of counts.
        '''
        
        def test_presence(self):
            self.assertTrue(bool(result), 'Check presence of result.')
            self.assertTrue(bool(control), 'Check presence of control.')
        
        def test_counts_outputs(self):
            self.assertEqual(self.result, self.control, 'Check equality of result and control.')
    unittest.main()

#==============================================================================
