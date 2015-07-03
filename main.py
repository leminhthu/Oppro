'''
Created on Jun 10, 2015

@author: shelvia_dwi_hotama
'''

from Parser import Parser
from Data_stub import Data_stub, CONST_PLANNED_ORDER_RELEASE_MASTERLIST,\
    CONST_MPS_MASTERLIST, CONST_MRP_MASTERLIST, CONST_FINISHED_GOODS_MASTERLIST
from MRP import MRP
from Data_Component.ComponentMasterList import CONST_COMPONENT_MASTERLIST

temp = Data_stub()
excel_parser = Parser("C:\Users\le_minh_thu\Desktop\BOM1.xlsx", temp, "BOM")

excel_parser.readDatafromExcel()

mps_parser = Parser("C:\Users\le_minh_thu\Desktop\MPS.xlsx", temp, "MPS")
mps_parser.readMPS()



print temp.data_detail(CONST_COMPONENT_MASTERLIST)

print temp.data_detail(CONST_FINISHED_GOODS_MASTERLIST)

print temp.data_detail(CONST_MPS_MASTERLIST)



material_requirement_plan= MRP(temp)
material_requirement_plan.process_requirement()

print temp.data_detail(CONST_MRP_MASTERLIST)
output =  temp.data_detail(CONST_PLANNED_ORDER_RELEASE_MASTERLIST)
print output