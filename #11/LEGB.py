# Tutorial: https://www.youtube.com/watch?v=QVdf0LgmICw&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=18

""""
LEGB
Local, Enclosing, Global, Built-in
"""

# import builtins
#
# # wyświetlanie wbudowanych funkcji
# print(dir(builtins))
#
# x = 'global x'
#
# m = min([5,1,3,4,2])
# print(m)
#
# # def test():
# # 	global x #definiowanie globalnej zmiennej
# # 	x = 'local x'
# # 	y = 'local y'
# # 	print(y)
# # 	print(x)
#
# def test(z):
# 	x = 'local x'
# 	y = 'local y'
# 	print(z)
#
# test('local z')


''' Enclosing '''
x = 'global x'

def outer():
	x = 'outer x'

	def inner():
		#nonlocal x
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()
print(x)