# Tutorial: https://www.youtube.com/watch?v=K8L6KVGG-7o&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=30
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321--555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# raw strings - python nie interpretuje znakow poprzedzonych backslashem jako np: znaku nowej linii \n
# word boundary to np: spacja
# () grupuje patterny

# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d\d\d\*\d\d\d\*\d\d\d\d')
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

# flaga ignorecase to ignorowania wielkosci liter
pattern = re.compile(r'start', re.IGNORECASE)


# matches = pattern.finditer(text_to_search)
# matches = pattern.findall(text_to_search)
# match nie jest iterowalny, pokazuje pozycje wzioru w tekscie
# matches = pattern.match(sentence)
matches = pattern.search(sentence)

print(matches)

for match in matches:
	print(match)

# with open('data.txt', 'r') as file:
# 	contents = file.read()
#
# 	matches = pattern.finditer(contents)
#
# 	for match in matches:
# 		print(match)


# print(text_to_search[1:4])