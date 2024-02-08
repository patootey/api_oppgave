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
                            return country['name']['common'], symbol, country['currencies'][symbol]["symbol"], country['flags']['png']
        try:
            for i in country['currencies']:
                if key.lower() == i.lower():
                    return country['name']['common'], i, country['currencies'][i]["symbol"], country['flags']['png']
                for x in country['currencies'][i]:
                    if key.lower() == country['currencies'][i][x].lower():
                        return country['name']['common'], i, country['currencies'][i]["symbol"], country['flags']['png']
        except:
            pass
    
    return f"Fant ikke {key}."
                    
print(search("British Pound"))
print(search("NOK"))