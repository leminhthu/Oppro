'''
Created on Jun 9, 2015

@author: le_minh_thu
'''

CONST_COMPONENT_MASTERLIST = "component masterlist"

class ComponentMasterList(object):
    '''
   class ComponentMasterList maintains the master list for all components ranging from level 0 to level4
    '''
    
    def __init__(self):
        self.master_list = {}
        self.finished_goods_list = {}
    
    def add_to_masterlist(self, component):
        new_key = component.code
        self.master_list[new_key] = component
        if component.status:
            self.finished_goods_list[new_key] = component
    
    def get_finished_goods_list(self):
        return self.finished_goods_list
    
    def get_master_list(self):
        return self.master_list
                      
    def isPresent(self, code):
    #check if a component is already declared previously
    
        if code in self.master_list.keys():
            return True
        else:
            return False

    def retrieve_level_zero_list (self):
        return self.finished_goods_list
    
    def CML_detail (self):
        component_details = ""
        for code in self.master_list.keys():
            component = self.master_list[code]
            component_details = component_details + component.component_details() + component.sub_component_details()
        return component_details
    
    def finished_goods_detail(self):
        finished_goods_details = ""
        for code in self.finished_goods_list.keys():
            finished_goods = self.finished_goods_list[code]
            finished_goods_details = finished_goods_details + finished_goods.component_details() + "\n"
        return finished_goods_details