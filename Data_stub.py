'''
Created on Jun 19, 2015

@author: le_minh_thu
'''

CONST_MPS_MASTERLIST = "mps masterlist"
CONST_MRP_MASTERLIST = "mrp masterlist"
CONST_PLANNED_ORDER_RELEASE_MASTERLIST = "planned order release masterlist"
CONST_COMPONENT_MASTERLIST = "component masterlist"
CONST_FINISHED_GOODS_MASTERLIST = "finished goods masterlist"

from Data_Component.Component import Component
from Data_Requirement.MPS_masterlist_test import MPSMasterList
from Data_Requirement.MRPMasterList import MRPMasterList
from Data_Component.ComponentMasterList import ComponentMasterList

class Data_stub(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        self.mps_master_list = MPSMasterList()
        self.mrp_masterlist = MRPMasterList()
        self.component_master_list = ComponentMasterList()
    #incorporated from shevlia's data class     
    
    def isPresentinList(self, obj):
        if isinstance(obj, Component):
            code = obj.code
            return self.component_master_list.isPresent(code)
        #elif isinstance(obj, Account):
        #   return False
       
    def add_to_masterlist(self, list_name, data):
        if list_name == CONST_COMPONENT_MASTERLIST:
            self.component_master_list.add_to_masterlist(data)
            
        elif list_name == CONST_MPS_MASTERLIST:
            self.mps_master_list.add_to_masterlist(data)
        
        elif list_name == CONST_MRP_MASTERLIST:
            self.mrp_masterlist.add_to_mrp_masterlist(data)
        
        elif list_name == CONST_PLANNED_ORDER_RELEASE_MASTERLIST:
            self.mrp_masterlist.add_to_por_masterlist(data)
    
    def retrieve_data(self, list_name, data):
        if list_name == CONST_COMPONENT_MASTERLIST:
            assert (data in self.component_master_list.master_list.keys()), "code not found: %r" % data
            return self.component_master_list.master_list.get(data)

    def retrieve_list(self,list_name):
        if list_name == CONST_COMPONENT_MASTERLIST:
            return self.component_master_list.get_master_list()
        
        elif list_name == CONST_FINISHED_GOODS_MASTERLIST:
            return self.component_master_list.get_finished_goods_list()
        
        elif list_name == CONST_MPS_MASTERLIST:
            return self.mps_master_list.retrieve_data()
        
        elif list_name == CONST_MRP_MASTERLIST:
            return self.mrp_masterlist.retrieve_mrp_masterlist()
        
        elif list_name == CONST_PLANNED_ORDER_RELEASE_MASTERLIST:
            return self.mrp_masterlist.retrieve_por_masterlist()
        
    def data_detail(self, list_name):
        if list_name == CONST_COMPONENT_MASTERLIST:
            return self.component_master_list.CML_detail()
        
        elif list_name == CONST_FINISHED_GOODS_MASTERLIST:
            return self.component_master_list.finished_goods_detail()
        
        elif list_name == CONST_MRP_MASTERLIST:
            return self.mrp_masterlist.data_detail_mrp()
        
        elif list_name == CONST_PLANNED_ORDER_RELEASE_MASTERLIST:
            return self.mrp_masterlist.data_detail_por()
        
        elif list_name == CONST_MPS_MASTERLIST:
            return self.mps_master_list.data_detail()
