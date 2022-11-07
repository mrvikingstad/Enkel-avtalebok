
from datetime import datetime




avtaler = []

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


#f: Gir brukeren muligheten til å legge inn flere avtaler
def ny_avtale():
    svar = "ja"
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
def lag_fil():
    svar = input("Hva vil du kalle filen?: ")+".txt"
    with open(svar, 'w') as f:
        for line in avtaler:
            f.write(f"{line}\n")


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


#l: Menysystem
def meny():
    menyvalg = ["Lag ny avtale", "Les inn fil med avtaler", "Skriv avtaler til ny fil", "Slett avtale", "Rediger avtale", "Avslutt program"]
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
            print("Programmet avsluttes.")
            break
        else:
            print("\nOBS! Skriv et tall mellom 1 og 6.")
            continue

if __name__ == "__main__":
    meny()