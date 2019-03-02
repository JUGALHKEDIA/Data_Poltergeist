#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:31:37 2019

@author: jugal
"""

import pdftables_api
import os

c = pdftables_api.Client('ppovr5eg8563')

file_path = "/home/jugal/Data_poltergeist"

for file in os.listdir(file_path):
    if file.endswith(".pdf"):
        c.html(os.path.join(file_path,file), file+'.html')