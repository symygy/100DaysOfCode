# Tutorial: https://www.youtube.com/watch?v=3dt4OGnU5sM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=20

'''Comprehensions'''
nums = [1,2,3,4,5,6,7,8,9,10]

# list = []
# for n in nums:
#     list.append(n)
# print(list)

# my_list = [n for n in nums]
# print(my_list)

# my_list = [n*n for n in nums]
# print(my_list)

# my_list = map(lambda n: n*n, nums)
# print(my_list)

# my_list = [n*n for n in nums if n%2==0]
# print(my_list)

# Tworzenie pary dla kazdej litery w 'abcd' i kazdej cyfry w '0123'
# my_list = [(l, n) for l, n in zip('abcd','0123')]
# print(my_list)

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# my_list = {k:v for k,v in zip(names, heroes)}
# print(my_list)

'''Generator expressions'''
def gen_exp(nums):
    for n in nums:
        yield n*n

my_list = (n*n for n in nums)
print(my_list)
for element in my_list:
    print(element)