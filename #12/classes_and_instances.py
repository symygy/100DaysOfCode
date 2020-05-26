# Tutorial: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=40

class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first.lower() + '.' + last.lower() + '@company.com'

	def fullname(self):
		return f'{self.first} {self.last}'

emp1 = Employee('Miki', 'Kiki', 10000)
emp2 = Employee('Test', 'User', 5000)


