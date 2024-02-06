# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:24:36 2024

@author: Virfrance
"""

import bs4_scraper
import pandas as pd

#collecting the data until 2024 and saves as csv
df = bs4_scraper.collecting_results(2024)
df.to_csv('raw_swertres_results.csv')
