# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 23:19:18 2022

@author: dejong71
"""

import os
import glob

def read_folder(path, ext='txt'): 
    files = glob.glob(os.path.join(os.path.abspath(path), 
                                   f'*.{ext}'))
    return files