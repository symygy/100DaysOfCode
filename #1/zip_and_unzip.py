# Tutorial: https://youtu.be/z0gguhEmWiY?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

import zipfile
import shutil
import requests

# my_zip = zipfile.ZipFile('files.zip', 'w')
#
# my_zip.write('test.txt')
# my_zip.write('test.bmp')
# my_zip.write('test.docx')
#
# my_zip.close()


"""Mozna to zapisac inaczej z wykorzystaniem context managera"""

# with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.write('test.txt')
#     my_zip.write('test.bmp')
#     my_zip.write('test.docx')

# with zipfile.ZipFile('prezentacja.zip', 'r') as my_zip:
#     print(my_zip.namelist())
#     my_zip.extractall('unziped')
#     my_zip.extract('prezentacja-dab.pdf')

'''Można użyć do pakowania folderów'''
#shutil.make_archive('another_one', 'zip', 'unziped')
#shutil.unpack_archive('another_one.zip', 'another_dir')

scrap = requests.get('https://github.com/symygy/RSSFeedParser/archive/master.zip')
with open('data.zip', 'wb') as file:
    file.write(scrap.content)

with zipfile.ZipFile('data.zip', 'r') as data_zip:
    print(data_zip.namelist())




