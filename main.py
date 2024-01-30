import tkinter
import requests
from matplotlib import pyplot as plt

class Currency():
    def __init__(self):
        self.key = "https://api.frankfurter.app/"
    
    def chooser(self):
        self.fromCurrency = "from="+input("From (EUR): ")
        self.toCurrency = "to="+input("To (NOK,USD,GBP): ")
        return "?"+self.fromCurrency+"&"+self.toCurrency

    def set_date(self):
        self.startDate = input("Start (YYYY-MM-DD): ")
        self.endDate = input("End (..YYYY-MM-DD): ")

    def time(self):
        check = input("Current values? Y/N: ")
        if check.lower() == "y":
            return "latest"
        else:
            self.set_date()
            return self.startDate + self.endDate

    def fetch_data(self):
        self.key += self.time() + self.chooser()
        print(self.key)
        self.key = requests.get(self.key)
        return self.key.json()
    
    def list_maker(self):
        goob = self.fetch_data()
        base = goob['base']
        rates = goob['rates']
        values = []
        for i in rates:
            values.append(rates[i]['NOK'])
        return values

    def plotter(self):
        data = self.list_maker()
        plt.plot(data)
        plt.ylabel(f"{self.toCurrency[3:]} i {self.fromCurrency[5:]}")
        plt.xlabel(f"Tid fra {self.startDate} til {self.endDate}")
        plt.show()
        
penge = Currency()
penge.plotter()