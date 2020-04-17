# Tutorial: https://www.youtube.com/watch?v=nghuHvKLhJA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=35

first_name = 'Michal'
last_name = 'Kxxxx'

sentence = f'My name is {first_name.upper()} {last_name.upper()}'

person = {'name' : 'Marcin', 'age' : 29}

sentence2 = 'My name is {} {}'.format(first_name, last_name)
sentence3 = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
sentence4 = f"My name is {person['name']} and I am {person['age']} years old"

calc = f'5 times 10 is equal: {5*10}'
print(calc)

print(sentence)
print(sentence2)
print(sentence3)
print(sentence4)

pi = 3.14159265
tekst = f'PI is equal to {pi:.4f}'
print(tekst)
