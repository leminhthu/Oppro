'''
Created on Jun 17, 2015

@author: le_minh_thu
'''

class MPSMasterList(object):
    '''
    This class keeps track of all level 0 component requirements
    '''
    #requirement masterlist is a dictionary keeping track of all component requirements (requirement objects) 
    #with the time required being the dictionary keys
    #Each key has a list of requirement objects sharing the same time required
    
    def __init__(self):
        self.mps_masterlist = {}

    def add_to_masterlist(self, requirement):
        key = requirement.time
        if key not in self.mps_masterlist.keys():
            self.mps_masterlist[key] = [requirement]          
        else:
            code = requirement.code
            requirement_list = self.mps_masterlist[key]
            index = self.find_index(code, requirement_list)
            if  index == -1:
                #code not found in the requirement list
                requirement_list.append(requirement)
            else:
                requirement_list[index] = requirement
            
    def find_index(self, code, requirement_list):
        for requirement in requirement_list:
            if code == requirement.code:
                return requirement_list.index(requirement)
        return -1
    
    def retrieve_data(self):
        """
        if time in self.mps_masterlist.keys():
            return self.mps_masterlist[time]
        else:
            return None
        """
        return self.mps_masterlist
    
    def data_detail(self):
        masterlist_detail = ""
        for time in self.mps_masterlist:
            for requirement in self.mps_masterlist[time]:
                masterlist_detail = masterlist_detail + requirement.requirement_detail()
        return masterlist_detail