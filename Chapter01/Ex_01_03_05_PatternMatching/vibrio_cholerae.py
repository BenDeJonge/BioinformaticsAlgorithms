# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:11:41 2022

@author: dejong71
"""

#==============================================================================

import os
from Chapter01.Ex_01_03_05_PatternMatching.pattern_matching import pattern_matching

#==============================================================================

path = os.path.dirname(__file__)
with open(os.path.join(path, 'Vibrio_cholerae.txt'), 'r') as f:
    genome = f.read().strip()
pattern = 'CTTGATCAT'
starts = pattern_matching(pattern, genome)

#==============================================================================