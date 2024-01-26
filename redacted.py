# currencies = requests.get("https://api.frankfurter.app/currencies")

list = ["USD","EUR","NOK"]
string = ""
for i in list:string+=i+","


# current = "latest"
# historical = "2008-09-15"
# fromDate,toDate = "2008-09-15..", "2017-09-15"
        

# query = True
# fromCurrency = "from="
# to = "to="

# if query:
#     key += current + "?" + fromCurrency + "GBP"
# printable = requests.get(key)
# print(key)
# print(printable.json())

# request = requests.get(key+current)
# request = request.json()
# print(f"I datoen {request['date']} hadde valutaen {currencies.json()['USD']} en verdi på {request['rates']['USD']} i {request['base']}")
# # print(currencies.json()["AUD"])
# newkey = requests.get(key+fromDate+toDate+"?"+fromCurrency+"&"+to)
# print(newkey.json())