import requests
from config import HEADERS
import json
import sys
import datetime
from dateutil.relativedelta import relativedelta

outbound_date = ''
inbound_date = 'anytime'
year = datetime.date.today().year

# today = datetime.date.today()
# six_months_later = today + relativedelta(months=+6)

def parse_data():
    querystring = {"inboundpartialdate": {inbound_date}}
    response = requests.request("GET", URL, headers=HEADERS, params=querystring)
    data = json.loads(response.text)
    return data

def print_results(data):
    for quote in data['Quotes']:
        destination_id = quote['OutboundLeg']['DestinationId']
        carrier_id = quote['OutboundLeg']['CarrierIds'][0]
        print(f"Oferta nr: {quote['QuoteId']} -> cena: {int(quote['MinPrice'])} zł -> kierunek: {places[destination_id]} "
              f"-> data wylotu: {quote['OutboundLeg']['DepartureDate'].split('T')[0]} -> przewoźnik: {carriers[carrier_id]}")

def create_places_dict(data):
    return {place['PlaceId']: place['Name'] for place in data['Places']}

def create_carriers_dict(data):
    return {carrier['CarrierId']: carrier['Name'] for carrier in data['Carriers']}

def set_outbound_date(outbound_day, outbound_month, outbound_year):
    return datetime.date(int(outbound_year), int(outbound_month), int(outbound_day))

# def set_inbound_date(inbound_day, inbound_month):
#     return datetime.date(year, int(inbound_month), int(inbound_day))

while True:
    print("""
        *** Wyszukiwarka tanich lotów ***
        1. Dowolna data
        2. Wybierz datę wylotu
        0. Zakończ

        Wpisz odpowiedni numer i zatwierdź klawiszem ENTER:
    """)

    choice = input()

    if choice == '1':
        outbound_date = 'anytime'
    elif choice == '2':
        day_outbound = input("Podaj planowany dzień wylotu: ")
        month_outbound = input("Podaj planowany miesiąc wylotu: ")
        year_outbound = input("Podaj planowany rok wylotu: ")
        outbound_date = set_outbound_date(day_outbound, month_outbound, year_outbound)
    elif choice == '0':
        sys.exit()
    else:
        print("Nie ma takiego numeru!")

    if outbound_date == '' or inbound_date == '':
        print("Wybrano niepoprawną datę !")
    else:
        URL = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/PL/PLN/pol-PL/KRK-sky/anywhere/{outbound_date}"
        data = parse_data()
        print(f"\n*** WYŚWIETLAM LOTY W TERMINIE: {outbound_date} - {inbound_date} ***\n")

        if len(data['Quotes']) == 0 or len(data['Places']) == 0 or len(data['Carriers']) == 0:
            print('Brak dostępnych lotów.')
        else:
            places = create_places_dict(data)
            carriers = create_carriers_dict(data)
            print_results(data)
