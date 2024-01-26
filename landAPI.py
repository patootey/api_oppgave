import requests

countries = requests.get("https://restcountries.com/v3.1/all")
countries = countries.json()
print(countries[0]['name']['official'])
for i in countries[10]['name']:
    if i == "nativeName":
        for x in countries[10]['name'][i]:
            if "Norway" in countries[10]['name'][i][x]:
                print(x)
    if "Norway" in countries[10]['name'][i]:
        print(countries[10]['name'][i])
    
# print(countries[10]['name'])
# print(countries[10]['currencies'])
# for i in countries[10]['currencies']:
#     print(i)