from bs4 import BeautifulSoup
import requests
import schedule
from time import sleep
import datetime

URL = 'https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=BIOMEDLUB'

def cyclic_job():
	source = requests.get(URL)
	source.encoding = 'utf-8'

	soup = BeautifulSoup(source.text, 'lxml')

	notowania = soup.find('div', class_='boxContent boxTable').table.tbody
	kurs = soup.find('div', class_='profilLast')

	print(datetime.datetime.now())
	print('-----------------------------------------------------------')
	print(f'Aktualny kurs: {kurs.text}')
	print()

	for tr in notowania.find_all('tr'):
		td_bolded = tr.find('td', class_='textBold').text
		if td_bolded == '':
			continue
		else:
			print(f'{tr.td.text} {td_bolded}')

	print('-----------------------------------------------------------')

schedule.every(1).minutes.do(cyclic_job)

cyclic_job()

while True:
	schedule.run_pending()
	sleep(1)