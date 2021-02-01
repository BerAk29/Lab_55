'''JavaScript Object Annotation'''
import json

people_string = '''
{
    "people": [
        {"name": "John Smith",
        "phone": "445-333-222",
        "emails": ["jsmith@gmail.com", "john.smith@abc.com"],
        "has_license": false
        },
        {"name": "Jane Doe",
        "phone": "111-444-555",
        "emails": null,
        "has_license": true
        }
    ]
}'''

# Step 1 : Convert JSON string into python dict using loads
data = json.loads(people_string)

print(data)  # will the dictionary with appropriate value
print(type(data))  # data is a dictionary
print(type(data['people']))  # data['key'] is a list

for person in data['people']:
    print(person)
    print(person['name'])
    print(person['emails'])
    if person['name'] == 'John Smith':
        del person['phone']  #del phone number for this one
    

# Step 2 : Convert Python Data/dict into JSON string using dumps
new_people_string = json.dumps(data, indent=2, sort_keys=False)  # new_people_string is json string, and data is python dict
# new_people_string = json.dumps(data, indent=2, sort_keys=True)  to structure output, sort_keys in apha;

print(new_people_string)  # John Smith is now without phone number



