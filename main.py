import tkinter
import requests

response = requests.get("https://api.frankfurter.app/currencies")

print(response.json()["AUD"])