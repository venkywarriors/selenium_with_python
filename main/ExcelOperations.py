'''
Created on 01-Jul-2020

@author: venkateshwara D
'''
import openpyxl 
import os
  
path = os.path.dirname(__file__) +"\\resources\\\\demo.xlsx"
print( path ) 

def readDataCell(row,column):
    wb_obj = openpyxl.load_workbook(path) 
    sheet_obj = wb_obj.active 
    cell_obj = sheet_obj.cell(row, column) 
    return cell_obj.value
