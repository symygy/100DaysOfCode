# Tutorial: https://www.youtube.com/watch?v=ng2o98k983k&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=46

from bs4 import BeautifulSoup
import requests
import csv


''' podstawy obslugi BS na przykladnie pliku example.html '''
# with open('example.html', 'r') as html_file:
# 	# lxml to jest parser jakiego chcemy uzyc
# 	soup = BeautifulSoup(html_file, 'lxml')

''' to znajduje tylko pierwsze napotkanie danego taga '''
# match = soup.title
# print(match)
# print(match.text)

''' zeby znalezc wszystkie wystapienia uzywamy find_all '''
''' podkreslenie po class jest dlatego ze slowo class jest slowem specjalnym w Pythonie '''
# find = soup.find('div', class_='footer')
# print(find)

# for article in soup.find_all('div', class_='article'):
# 	# print(article)
#
# 	headline = article.h2.a.text
# 	print(headline)
#
# 	summary = article.p.text
# 	print(summary)
# 	print()

''' Uzycie BS na przykladzie istniejacej strony WWW '''
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

csv_file = open('scrapped_info.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
	headline = article.h2.a.text
	summary = article.find('div', class_='entry-content').p.text

	try:
		''' Jeśli potrzebujemy dostępu do któregos z atrybutów, możemy odwołać się do niego jak w słownikach'''
		video_src = article.find('iframe', class_='youtube-player')['src']
		video_id = video_src.split('/')[4]
		video_id = video_id.split('?')[0]
		yt_link = f'https://youtube.com/watch?v={video_id}'
	except Exception as e:
		'''Jeśli dany post nie bedzie mial linka to przypisujemy mu wartosc None'''
		yt_link = None

	print(yt_link)
	print()

	csv_writer.writerow([headline, summary, yt_link])


csv_file.close()