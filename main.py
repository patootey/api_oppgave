import tkinter
import requests
from matplotlib import pyplot as plt

class Currency():
    def __init__(self):
        self.key = "https://api.frankfurter.app/"
    
    def chooser(self):
        self.fromCurrency = "from="+input("From (EUR): ")
        self.toCurrency1 = "to="+input("First to (NOK): ")
        self.toCurrency2 = input("Other to: ")
        return "?"+self.fromCurrency+"&"+self.toCurrency1+","+self.toCurrency2

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
        raw_data = self.fetch_data()
        rates = raw_data['rates']
        values1,values2 = [],[]
        for i in rates:
            values1.append(rates[i][self.toCurrency1[3:]])
            values2.append(rates[i][self.toCurrency2])
        return values1,values2

    def plotter(self):
        data = self.list_maker()
        plt.grid()
        plt.plot(data[0], color="blue")
        plt.plot(data[1], color="red")
        plt.ylabel(f"{self.fromCurrency[5:]} i valutaer")
        plt.xlabel(f"Tid fra {self.startDate} til {self.endDate}")
        plt.tick_params(axis='x', which='both', labelbottom=False)
        plt.legend([self.toCurrency1[3:],self.toCurrency2])
        plt.show()
        
penge = Currency()
penge.plotter()