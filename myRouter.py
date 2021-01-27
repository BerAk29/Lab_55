
class Router:
    """ Router Class """
    def __init__(self, model, sw_version, ip_add):
        """ initializing value"""
        self.model = model
        self.sw_version = sw_version
        self.ip_add = ip_add
    
    def getdesc(self):
        """ return a description from information """
        desc = {'Router Model': self.model, 
                'Software version': self.sw_version, 
                'Management IP': self.ip_add}
        return desc

rtr1 = Router('ASR1001-X', '16.12.4', '10.10.1.1')
rtr2 = Router('ASR9901', '6.6.3', '10.10.2.2')
rtr3 = Router('ISR4451', '16.6.5', '10.10.3.3')

desc1 = rtr1.getdesc()
desc2 = rtr2.getdesc()
print('\n')
for key, value in desc1.items():
    print(key, ':', value)
print('\n')
for key, value in desc2.items():
    print(key, ':', value)

#for item in desc1.items():
 #   print(item)

import calendar as cal
print('\n', cal.month(2021, 1, 2, 1))