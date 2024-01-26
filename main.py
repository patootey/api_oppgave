import tkinter
import requests

currencies = requests.get("https://api.frankfurter.app/currencies")
key = "https://api.frankfurter.app/"

current = "latest"
historical = "2008-09-15"
fromDate,toDate = "2008-09-15..", "2017-09-15"
query = False
fromCurrency = "from=EUR"
to = "to=USD"

request = requests.get(key+current)
request = request.json()
print(f"I datoen {request['date']} hadde valutaen {currencies.json()['USD']} en verdi på {request['rates']['USD']} i {request['base']}")
# print(currencies.json()["AUD"])
newkey = requests.get(key+fromDate+toDate+"?"+fromCurrency+"&"+to)
print(newkey.json())