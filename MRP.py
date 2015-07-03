'''
Created on Jun 19, 2015

@author: le_minh_thu
'''
from Data_stub import CONST_MPS_MASTERLIST, CONST_COMPONENT_MASTERLIST,\
    CONST_MRP_MASTERLIST, CONST_PLANNED_ORDER_RELEASE_MASTERLIST
from Data_Requirement.Requirement import Requirement

class MRP(object):
    '''
    This class explodes the material requirements for MPS
    '''

    def __init__(self, all_data):
        self.all_data = all_data
        
        mps_list = self.all_data.retrieve_list(CONST_MPS_MASTERLIST)
        self.requirement_list_by_time = mps_list
        
        self.all_data.add_to_masterlist(CONST_MRP_MASTERLIST, self.requirement_list_by_time)
        
        self.por_masterlist = {}
    
    def process_requirement(self):
        if len(self.requirement_list_by_time) == 0:
            return
        else:
            time_list = self.requirement_list_by_time.keys()
            time_list = sorted(time_list)
            sub_requirement_list = {}
            
            for time in time_list:
                current_requirement_list = self.requirement_list_by_time[time]
                sub_requirement_list_all_parents = self.generate_sub_requirement_list_by_time(current_requirement_list)
                for sub_requirement in sub_requirement_list_all_parents:
                    sub_requirement_list = self.update_requirement_list(sub_requirement, sub_requirement_list)
        
            self.requirement_list_by_time = sub_requirement_list
            
            if len(self.requirement_list_by_time) > 0:
                self.all_data.add_to_masterlist(CONST_MRP_MASTERLIST, self.requirement_list_by_time)
            
            self.process_requirement()
        
    def update_requirement_list(self, requirement, requirement_list):
        #insert requirement into the existing requirement_list dictionary
        #if the key is new, create a new value (list of requirement under the corresponding time)
        #if the key alrd exists, search the list of requirements under the key
        #if the product code alrd exists, add the new requirement to the existing requirement
        #if not, append the new requirement to the back of the list
        
        key = requirement.time
        if key not in requirement_list.keys():
            requirement_list[key] = [requirement]
        else:
            existing_list = requirement_list[key]
            index = 0
            while (index < len(existing_list)) and (existing_list[index].code != requirement.code):
                index += 1
            else:
                if index == len(existing_list):
                    existing_list.append(requirement)
                elif existing_list[index].code == requirement.code:
                    existing_list[index] = self.update_existing_requirement(existing_list[index], requirement)
        return requirement_list
                        
    def update_existing_requirement(self, existing_requirement, new_requirement):
        existing_qty = existing_requirement.qty
        new_qty = new_requirement.qty
        total_qty = existing_qty + new_qty
        new_requirement.set_qty(total_qty)
        
        return new_requirement
           
    def generate_sub_requirement_list_by_time(self, requirement_list):
        sub_requirement_list_all_parents = []
        
        for requirement in requirement_list:
            code = requirement.code
            parent = self.retrieve_component(code)
            sub_requirement_list_per_parent = self.generate_sub_requirement_list_by_parent(parent, requirement)
            sub_requirement_list_all_parents += sub_requirement_list_per_parent
            
        return sub_requirement_list_all_parents
        
    def generate_sub_requirement_list_by_parent(self, parent, requirement):
        sub_component_list = parent.sub_component_and_quantity_list
        required_time_sub_component = requirement.time - parent.lead_time
        
        sub_requirement_list_per_parent = []
        
        if len(sub_component_list) == 0:
            self.release_order(parent, requirement)
            
        else:   
            for code in sub_component_list:
                qty_per_parent = sub_component_list[code]
                required_qty_sub_component = self.calc_sub_requirement_qty(code, qty_per_parent, requirement.qty)
                
                new_requirement = Requirement()
                new_requirement.set_code(code)
                new_requirement.set_time(required_time_sub_component)
                new_requirement.set_qty(required_qty_sub_component)
                sub_requirement_list_per_parent.append(new_requirement)
            
        return sub_requirement_list_per_parent
    
    def release_order(self, component, requirement):
        lead_time = component.lead_time
        release_time = requirement.time - lead_time
        qty = requirement.qty
        code = requirement.code
        
        order_release = Requirement()
        order_release.set_code(code)
        order_release.set_time(release_time)
        order_release.set_qty(qty)
        
        self.por_masterlist = self.update_requirement_list(order_release, self.por_masterlist)   
        self.all_data.add_to_masterlist(CONST_PLANNED_ORDER_RELEASE_MASTERLIST, self.por_masterlist)
        
    def calc_sub_requirement_qty(self,code, qty_per_parent, required_qty_parent):
        sub_component = self.retrieve_component(code)
        
        required_qty_sub_component = qty_per_parent * required_qty_parent
        actual_required_qty_sub_component = self.update_actual_qty(sub_component, required_qty_sub_component)
        
        return actual_required_qty_sub_component
    
    def update_actual_qty(self, component, required_qty):
        actual_required_qty = required_qty - component.stock
        
        if actual_required_qty >= 0:
            component.set_stock(0.0)
        else:
            remaining_stock = (-1) * actual_required_qty
            component.set_stock(remaining_stock)
            actual_required_qty = 0.0
            
        return actual_required_qty
    
    def retrieve_component(self, code):
        return self.all_data.retrieve_data(CONST_COMPONENT_MASTERLIST, code)