import requests

countries = requests.get("https://restcountries.com/v3.1/all")
countries = countries.json()
def search(key:str):
    for country in countries:
            
        for i in country['name']:
            if key in country['name'][i]:
                for name in country['currencies']:
                    symbol = name
                return country['name']['common'], symbol, country['currencies'][symbol]["symbol"]
                

            if i == "nativeName":
                for x in country['name'][i]:
                    for z in country['name'][i][x]:
                        if key in country['name'][i][x][z]:
                            for name in country['currencies']:
                                symbol = name
                            return country['name']['common'], symbol, country['currencies'][symbol]["symbol"]
    return f"Fant ikke landet '{key}'."
                    
                    
print(search("Norway"))
print(search("Norge"))
print(search("Britain"))
print(search("Lugudo"))