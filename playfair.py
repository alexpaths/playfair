#!/usr/bin/env python3

'''Playfair Cipher Matrix Generator

This script runs in Python3

See README.md for details'''

## Imports
from datetime import date
import string
import random

## Global Variables
CHOICES = ''.join([string.ascii_uppercase,string.digits]) # Must be of a length such that GRIDSIZE is an integer

## Prepare Cipher Matrix
grid = []
matrix_md = ''
GRIDSIZE = 6 # GRIDSIZE left as a variable to leave room for more CHOICES
MATRIXCOPIES = 2

for j in range(0, GRIDSIZE + 1):
    gridrow = []
    if j == 1:
        for i in range(0, GRIDSIZE): # Looping so GRIDSIZE is variable for additional CHOICES
            gridrow.append(':---:')
    else:
        for i in range(0, GRIDSIZE):
            choice = random.choice(CHOICES)
            while (any(choice in s for s in grid) or any(choice in s for s in gridrow)):
                choice = random.choice(CHOICES)
            gridrow.append(choice)
    grid.append(gridrow)

## Modify to Markdown

for row in grid:
    matrix_md += ''.join(['| ',' | '.join(row),' |\n'])

## Output to file

FNAME = ''.join(['output/',date.today().strftime("%Y%m%d"),'_',''.join(grid[0]),'.md'])
with open(FNAME, mode='w', encoding='utf-8') as f:
    for x in range(0, MATRIXCOPIES):
        f.write(''.join(['# ', date.today().strftime("%Y%m%d"),'\n\n']))
        f.write(matrix_md)
        f.write('\n---\n')

    f.write('For Academic Purposes Only - GPL-3.0-only  \n\n')
    f.write('[Source Code](https://github.com/alexpaths/playfair)\n')

## EOF
