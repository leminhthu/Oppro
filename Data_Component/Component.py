'''
Created on Jun 9, 2015

@author: le_minh_thu
'''
from datetime import timedelta

class Component(object):   

    
    def __init__(self):
        self.code = ""
        self.status = False
        self.name = ""
        self.description = ""
        self.lead_time = timedelta(days = 0)
        self.time_period = ""
        self.moq = 0
        self.unit_of_measure =""
        self.supplier =""
        self.notes =""
        self.sub_component_and_quantity_list = {}
        self.stock=0
        self.lot_size = 1
             
    def set_code(self, code):
        self.code = code
        
    def get_code(self):
        return self.code
    
    def set_status(self, status):
        if str(status) == 'Y':
            self.status = True
        elif str(status) == 'N':
            self.status = False
            
    def get_status(self):
        return self.status
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_description(self, description):
        self.description = description
        
    def get_description(self):
        return self.description
    
    def set_lead_time(self, lead_time):
        if self.time_period == "day":
            self.lead_time = timedelta(days = lead_time)
            
        elif self.time_period == "week":
            self.lead_time = timedelta(weeks = lead_time)
            
        elif self.time_period == "month":
            self.lead_time = timedelta(months = lead_time)
            
        elif self.time_period == "year":
            self.lead_time = timedelta(years = lead_time)
    
    def set_time_period(self, time_period):
        self.time_period = time_period
        
    def get_time_period(self):
        return self.time_period
        
    def get_lead_time(self):
        return self.lead_time  
        
    def set_moq(self, moq):
        self.moq = moq
    
    def get_moq(self):
        return self.moq
    
    def set_lot_size(self, lot_size):
        self.lot_size = lot_size
        
    def get_lot_size(self):
        return self.lot_size
       
    def set_unit_of_measure(self, unit_of_measure):
        self.unit_of_measure = unit_of_measure
        
    def get_unit_of_measure(self):
        return self.unit_of_measure
    
    def set_stock(self, stock):
        self.stock = stock
    
    def get_stock(self):
        return self.stock
    
    def set_supplier(self, supplier):
        self.supplier = supplier
        
    def get_supplier(self):
        return self.supplier
    
    def set_notes(self, notes):
        self.notes = notes
        
    def get_notes(self):
        return self.notes
    
    def get_sub_component_and_quantity_list(self):
        return self.sub_component_and_quantity_list.items()
            
    def add_sub_component(self, sub_component, qty):
        if sub_component not in self.sub_component_and_quantity_list.keys():  
        #add a new sub-component if it has not alrd existed
            self.sub_component_and_quantity_list[sub_component] = qty
            return True
        else:
            #if the sub-component to be added alrd exists
            return False

    """ 
    def delete_sub_component(self, sub_component):      
        if sub_component in self.sub_component_and_quantity_list:
            #delete sub-component if it can be found in the list
            self.sub_component_and_quantity_list.remove(sub_component)
            return True
        else:
            #if sub_component to be deleted cannot be found
            return False
    """
    
    def component_details(self):
        list_in_string = self.code + " " + self.name + " " + self.description + " " + self.unit_of_measure + " " + str(self.lead_time) + " " + str(self.time_period) +" " + str(self.moq) + " "  + self.supplier + " " + self.notes + "\n"
        return list_in_string
    
    def sub_component_details(self):
        return str(self.sub_component_and_quantity_list.items()) + "\n"
