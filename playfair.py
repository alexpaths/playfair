# Playfair Cipher Matrix Generator
#
# See README.md for details
# 

## Imports
from datetime import date
import string
import random

## Global Variables
today = date.today()
choices = string.ascii_uppercase + string.digits

## Prepare Cipher Matrix
grid = []
gridsize = 6

for j in range(0, gridsize + 1):
    gridrow = []
    if j == 1:
	for i in range(0, gridsize):
            gridrow.append('---')
    else:
        for i in range(0, gridsize):
            choice = random.choice(choices)
            while (any(choice in s for s in grid) or any(choice in s for s in gridrow)):
                choice = random.choice(choices)
            gridrow.append(choice)
    grid.append(gridrow)

## Modify to Markdown

PFmatrix = ''
for j in grid:
    rowstring = '| '
    for i in j:
        rowstring += i + ' | '
    rowstring += ' \n'
    PFmatrix += rowstring

## Output to file

matrixCopies = 2

fID = ''
for i in grid[0]:
    fID += i

fname = 'output/' + today.strftime("%Y%m%d") + '_' + fID + '.md'
f = open(fname, 'w')

for x in range(0, matrixCopies):
    f.write('# ' + today.strftime("%Y%m%d") + '\n')
    f.write('\n')
    f.write(PFmatrix)
    f.write('\n<br>\n')

f.write('For Academic Purposes Only - GPL-3.0-only  \n')
f.write('[Source Code](https://github.com/alexpaths/playfair)\n')
f.close()

## EOF
