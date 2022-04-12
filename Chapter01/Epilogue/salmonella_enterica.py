# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 00:25:04 2022

@author: dejong71
"""

#==============================================================================

import os
import matplotlib.pyplot as plt
import numpy as np

from Chapter01.Ex_01_07_08_SkewDiagram.skew_diagram import skew_diagram
from Chapter01.Ex_01_08_10_FrequentWordsMismatchesReverseComplements.frequent_words_mismatches_reverse_complements \
    import frequent_words_mismatches_reverse_complements

#==============================================================================

class FastaReader:
    '''
    Basic class to read a FASTA file and return a description and genome.

    Parameters
    ----------
    path : str
        The filepath to the FASTA file, containing a single genome.
    name : str
        The genus of the genome organism.

    Returns
    -------
    None.
    '''
    def __init__(self, path : str, name : str):
        self.name = name
        self.abbrev = f'{name.split()[0][0]}. {name.split()[1]}'
        self.path = path
        self._text = self.reader()
        self.description, self.genome = self.parse_text()
        
    def reader(self) -> list[str]:
        '''Read a file and return the text as a list of lines.'''
        with open(self.path, 'r') as f:
            text = f.readlines()
        return text
            
    def parse_text(self) -> tuple[str]:
        '''Split the _text attribute in a description and a joined genome.'''
        description = 'N/A'
        text = self._text
        if self._text[0].startswith('>'):
            description = self._text[0][1:]
            text = self._text[1:]
        genome = ''.join( line.strip() for line in text )
        return description, genome

#==============================================================================

# Settings.
PLOTTING = True
# Grabbing data.
path = os.path.join(os.path.dirname(__file__),
                    'salmonella_enterica.txt')
salmonella = FastaReader(path, 'Salmonella enterica')
# Calculating and plotting GC-skew.
skew = skew_diagram(salmonella.genome)
i_min_skew = skew.index(min(skew))

#------------------------------------------------------------------------------

if PLOTTING:
    # Plotting.
    fig_skew, ax_skew = plt.subplots()
    ax_skew.plot(skew)
    # Formatting labels.
    ax_skew.set_title(f'GC-skew diagram of $\it{f"{salmonella.abbrev}"}$')
    ax_skew.set_xlabel('Position [bases]')
    ax_skew.set_ylabel('Skew [#G-#C]')
    ax_skew.vlines(i_min_skew, min(skew), (max(skew)+min(skew))/2, color=(1,0,0))
    ax_skew.text(i_min_skew, (max(skew)+min(skew))/2, 
                 f'{min(skew)}\n@{i_min_skew:,}\n', 
                 ha='center', va='bottom')
    # Saving.
    fig_skew.savefig(os.path.join(os.path.dirname(__file__), 'gc_skew.png'),
                     dpi=300, transparent=True, bbox_inches='tight')
    
#------------------------------------------------------------------------------

# Determining ori window and search settings.
width = 1000
before = width // 2
window = salmonella.genome[i_min_skew - before : i_min_skew + (width - before)]
length = 9
mismatches = 1
# Finding DnaA boxes.
potential_dnaa = frequent_words_mismatches_reverse_complements(window, length, mismatches)
dnaa = [ dnaa for dnaa in potential_dnaa if dnaa in window ]

#------------------------------------------------------------------------------

# Plotting DnaA boxes in window.
if PLOTTING:
    # Reshaping data to array.
    data = [0] * len(window)
    for d in dnaa:
        i = window.index(d)
        data[i:i+length] = [1] * length
    xdim = 50
    ydim = width // xdim
    data = np.reshape(data, (ydim, xdim))
    # Plotting.
    fig_dnaa, ax_dnaa = plt.subplots()
    ax_dnaa.imshow(data, interpolation='none', aspect='equal', cmap='cividis')
    # Formatting ticks.
    ax_dnaa.set_xticks(np.arange(-0.5, xdim+0.5, 5))
    ax_dnaa.set_xticklabels(range(0, xdim + 1, 5))
    ax_dnaa.set_yticks(np.arange(-0.5, ydim+0.5, 5))
    ax_dnaa.set_yticklabels(range(0,ydim+1, 5))
    # Formatting grid.
    ax_dnaa.set_xticks(np.arange(-0.5, xdim+0.5, 1), minor=True)
    ax_dnaa.set_yticks(np.arange(-0.5, ydim+0.5, 1), minor=True)
    ax_dnaa.grid(which='both', color='w', linestyle='-', linewidth=0.1)
    # Formatting labels.
    ax_dnaa.set_title(f'Potential ORI location in $\it{f"{salmonella.abbrev}"}$ window [{width} b]')
    ax_dnaa.set_xlabel('Column')
    ax_dnaa.set_ylabel('Row')
    # Saving.
    fig_dnaa.savefig(os.path.join(os.path.dirname(__file__), 'dnaa_loc.png'),
                     dpi=300, transparent=True, bbox_inches='tight')
    
#==============================================================================