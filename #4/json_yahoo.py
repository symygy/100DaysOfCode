import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/currencies/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAFgw5FpTrx96-6_4vuSLXO9xjBpdrS0KgMS7zGhhlqDG9TBGyez7gxDsCLTxBEGc2Gv9uLYXf7K1jx2VrMZshuNa8GtUO6QukjLJZyx4dXaJ_e3wrAY6qO8zUchs_DYpCWxHZtyH6SUkocRPMskNilpn_lW6BydtgZ0M1JY9IbA2") as response:
    source = response.read()

print(source)

data = json.loads(source)

print(json.dumps(data, indent=2))