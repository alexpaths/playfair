#!/usr/bin/env python3

'''Playfair Cipher Matrix Generator

This script runs in Python3

See README.md for details'''

## Imports
from datetime import date
import string
import random
from icecream import ic

class PlayfairMatrix():
    def __init__(self):
        self.choices = ''.join([string.ascii_uppercase,string.digits])
        self.indexes = [*range(0,len(self.choices),1)]
        self.CreateNewMatrix()
    
    def CreateNewMatrix(self):
        random.shuffle(self.indexes)
        self.output = [self.choices[i] for i in self.indexes]

    def ConvertMarkdown(self):
        self.markdown = [
            ''.join(['|','|'.join(self.output[0:6]),'|\n']),
            '|:---:|:---:|:---:|:---:|:---:|:---:|\n',
            ''.join(['|','|'.join(self.output[6:12]),'|\n']),
            ''.join(['|','|'.join(self.output[12:18]),'|\n']),
            ''.join(['|','|'.join(self.output[18:24]),'|\n']),
            ''.join(['|','|'.join(self.output[24:30]),'|\n']),
            ''.join(['|','|'.join(self.output[30:37]),'|\n'])]

    # TODO Fix this
    # def addMarkdownFooter():
        # \n---\n',
        # 'For Academic Purposes Only - GPL-3.0-only  \n\n',
        # '[Source Code](https://github.com/alexpaths/playfair)\n']

    def ExportMarkdown(self):
        self.ConvertMarkdown()
        FNAME = ''.join(['output/',date.today().strftime("%Y-%m-%d"),'_',''.join(self.output[0:6]),'.md'])
        with open(FNAME, mode='w', encoding='utf-8') as f:
            f.write(''.join(['## ', date.today().strftime("%Y-%m-%d"),'\n\n']))
            for line in self.markdown:
                f.write(line)

    def ExportMarkdownSheet(self,num):
        FNAME = ''.join(['output/',date.today().strftime("%Y-%m-%d"),'_SHEET.md'])
        with open(FNAME, mode='w', encoding='utf-8') as f:
            f.write(''.join(['## ', date.today().strftime("%Y-%m-%d"),'\n\n']))
            for click in range(num):
                self.CreateNewMatrix()
                self.ConvertMarkdown()

                f.write(''.join(['# Code ', str(click), '\n']))
                
                for line in self.markdown:
                    f.write(line)
                
                f.write('---\n')


if __name__ == "__main__":
    data = PlayfairMatrix()
    data.ExportMarkdownSheet(5)

# ## EOF
