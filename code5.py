#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:24:43 2019

@author: jugal
"""

from pdf2image import convert_from_path
pages = convert_from_path('Application of Image Processing and Convolution.pdf', 500)

for idx, page in enumerate(pages):
    if idx == 0: 
        page.save('frontpage.jpg', 'JPEG')
        break


from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/home/jugal/.virtualenvs/fe/lib/python3.6/site-packages/pytesseract/'
TESSDATA_PREFIX = '/home/jugal/.virtualenvs/fe/lib/python3.6/site-packages/pytesseract'
output = pytesseract.image_to_string(PIL.Image.open('frontpage.jpg').convert("RGB"), lang='eng')
print(output)