
from datetime import datetime


#d
class Avtale:

    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = str(tittel)
        self.sted = str(sted)
        self.starttidspunkt = datetime.fromisoformat(starttidspunkt)
        self.varighet = int(varighet)

    #e: __str__ metode for å printe ut avtaler på oversiktelig vis
    def __str__(self):
        return f"Avtalen angår: {self.tittel}\nLokasjon: {self.sted}\n{self.starttidspunkt}\nAvtalen beregnes til å vare i omlag {self.varighet} minutter"


#f: Gir brukeren muligheten til å legge inn flere avtaler
def ny_avtale():
    svar = "ja"
    global avtaler
    avtaler = []
    while svar == "ja":
        avtale_tittel = input("Hva gjelder avtalen?: ")
        avtale_sted = input("Hvor er avtalen?: ")
        avtale_starttidspunkt = input("Når er avtalen? ÅÅÅÅ-MM-DD TT:MM:SS ")
        avtale_varighet = int(input("Hvor lenge varer den i minutter?: "))
        oppsatt_avtale = Avtale(avtale_tittel, avtale_sted, avtale_starttidspunkt, avtale_varighet)
        svar = input("Ny avtale? ja/nei: ")
        avtaler.append(oppsatt_avtale)
    return(avtaler)


#g: Skriver ut en liste med indekser og tittel på avtaler. Har frivillig laget en funksjon mer_info() som skriver ut mer info om avtalen man forespør ved indeks
def avtale_bok(tittel):
    print(tittel)
    for i in range(len(avtaler)):
        print(f"{i}.: {avtaler[0+i].tittel}")


#h: Skriver lister til tekstfil i printet format (som ved bruk av __str__ funksjon)
def lag_fil(liste):
    with open('Avtale_liste.txt', 'w') as f:
        for line in liste:
            f.write(f"{line}\n")


#i: Leser fil og printer ut til terminal
def les_fil():
    with open('Avtale_liste.txt', 'r') as f:
        for line in f:
            print(line)


#j: Printer ut liste av avtaler på bestemt dato
def dato_sjekk():
    svar = datetime.fromisoformat(input("Skriv inn datoen du har lyst å sjekke: (ÅÅÅÅ-MM-DD) ")).date()
    for dato in range(len(avtaler)):
        if svar == (avtaler[dato].starttidspunkt.date()):
            print(avtaler[dato])


#Funksjon laget frivillig
def mer_info():
    svar = input("Vil du se mer info om en bestemt avtale? ja/nei: ")
    while True:
        if svar == "ja":
            indeks = int(input("Hvilken avtale vil du se nærmere på?: "))
            print(avtaler[indeks])
            break
        elif svar != "nei":
            # fiks
            pass
        else:
            pass    



if __name__ == "__main__":
    ny_avtale()
    avtale_bok("Avtaler")
#    mer_info()
#    lag_fil(avtaler)
#    les_fil()
    dato_sjekk()