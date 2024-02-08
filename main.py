import tkinter
import requests
from matplotlib import pyplot as plt

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

class Currency():
    def __init__(self):
        self.key = "https://api.frankfurter.app/"
        self.query = input("Land(1) eller valuta(2): ")
    
    def chooser(self):
        if int(self.query) == 1:
            self.fromCurrency = search(input("Gi land fra: "))
            self.toCurrency1 = search(input("Gi land til 1: "))
            self.toCurrency2 = search(input("Gi land til 2: "))

            self.fromCurrency = "from="+self.fromCurrency[2]
            self.toCurrency1 = "to="+self.toCurrency1[2]
            self.toCurrency2 = self.toCurrency2[2]
        else:
            self.fromCurrency = "from="+input("From (EUR): ")
            self.toCurrency1 = "to="+input("First to (NOK): ")
            self.toCurrency2 = input("Other to: ")
        return "?"+self.fromCurrency+"&"+self.toCurrency1+","+self.toCurrency2

    def set_date(self):
        self.startDate = input("Start (YYYY-MM-DD): ")
        self.endDate = input("End (..YYYY-MM-DD): ")
        return self.startDate + self.endDate


    def fetch_data(self):
        self.key += self.set_date() + self.chooser()
        print(self.key)
        self.key = requests.get(self.key)
        return self.key.json()
    
    
    
    def list_maker(self, data):
        raw_data = data
        if data != None:
            raw_data = self.fetch_data()
        print(raw_data)
        rates = raw_data['rates']
        values1,values2 = [],[]
        for i in rates:
            try:values1.append(rates[i][self.toCurrency1[3:]])
            except:pass
            try:values2.append(rates[i][self.toCurrency2])
            except:pass
        return values1,values2

    def plotter(self, data=None):
        data = self.list_maker(data)
        plt.grid()
        plt.plot(data[0], color="blue")
        plt.plot(data[1], color="red")
        plt.ylabel(f"{self.fromCurrency[5:]} i valutaer")
        plt.xlabel(f"Tid fra {self.startDate} til {self.endDate}")
        plt.tick_params(axis='x', which='both', labelbottom=False)
        plt.legend([self.toCurrency1[3:],self.toCurrency2])
        plt.show()
        
penge = Currency()
penge.plotter(search('russia'))