import requests

countries = requests.get("https://restcountries.com/v3.1/all")
countries = countries.json()
def search(key:str):
    for number in range(len(countries)):
        
        for i in countries[number]['name']:
            if i == "nativeName":
                for x in countries[number]['name'][i]:
                    for z in countries[number]['name'][i][x]:
                        if key in countries[number]['name'][i][x][z]:
                            for name in countries[number]['currencies']:
                                z = name
                            return countries[number]['name']['official'], z
                    
                    
            if key in countries[number]['name'][i]:
                for name in countries[number]['currencies']:
                    z = name
                return countries[number]['name']['official'], z
print(search("Norway"))
print(search("Norge"))
print(search("Noreg"))