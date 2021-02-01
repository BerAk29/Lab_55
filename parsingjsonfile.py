'''JavaScript Object Annotation'''
import json
from pprint import pprint


# First method
with open('interfaces.json') as f:
    json_data = json.load(f)

#pprint(json_data)
#print(type(json_data))  # is a dict
#print(type(json_data['ietf-interfaces:interfaces'])) # is dict

int_dict = dict()
for items in json_data['ietf-interfaces:interfaces']['interface']:
    name = items['name']
    ip_add = items['ietf-ip:ipv4']['address'][0]['ip']
    netmask_add = items['ietf-ip:ipv4']['address'][0]['netmask']
    print(name, ip_add, netmask_add)
    
    #for x2 in x1:
        #print(x2['name'], x2['type'], x2['ietf-ip:ipv4'])
        #print(x2['name'], x2['type'], x2['ietf-ip:ipv4']['address'][0])
        #print(x2['name'], x2['type'], x2['ietf-ip:ipv4']['address'][0])

#pprint(json_data)
 


"""
# Second method

with open('interfaces.json') as f:
    json_string = f.read()
    


# Display the type and contents of the json_text variable
print("json_text is a", type(json_string))
print(json_string)

# Use the json module to parse the JSON string into native Python data
json_data = json.loads(json_string)

# Display the type and contents of the json_data variable
print("json_data is a", type(json_data))
pprint(json_data)
"""

