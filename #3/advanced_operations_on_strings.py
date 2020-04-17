# tutorial: https://www.youtube.com/watch?v=vTX3IwquFkc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=22
import datetime

person = {'name' : 'Michal', 'age' : 29}
sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence)


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Miki', '29')
sentence = 'My name is {0.name} and I am {0.age} years old'.format(person)
print(sentence)

sentence = 'My name is {name} and I am {age} years old'.format(name = 'Marian', age='33')
print(sentence)

my_date = datetime.datetime(2020, 2, 21, 12, 30, 00)
print(my_date)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)

