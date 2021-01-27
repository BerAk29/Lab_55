
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

class Switch(Router):

    def getdesc(self):
        """ return a description from information """
        desc = {'Switch Model': self.model, 
                'Software version': self.sw_version, 
                 'Management IP': self.ip_add}
        return desc

rtr1 = Router('ASR1001-X', '16.12.4', '10.10.1.1')
rtr2 = Router('ASR9901', '6.6.3', '10.10.2.2')
rtr3 = Router('ISR4451', '16.6.5', '10.10.3.3')
sw1 = Switch('Cat9500', '16.12.4', '10.10.10.10')


desc1 = rtr1.getdesc()
desc2 = rtr2.getdesc()
desc4 = sw1.getdesc()

# Method 1 to redirect to a File
with open('out.txt', 'w') as f:
    print(end='\n', file=f)
    for key, value in desc1.items():
        print(key, ':', value, file=f)

    print(end='\n', file=f)
    for key, value in desc2.items():
        print(key, ':', value, file=f)

    print(end='\n', file=f)
    for key, value in desc4.items():
        print(key, ':', value, file=f)


# Method 2 to redirect to a File
from contextlib import redirect_stdout

with open('out2.txt', 'w') as f:
    with redirect_stdout(f):
        print(end='\n')
        for key, value in desc1.items():
            print(key, ':', value)

        print(end='\n')
        for key, value in desc2.items():
            print(key, ':', value)

        print(end='\n')
        for key, value in desc4.items():
            print(key, ':', value)


"""
# Method 3 : Redirecting externally from the shell itself is another option, and often preferable:
./script.py > out3.txt
"""

"""
#for item in desc1.items():
 #   print(item)

import calendar as cal
print('\n', cal.month(2021, 1, 2, 1))
"""

