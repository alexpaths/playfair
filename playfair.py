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

for j in range(0, gridsize):
    gridrow = []
    for i in range(0, gridsize):
        choice = random.choice(choices)
        while (any(choice in s for s in grid) or any(choice in s for s in gridrow)):
            choice = random.choice(choices)
        gridrow.append(choice)
    grid.append(gridrow)

## Output to file

print(grid)

fname = today.strftime("%Y%m%d") + '.md'
f = open(fname, 'w')

#for x in range(0,2):
#    f.write = '# ' + today.strftime("%Y%m%d") + '  \n'
#    f.write = '<br>'


#Move matrix into md file twice... with date directly above and hr separator 
