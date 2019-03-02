#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:09:35 2019

@author: jugal
"""

'''Hello Everyone, here are some more details for Machine learning Problem Statement.

Input: research paper pdf
Output: extracted segments of research work in JSON format

Necessary tasks: extract title, authors, abstract

Would be great if done tasks: extract problem statement, approach, related work, citations

Let me know if you need more clarification.
import re
import os, os.path'''

from PyPDF2 import PdfFileReader


def text_extractor(path):
   with open(path, 'rb') as f:
       pdf = PdfFileReader(f)

       # get the first page
       page = pdf.getPage(1)
       print(page)
       print('Page type: {}'.format(str(type(page))))

       text = page.extractText()
       print(text)


if __name__ == '__main__':
   path = 'Deep Residual Learning for Image Recognition.pdf'
   text_extractor(path)


import PyPDF2

pdfFileObj = open('Deep Residual Learning for Image Recognition.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

pdfFileObj.close()



'''
print("HERE IT STARTS")

import os
import re
path = '/Users/rushirajparmar/Downloads/ML_Hackathon/AU/Automatic Extraction of Main Thesis Documents Fields Using Decision Trees.pdf'
for i in os.listdir(path):
   with open(path+i) as f:
       content = f.read()
       pattern = re.compile('CONCLUSION:\s*([\s\w.]*)\n[A-Z\s]*:')
       print(pattern.findall(content)[0])
'''



import re
import os, os.path

PATH = '/home/jugal/Data_poltergeist'
conclusions = []
for file in os.listdir(PATH):
    with open(os.path.join(PATH, file)) as f:
        data = f.read()

'''fd = os.open("Topic_Extraction.txt", os.O_RDWR|os.O_CREAT )
data = fd.read()'''

f = open("Topic_Extraction.txt", "r")
print(f.read())

conclusion = re.search('Abstract: (.*?)([A-Z]{2,})', f).group(1)
conclusions.append(conclusion)