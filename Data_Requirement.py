'''
Created on Jun 10, 2015

@author: le_minh_thu
'''
import types
import datetime

class Requirement(object):
    '''
    class Data_Requirement contains the components to be produced, time period and quantity required
    '''

    def __init__(self):
        self.time = datetime.date.today()
        self.code = ""
        self.qty = 0
    
    def set_code(self, code):
        #assert type(code) is types.StringType, "code is not a string: %r" % code
        
        self.code = code
        
    def set_time(self, time):
        assert type(time) is datetime.date, "time is not in the correct datetime datatype: %r" % time
        
        self.time = time
    
    def set_qty(self, qty):
        assert type(qty) is types.FloatType, "qty is not float: %r" % qty
        assert qty>=0, "quantity to be produced is negative"
        
        self.qty = qty
    
    def requirement_detail(self):
        return  self.code + " " + str(self.time) + " " + str(self.qty) + "\n"