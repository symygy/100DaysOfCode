# Tutorial: https://www.youtube.com/watch?v=bkpLhQd6YQM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=29

import csv

html_output = ''
titles = []


# with open('example_file.csv', 'r') as file:
#     csv_data = csv.reader(file)
#     # tworzona jest zmienna ktora dziala jak generator, czyli musimy albo iterowac po takim obiekcie, albo skonwertowac do listy tracac wszystkie zalety generatorow
#
#     # nie potrzebuję naglowkow
#     next(csv_data)
#
#     for line in csv_data:
#         titles.append(f'{line[2]} - {line[0]}')
#
# html_output += f'<p>W pliku jest {len(titles)} filmów!</p>'
# html_output += '\n<ul>'
# for movie in titles:
#     html_output += f'\n\t<li>{movie}</li>'
# html_output += '\n</ul>'
# print(html_output)


'''DictionaryReader'''
with open('example_file.csv', 'r') as file:
    csv_data = csv.DictReader(file)

    for line in csv_data:
        titles.append(f"{line['Title']} - {line['Year']}")

html_output += f'<p>W pliku jest {len(titles)} filmów!</p>'
html_output += '\n<ul>'
for movie in titles:
    html_output += f'\n\t<li>{movie}</li>'
html_output += '\n</ul>'
print(html_output)