import tkinter
import requests

currencies = requests.get("https://api.frankfurter.app/currencies")
key = "https://api.frankfurter.app/"
addon = "latest"
request = requests.get(key+addon)
request = request.json()
print(f"I datoen {request['date']} hadde valutaen {currencies.json()['USD']} en verdi på {request['rates']['USD']} i {request['base']}")
# print(currencies.json()["AUD"])