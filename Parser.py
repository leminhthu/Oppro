'''
Created on Jun 12, 2015

@author: shelvia_dwi_hotama
'''
import xlrd
from Data_Component.Component import Component
from Data_Component.ComponentMasterList import ComponentMasterList
from Data_stub import Data_stub, CONST_MPS_MASTERLIST
from Data_Requirement.Requirement import Requirement
import datetime
from itertools import count

CONST_COMPONENT_MASTERLIST = "component masterlist"

class Parser(object):
    
    #file_address = ""
    #current BOM address: "C:/Users/shelvia_dwi_hotama/workspace/test1/src/BOM.xlsx"
    temp = Data_stub()
    
    def __init__(self, fileloc, data, sheet_type):
        self.data = data
        self.workbook = xlrd.open_workbook(fileloc)
        self.row_header = 7
        self.col_code = 0
        self.col_status= 1
        self.col_name = 2
        self.col_description= 3
        self.col_uom=4
        self.col_leadtime=5
        self.col_time_period=6
        self.col_moq=7
        self.col_supplier=8
        self.col_notes=9
        self.col_sub_component = 10
        self.mps_row_header = 0
        self.mps_col_code= 0
        self.mps_col_time = 1
        self.mps_col_qty = 2
        self.sheet = self.workbook.sheet_by_name(sheet_type)
    
    def get_row_header(self):
        return self.row_header
    def get_col_code(self):
        return self.col_code
    def get_col_bomlevel(self):
        return self.col_bomlevel
    def get_col_name(self):
        return self.col_name
    def get_col_description(self):
        return self.col_description
    def get_col_qty(self):
        return self.col_qty
    def get_col_uom(self):
        return self.col_uom
    def get_col_leadtime(self):
        return self.col_leadtime
    def get_col_moq(self):
        return self.col_moq
    def get_col_stock(self):
        return self.col_stock
    def get_col_supplier(self):
        return self.col_supplier
    def get_col_notes(self):
        return self.col_notes

    def readDatafromExcel(self):
        
        for row in range(self.row_header+1, self.sheet.nrows):
            
            new_component = Component()
            
            new_code = self.sheet.cell_value(row,self.col_code)
            new_component.set_code(new_code)
            
            new_status = self.sheet.cell_value(row, self.col_status)
            new_component.set_status(new_status)
            
            new_name = self.sheet.cell_value(row, self.col_name)
            new_component.set_name(new_name)
            
            new_description = self.sheet.cell_value(row, self.col_description)
            new_component.set_description(new_description)
            
            new_uom = self.sheet.cell_value(row, self.col_uom)
            new_component.set_unit_of_measure(new_uom)
            
            new_time_period = str(self.sheet.cell_value(row, self.col_time_period))
            new_component.set_time_period(new_time_period)
            
            new_leadtime = self.sheet.cell_value(row, self.col_leadtime)
            new_component.set_lead_time(new_leadtime)
            
            new_moq = self.sheet.cell_value(row, self.col_moq)
            new_component.set_moq(new_moq)
            
            new_supplier = self.sheet.cell_value(row, self.col_supplier)
            new_component.set_supplier(new_supplier)
            
            new_notes = self.sheet.cell_value(row, self.col_notes)
            new_component.set_notes(new_notes)

            if not self.data.isPresentinList(new_component):
                col_sub_component = self.col_sub_component
                
                while self.sheet.cell_type(row, col_sub_component) != 0:
                    new_sub_component = self.sheet.cell_value(row, col_sub_component)
                    new_qty = self.sheet.cell_value(row, col_sub_component+1)
                    #need to throw exception
                    
                    new_component.add_sub_component(new_sub_component, new_qty)
                    col_sub_component +=2
                    
                self.data.add_to_masterlist(CONST_COMPONENT_MASTERLIST, new_component)
            else:
                del new_component
                
    def readMPS (self):

        for row in range(self.mps_row_header+1, self.sheet.nrows):

            mps_object = Requirement()
            
            mps_code = self.sheet.cell_value(row, self.mps_col_code)
            mps_object.set_code(mps_code)
            
            mps_time = self.sheet.cell_value(row, self.mps_col_time)
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(mps_time, self.workbook.datemode)
            mps_date = datetime.date(year, month, day)
            mps_object.set_time(mps_date)
            
            mps_qty = self.sheet.cell_value(row, self.mps_col_qty)
            mps_object.set_qty(mps_qty)
            
            self.data.add_to_masterlist(CONST_MPS_MASTERLIST, mps_object)
            
'''
print sheet.cell_value(0,0)
print wkbook.sheets()
print wkbook.sheet_names()

print sheet.nrows
print sheet.ncols

for col in range(sheet.ncols):
    print sheet.cell_value(7, col)
 
for row in range(8, sheet.nrows):
    print sheet.cell_value(row, 0)
'''
