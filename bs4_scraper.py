# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:22:41 2024

author/answered by: cosinepenguin
url: https://stackoverflow.com/questions/45070818/python-web-scraper-crawler-html-tables-to-excel-spreadsheet
"""

import pandas as pd
import requests
import bs4

rowdf= []


def collecting_results(year):
    #website data from year 2009 - 2020
    for i in range(2009, 2021):
        url = 'https://www.pinoyswertres.com/pcso-swertres-result-history-{}/'.format(i)
        response = requests.get(url)
        html = response.content
        soup = bs4.BeautifulSoup(html, "lxml")
        tables = soup.findAll("table")
        
        for table in tables:
            #Here you can do whatever you want with the data! You can findAll table row headers, etc...
            list_of_rows = []
            for row in table.findAll('tr')[1:]:
                list_of_cells = []
                
                for cell in row.findAll('td'):
                    text = cell.text.replace('&nbsp;', '')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)
            rowdf.extend(list_of_rows)
            
    #to load year 2021 up      
    for i in range(2021, (year+1)):
        url = 'https://www.pinoyswertres.com/swertres-result-history-{}//'.format(i)
        response = requests.get(url)
        html = response.content
        soup = bs4.BeautifulSoup(html, "lxml")
        tables = soup.findAll("table")
        
        for table in tables:
            list_of_rows = []
            for row in table.findAll('tr')[1:]:
                list_of_cells = []
                
                for cell in row.findAll('td'):
                    text = cell.text.replace('&nbsp;', '')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)
            rowdf.extend(list_of_rows)
    
    #making the list into a DataFrame and saves it as csv 
    return pd.DataFrame(list(rowdf))
    

