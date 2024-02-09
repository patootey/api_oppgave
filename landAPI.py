import requests

countries = requests.get("https://restcountries.com/v3.1/all")
countries = countries.json()
def search(key:str):
    for country in countries:
            
        for code in country['name']:
            if code != "nativeName" and key.lower() in country['name'][code].lower():
                for name in country['currencies']:
                    code = name
                return country['name']['common'], country['currencies'][code]['name'], code, country['currencies'][code]["symbol"], country['flags']['png']
                

            elif code == "nativeName":
                for symbol in country['name'][code]:
                    for z in country['name'][code][symbol]:
                        if key.lower() in country['name'][code][symbol][z].lower():
                            for name in country['currencies']:
                                code = name
                            return country['name']['common'], country['currencies'][code]['name'], code, country['currencies'][code]["symbol"], country['flags']['png']
        try:
            for code in country['currencies']:
                if key.lower() == code.lower():
                    return country['name']['common'], country['currencies'][code]['name'], code, country['currencies'][code]["symbol"], country['flags']['png']
                
                for symbol in country['currencies'][code]:
                    if key.lower() == country['currencies'][code][symbol].lower():
                        return country['name']['common'], country['currencies'][code]['name'], code, country['currencies'][code]["symbol"], country['flags']['png']
        except:
            pass

    return f"Fant ikke landet '{key}'."