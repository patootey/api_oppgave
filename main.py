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

    def sammensveising(self):
        self.key += self.time() + self.chooser()
        print(self.key)
        self.key = requests.get(self.key)
        return self.key.json()
    
    def printer(self):
        print(self.sammensveising())
penge = Currency()
penge.printer()