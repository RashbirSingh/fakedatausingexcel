#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:03:13 2019

@author: ubuntu
"""

import time
from fakedatafromexcel import fakedata
start_time = time.time()
fd = fakedata()
fd.fakedatagenarator(in_path='Related.XLSX')
end_time = time.time()
print(start_time-end_time)
