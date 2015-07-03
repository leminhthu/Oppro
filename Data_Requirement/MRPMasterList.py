'''
Created on Jun 19, 2015

@author: le_minh_thu
'''

class MRPMasterList(object):
    '''
    This class keeps track of exploded material requirements
    '''
    def __init__(self):
        self.mrp_masterlist = {}
        self.level = 0
        #por is planned order release
        self.por_masterlist = {}
    
    def add_to_mrp_masterlist(self, requirement_list):
        self.mrp_masterlist[self.level] = requirement_list
        self.level += 1
        
    def add_to_por_masterlist(self, por_masterlist):
        self.por_masterlist = por_masterlist
                
    def find_index(self, code, requirement_list):
        for requirement in requirement_list:
            if code == requirement.code:
                return requirement_list.index(requirement)
        return -1
           
    def retrieve_mrp_masterlist(self):
        return self.mrp_masterlist
    
    def retrieve_por_masterlist(self):
        return self.por_masterlist
    
    def data_detail_mrp(self):
        detail = ""
        for level in self.mrp_masterlist.keys():
            detail = detail + str(level) + "\n"
            value = self.mrp_masterlist[level]
            for time in value.keys():
                detail = detail + str(time) + "\n"
                requirement_list = value[time]
                for requirement in requirement_list:
                    detail = detail + requirement.requirement_detail()
        return detail
    
    def data_detail_por(self):
        detail = ""
        time_list = self.por_masterlist.keys()
        time_list = sorted(time_list)
        
        for time in time_list:
            detail = detail + str(time) + "\n"
            requirement_list = self.por_masterlist[time]
            for requirement in requirement_list:
                detail = detail + requirement.requirement_detail()
                
        return detail