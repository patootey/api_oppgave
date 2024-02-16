import requests
from matplotlib import pyplot as plt

def search(key:str):
    """
    Funksjon for å søke gjennom restcountries API der den returnerer landets navn, valutanavn
    -kode og -symbol, og en PNG av landets flagg

    Parametere:
        key (string): Nøkkelen brukeren oppgir for å søke i datasettet
    """
    countries = requests.get("https://restcountries.com/v3.1/all")
    countries = countries.json()

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
    """
    Klasse for å la brukeren sette sammen en forespørsel, hente data fra valuta API
    og lage en graf med valutaens endring gjennom tid. 

    Attributt:
        key (string): første delen av forespørselen til API-et
    """
    def __init__(self):
        self.key = "https://api.frankfurter.app/"
    
    def chooser(self):
        """
        Metode som lar brukeren oppgi det som skal søkes etter i search funksjonen

        Attributter:
            fromCurrency (list): liste som inneholder de returnerte verdiene til search()
            toCurrency1  (list): samme som over
            toCurrency2  (list): samme som over

        Returner: 
            en string som skal legges til key
        """
        self.fromCurrency = search(input("Gi land fra: "))
        self.toCurrency1 = search(input("Gi land til 1: "))
        self.toCurrency2 = search(input("Gi land til 2: "))

        return "?from="+self.fromCurrency[2]+"&to="+self.toCurrency1[2]+","+self.toCurrency2[2]

    def set_date(self):
        """
        Metode som bruker input til å sette et tidsintervall for sammenlikningen

        Attributter:
            startDate (string): starten på intervallet som skrives i formatet slik vist
            endDate   (string): slutten på intervallet, der to punktum (..) gir verdier til dags dato
        
        Returnerer:
            En sammenslåing av de to strengene over som skal legges til i key
        """
        self.startDate = input("Start (YYYY-MM-DD): ")
        self.endDate = input("End (..YYYY-MM-DD): ")
        return self.startDate + self.endDate


    def fetch_data(self):
        """
        Metode som slår sammen key og ber om dataen fra API-et

        Returnerer:
            Dataen fra API i JSON format som tilsvarer en dictionary i Python
        """
        self.key += self.set_date() + self.chooser()
        print(self.key)
        self.key = requests.get(self.key)
        return self.key.json()
    
    
    def list_maker(self, data):
        """
        Metode der dataen fra API-et blir satt inn i to lister som senere skal plottes
        Dersom det oppstår en feil med listene så returnerer metoden en string som bearbeides i neste metode
        Hvis ikke legger den inn alle mulige verdier i to lister
        
        Parametere:
            data (list): en parameter som du kan gi en bestemt verdi eller la være for å få data fra fetch_data

        Returnerer:
            Enten listene
            Eller en string
        """
        try:
            raw_data = data
            if data == None:
                raw_data = self.fetch_data()
            rates = raw_data['rates']

            values1,values2 = [],[]
            for i in rates:
                try:values1.append(rates[i][self.toCurrency1[2]])
                except:pass
                
                try:values2.append(rates[i][self.toCurrency2[2]])
                except:pass
            return values1,values2
        except Exception as e:
            return e

    def plotter(self, data=None):
        """
        Metode som bruker listene tidligere definert, gitt at det fungerte, og plotter det
        Dersom dataen er en string stopper metoden og erroren skal behandles

        Returnerer:
            Den plottede figuren som skal bearbeides i tkinter, fig
            Dersom det er noen feilmeldinger befinner de seg i listen error
        """
        data = self.list_maker(data)
        if type(data) == str:
            return data
        
        fig, ax = plt.subplots()
        ax.grid()
        ax.plot(data[0], color="blue")
        ax.plot(data[1], color="red")
        ax.set_ylabel(f"{self.fromCurrency[2]} i valutaer")
        ax.set_xlabel(f"Tid fra {self.startDate} til {self.endDate}")
        ax.tick_params(axis='x', which='both', labelbottom=False)
        ax.legend([self.toCurrency1[2],self.toCurrency2[2]])
        error = []
        for i in data:
            if len(i) == 0 or len(i) < len(data[0] if data[1] == i else data[1]):
                error.append(0 if i == data[0] else 1)
        return fig, error
        
penge = Currency()
