'''
Created on Jun 10, 2015

@author: shelvia_dwi_hotama
'''

from Data_Component.Component import Component
from Parser import Parser
from Data_stub import Data_stub, CONST_MRP_MASTERLIST, CONST_PLANNED_ORDER_RELEASE_MASTERLIST, CONST_MPS_MASTERLIST, CONST_COMPONENT_MASTERLIST, CONST_FINISHED_GOODS_MASTERLIST
from MRP import MRP

temp = Data_stub()
excel_parser = Parser("/Users/shelviadwihotama/Documents/workspace/oppro/BOM.xlsx", temp, "BOM")

excel_parser.readDatafromExcel()

mps_parser = Parser("/Users/shelviadwihotama/Documents/workspace/oppro/MPS.xlsx", temp, "MPS")
mps_parser.readMPS()

material_requirement_plan= MRP(temp)
#material_requirement_plan.process_requirement()

#print temp.data_detail(CONST_COMPONENT_MASTERLIST)

FG_dict = temp.retrieve_list(CONST_FINISHED_GOODS_MASTERLIST)

FG_list = FG_dict.keys()

for key in FG_list:
    print key

print temp.data_detail(CONST_FINISHED_GOODS_MASTERLIST)

print temp.data_detail(CONST_MPS_MASTERLIST)

mps_details = temp.data_detail(CONST_MPS_MASTERLIST)
print mps_details

material_requirement_plan= MRP(temp)
material_requirement_plan.process_requirement()

print temp.data_detail(CONST_MRP_MASTERLIST)
output =  temp.data_detail(CONST_PLANNED_ORDER_RELEASE_MASTERLIST)
print output