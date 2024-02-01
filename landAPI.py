import requests

countries = requests.get("https://restcountries.com/v3.1/all")
countries = countries.json()
def search(key:str):
    for country in countries:
            
        for i in country['name']:
            if i != "nativeName" and key.lower() in country['name'][i].lower():
                for name in country['currencies']:
                    symbol = name
                return country['name']['common'], symbol, country['currencies'][symbol]["symbol"], country['flags']['png']
                

            elif i == "nativeName":
                for x in country['name'][i]:
                    for z in country['name'][i][x]:
                        if key.lower() in country['name'][i][x][z].lower():
                            for name in country['currencies']:
                                symbol = name
                            return country['name']['common'], symbol, country['currencies'][symbol]["symbol"], country['flags']['svg']
    return f"Fant ikke landet '{key}'."
                    
                    
print(search("Norway"))
print(search("Norge"))
print(search("briTain"))
print(search("Lugudo"))
print(search("vietnam"))
print(search("deutschland"))