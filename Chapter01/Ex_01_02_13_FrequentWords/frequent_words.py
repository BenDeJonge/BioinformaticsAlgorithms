# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:05:05 2022

@author: dejong71
"""

#==============================================================================

def get_frequency_table(text : str, k : int) -> dict:
    '''
    Given a text (string) and a size k (int), return the a frequency table of
    occurences of text fragment of length k in the text.
    
    Parameters
    ----------
    text : str
        The text to look for patterns.
    k : int
        The length of the pattern to look for.

    Returns
    -------
    dict
        A frequency table of occurences of fragments of length k inside text.
    '''
    # Construct frequency table.
    frequent_words = {}
    for i in range(len(text) - k + 1):
        fragment = text[ i : i + k ]
        try:
            frequent_words[fragment] += 1
        except KeyError:
            frequent_words[fragment] = 1
    return frequent_words

#==============================================================================

def frequent_words(text : str, k : int) -> list:
    '''
    Given a text (string) and a size k (int), return the text fragment of 
    length k that occurs most in the text.
    
    E.g. 'ACG TCG CGC GAC GTA', 2 -> ['CG']
         'ATA ATA CGC CGC'    , 3 -> ['ATA', 'CGC']
    
    Parameters
    ----------
    text : str
        The text to look for patterns.
    k : int
        The length of the pattern to look for.

    Returns
    -------
    list
        The fragment of length k with the most occurences.
    '''
    fw = get_frequency_table(text, k)
    # Find max frequency and get all values with that frequency.
    max_count = max(fw.values())
    frequent_list = [ fragment for fragment, count in fw.items() 
                      if count == max_count ]   
    return sorted(frequent_list)

#==============================================================================