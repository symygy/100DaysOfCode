# Turorial: https://www.youtube.com/watch?v=9N6a-VLBa2I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=47


# JavaScript Object Notation
import json

people = '''
{
    "people": [
        {
            "name" : "Michal",
            "phone" : "123 345 456",
            "email" : ["asdasd@wp.pl", "asdasd@wp.pl"],
            "license" : false
        },
        {
            "name" : "MAciek",
            "phone" : "123 345 4234223456",
            "email" : ["aaaaaa@wp.pl", "fffffff@wp.pl"],
            "license" : true
        }
    ]
}
'''

data = json.loads(people)

print(type(data))
print(type(data['people']))
print(data)

for person in data['people']:
    del person['phone']
    print(person['name'])

new_people = json.dumps(data, indent=2, sort_keys=True)



print(type(new_people))

# with open('states.json') as file:
#     data = json.load(file)
#
# for state in data['states']:
#     #print(state['name'], state['abbreviation'])
#     del state['area_codes']
#
# with open('new_states.json', 'w') as file:
#     json.dump(data, file, indent=2)

