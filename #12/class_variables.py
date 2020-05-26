# Tutorial: https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=41
#

class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first.lower() + '.' + last.lower() + '@company.com'

		Employee.num_of_emps += 1


	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Miki', 'Kiki', 10000)
emp2 = Employee('Test', 'User', 5000)

# print(emp1.raise_amount)
# # print(emp2.raise_amount)
# # print(Employee.raise_amount)
# # Employee.raise_amount = 1.05
# # print(Employee.raise_amount)

print(Employee.num_of_emps)
print(emp1.num_of_emps)

# Wyswietlenie namespace'a dla danego obiektu
#print(emp1.__dict__)