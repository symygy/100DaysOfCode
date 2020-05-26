# Tutorial: https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=42

class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first.lower() + '.' + last.lower() + '@company.com'

		# Odnosi sie do calej klasy w przeciwienstwie do self
		Employee.num_of_emps += 1


	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		# pracujemy na klasie zamiast na instancji klasy
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday == 6:
			return False
		return True

'''
static methods
Nie przekazuja nic automatycznie. Moga przekazywac instancje lub klase.
Działają jak zwykłe funkcje jednak wrzucamy je wewnatrz klasy ze wzgledu na to, że
sa powiazane w jakis posob z dana klasa.
'''

emp1 = Employee('Miki', 'Kiki', 10000)
emp2 = Employee('Test', 'User', 5000)

import datetime
my_date = datetime.date(2020, 7, 10)

print(Employee.is_workday(my_date))

# Employee.set_raise_amt(1.05)
#
# emp_str1 = 'Miki-Kiki-120000'
# emp_str2 = 'Marcin-Daniec-130000'
# emp_str3 = 'Maciej-Kanapka-140000'
#
# new_emp2 = Employee.from_string(emp_str2)
# print(new_emp2.email)

