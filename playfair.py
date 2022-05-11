#!/usr/bin/env python3

'''Playfair Cipher Matrix Generator

This script runs in Python3

See README.md for details'''

## Imports
from datetime import date
import string
import random

## Global Variables
CHOICES = ''.join([string.ascii_uppercase,string.digits])
output = [*range(0,len(CHOICES),1)]

## Prepare Cipher Matrix
random.shuffle(output)

i = 0
for num in output:
    output[i] = CHOICES[num]
    i = i + 1

# print (str(''.join(output)))

## Output to file
FNAME = ''.join(['output/',date.today().strftime("%Y-%m-%d"),'_',''.join(output[0:6]),'.md'])
with open(FNAME, mode='w', encoding='utf-8') as f:
    f.write(''.join(['# ', date.today().strftime("%Y-%m-%d"),'\n\n']))
    f.write(''.join(['|','|'.join(output[0:6]),'|\n']))
    f.write('|:---:|:---:|:---:|:---:|:---:|:---:|\n')
    f.write(''.join(['|','|'.join(output[6:12]),'|\n']))
    f.write(''.join(['|','|'.join(output[12:18]),'|\n']))
    f.write(''.join(['|','|'.join(output[18:24]),'|\n']))
    f.write(''.join(['|','|'.join(output[24:30]),'|\n']))
    f.write(''.join(['|','|'.join(output[30:37]),'|\n']))
    f.write('\n---\n')
    f.write('For Academic Purposes Only - GPL-3.0-only  \n\n')
    f.write('[Source Code](https://github.com/alexpaths/playfair)\n')

## EOF
