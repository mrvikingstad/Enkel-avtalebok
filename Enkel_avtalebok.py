
from datetime import datetime




avtaler = []
kategorier = []

#d
class Avtale:

    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = str(tittel)
        self.sted = str(sted)
        self.starttidspunkt = datetime.fromisoformat(starttidspunkt)
        self.varighet = int(varighet)

    #e: __str__ metode for å printe ut avtaler på oversiktelig vis
    def __str__(self):
        return f"Avtalen angår: {self.tittel}\nLokasjon: {self.sted}\nTidspunkt: {self.starttidspunkt}\nAvtalen beregnes til å vare i omlag {self.varighet} minutter"

class Kategori:

    def __init__(self, id, navn, prioritet=1):
        self.id = str(id)
        self.navn = str(navn)
        self.prioritet = int(prioritet)

    def __str__(self):
        if self.prioritet == 1:
            prio = "Standard"
        elif self.prioritet == 2:
            prio = "Viktig"
        elif self.prioritet == 3:
            prio = "Svært viktig"
        return f"Viser informasjon for kategori med ID {self.id}:\nNavn : \"{self.navn}\"\nNåværende prioritet er satt til : \"{prio}\""

def ny_kategori():
    svar = "ja"
    while svar == "ja":
        kategori_id = input("Hvilken ID vil du gi kategorien?: ")
        kategori_navn = input("Hva vil du kalle kategorien?: ")
        kategori_prioritet = int(input("Hvor høyt vil du prioritere kategorien? (1 = standard, 2 = viktig, 3 = svært viktig): "))
        avtale_kategori = Kategori(kategori_id, kategori_navn, kategori_prioritet)
        kategorier.append(avtale_kategori)
        svar = input("Ny avtale? ja/nei: ")
    return avtale_kategori




#f: Gir brukeren muligheten til å legge inn flere avtaler
def ny_avtale():
    svar = "ja"
    while svar == "ja":
        avtale_tittel = input("Hva gjelder avtalen?: ")
        avtale_sted = input("Hvor er avtalen?: ")
        avtale_starttidspunkt = input("Når er avtalen? ÅÅÅÅ-MM-DD TT:MM:SS ")
        avtale_varighet = int(input("Hvor lenge varer den i minutter?: "))
        oppsatt_avtale = Avtale(avtale_tittel, avtale_sted, avtale_starttidspunkt, avtale_varighet)
        avtaler.append(oppsatt_avtale)
        svar = input("Ny avtale? ja/nei: ")
    return(avtaler)


#g: Skriver ut en liste med indekser og tittel på avtaler.
def avtale_bok(tittel):
    print(tittel)
    for i in range(len(avtaler)):
        print(f"{i}.: {avtaler[0+i].tittel}")


#h: Skriver lister til tekstfil i printet format (som ved bruk av __str__ funksjon)
def lag_fil():
    svar = input("Hva vil du kalle filen?: ")+".txt"
    with open(svar, 'w') as f:
        for line in avtaler:
            f.write(f"{line}\n")
    print(f"Filen er lagret som {svar}")

def lag_fil_kategorier():
    svar = input("Hva vil du kalle filen?: ")+".txt"
    with open(svar, 'w') as f:
        for line in kategorier:
            f.write(f"{line}\n")
    print(f"Filen er lagret som {svar}")


#i: Leser fil og printer ut til terminal
def les_fil():
    filnavn = input("Skriv navnet på filen: ")+".txt"
    with open(filnavn, 'r') as f:
        for line in f:
            print(line)
            avtaler.append(line)


#j: Printer ut liste av avtaler på bestemt dato
def dato_sjekk():
    svar = datetime.fromisoformat(input("Skriv inn datoen du har lyst å sjekke: (ÅÅÅÅ-MM-DD) ")).date()
    for dato in range(len(avtaler)):
        if svar == (avtaler[dato].starttidspunkt.date()):
            print("\nFølgende avtale(r) er funnet: ")
            print(avtaler[dato])
        else:
            print("Finner ingen avtale med forespurt dato.")
            break

#k: Søker etter titler på avtaler. Oppgaven tolkes som man ikke skal kunne søke etter sted.
def tittel_sjekk():
    svar = input("Skriv tittel på avtalen du har lyst å sjekke: ").lower()
    for tittel in range(len(avtaler)):
        if svar == (avtaler[tittel].tittel.lower()):
            print("\nFølgende avtale(r) er funnet: ")
            print(avtaler[tittel])
        else:
            print("Finner ingen avtale med forespurt tittel.")
            break

#m: Lar bruker slette avtale
def slett_avtale():
    i = 0
    for i in range(len(avtaler)):
        print(f"{i}. {avtaler[i].tittel}")
    svar = int(input("Hvilken avtale vil du slette?: "))
    del avtaler[svar]
    print("Avtalen er slettet. Disse avtalene gjenstår: ")
    for i in range(len(avtaler)):
        print(f"{i}. {avtaler[0+i].tittel}")
    print("Du tas tilbake til menyen.\n")
        
#n: Lar bruker redigere verdiene til valgt avtale
def rediger_avtale():
    i = 0
    for i in range(len(avtaler)):
        print(f"{i}. {avtaler[i].tittel}")
    svar = int(input("Hvilken avtale vil du endre?: "))
    print(f"\n1. Tittel: {avtaler[svar].tittel}")
    print(f"2. Sted: {avtaler[svar].sted}")
    print(f"3. Dato: {avtaler[svar].starttidspunkt}")
    print(f"4. Varighet: {avtaler[svar].varighet} minutter\n")
    svar2 = int(input("Hva ønsker du å endre?: (1-4) "))
    if svar2 == 1:
        print(f"\nForeløpig lokasjon er: {avtaler[svar].tittel}")
        svar3 = input("Hva ønsker du å endre tittelen til?: ")
        avtaler[svar].tittel = svar3
        print(f"Tittelen er endret til {svar3}\n")
    elif svar2 == 2:
        print(f"\nForeløpig lokasjon er: {avtaler[svar].sted}")
        svar4 = input("Hva ønsker du å endre lokasjonen til?: ")
        avtaler[svar].sted = svar4
        print(f"Lokasjon er endret til {svar4}\n")
    elif svar2 == 3:
        print(f"\nForeløpig dato og tid er satt til: {avtaler[svar].starttidspunkt}")
        svar5 = input("Hva ønsker du å endre tidspunktet til?: ")
        avtaler[svar].starttidspunkt = svar5
        print(f"Tidspunktet er endret til {svar5}\n")
    elif svar2 == 4:
        print(f"\nForeløpig varighet er satt til: {avtaler[svar].varighet} minutter")
        svar6 = input("Hva ønsker du å endre varigheten til?: ")
        avtaler[svar].varighet = svar6
        print(f"Varigheten er endret til {svar6} minutter\n")
    else:
        print("Ugyldig svar. Du tas tilbake til menyen.\n")
        pass

#Nytt menysystem som har en overordnet meny for å velge kategori eller avtaler
def hovedmeny():
    menyvalg2 = ["Avtaler", "Kategorier"]
    i = 0
    while True:
        for i in range(len(menyvalg2)):
            print(f"{i+1}. {menyvalg2[i]}")
        valg2 = int(input("Velg et alternativ: "))
        print(" ")
        if valg2 == 1:
            meny()
            continue
        elif valg2 == 2:
            kategorimeny()
            continue

#l: Menysystem
def meny():
    menyvalg = ["Lag ny avtale", "Les inn fil med avtaler", "Skriv avtaler til ny fil", "Slett avtale", "Rediger avtale", "Gå til hovedmeny", "Avslutt program"]
    i = 0
    while True:
        for i in range(len(menyvalg)):
            print(f"{i+1}. {menyvalg[i]}")
        valg = int(input("Velg et alternativ: "))
        print(" ")
        if valg == 1:
            ny_avtale()
            continue
        elif valg == 2:
            les_fil()
            continue
        elif valg == 3:
            lag_fil()
            continue
        elif valg == 4:
            slett_avtale()
            continue
        elif valg == 5:
            rediger_avtale()
            continue
        elif valg == 6:
            hovedmeny()
            continue
        elif valg == 7:
            print("Programmet avsluttes.")
            break
        else:
            print("\nOBS! Skriv et tall mellom 1 og 6.")
            continue

def kategorimeny():
    menyvalg3 = ["Lag ny kategori", "Les inn fil med kategorier", "Skriv kategorier til ny fil", "Gå til hovedmeny", "Avslutt program"]
    i = 0
    while True:
        for i in range(len(menyvalg3)):
            print(f"{i+1}. {menyvalg3[i]}")
        valg3 = int(input("Velg et alternativ: "))
        print(" ")
        if valg3 == 1:
            ny_kategori()
            continue
        elif valg3 == 2:
            les_fil()
            continue
        elif valg3 == 3:
            lag_fil_kategorier()
            continue
        elif valg3 == 4:
            hovedmeny()
            continue
        elif valg3 == 5:
            print("Programmet avsluttes.")
            break
        else:
            print("\nOBS! Skriv et tall mellom 1 og 5.")
            continue



if __name__ == "__main__":
    hovedmeny()
#    ny_kategori()