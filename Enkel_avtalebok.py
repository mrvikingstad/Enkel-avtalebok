
from datetime import datetime







#d
class Avtale:

    def __init__(self, tittel, sted, starttidspunkt, varighet, kategori=" "):
        self.tittel = str(tittel)
        self.sted = str(sted)
        self.starttidspunkt = datetime.fromisoformat(starttidspunkt)
        self.varighet = int(varighet)
        self.kategori = kategori

  #  e: __str__ metode for å printe ut avtaler på oversiktelig vis
    def __str__(self):
        return f"\nAvtalen angår: {self.tittel}\nLokasjon: {self.sted}\nTidspunkt: {self.starttidspunkt}\nAvtalen beregnes til å vare i omlag {self.varighet} minutter.\nAvtalen er tilegnet følgende kategorier: {self.kategori.navn}"
    
    avtaler = []
    kategorier = []
 
    def legg_til_kategori(kategori):
        Avtale.avtaler[-1].kategori = Avtale.kategorier[kategori]
        return Avtale.avtaler


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
        return f"\n\nViser informasjon for kategori med ID {self.id}:\nNavn : \"{self.navn}\"\nNåværende prioritet er satt til : \"{prio}\""

def ny_kategori():
    svar = "ja"
    while svar == "ja":
        kategori_id = input("Hvilken ID vil du gi kategorien?: ")
        kategori_navn = input("Hva vil du kalle kategorien?: ")
        kategori_prioritet = int(input("Hvor høyt vil du prioritere kategorien? (1 = standard, 2 = viktig, 3 = svært viktig): "))
        avtale_kategori = Kategori(kategori_id, kategori_navn, kategori_prioritet)
        Avtale.kategorier.append(avtale_kategori)
        svar = input("Ny kategori? ja/nei: ")
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
        Avtale.avtaler.append(oppsatt_avtale)
        ny_kategori = input("Ønsker du å tilegne avtalen en kategori? ja/nei: ")
        if ny_kategori == "ja":
            i = 0
            z = 0
            for i in range(len(Avtale.kategorier)):
                try:
                    print(f"{abs(i-z)}. {Avtale.kategorier[i].navn}")
                    z + 1
                except AttributeError:
                    continue
            hvilken = int(input("Hvilken kategori vil du tilegne avtalen?: "))
            while True:
                Avtale.legg_til_kategori(hvilken)
                break
        else:
            pass
        svar = input("Ny avtale? ja/nei: ")
    print("Du tas tilbake til menyen\n")
    return(Avtale.avtaler)


#g: Skriver ut en liste med indekser og tittel på avtaler.
def avtale_bok():
    if len(Avtale.avtaler) != 0:
        print("Skriver ut liste for avtalene i avtaleboken:")
        for i in range(len(Avtale.avtaler)):
            print(f"{i}.: {Avtale.avtaler[0+i].tittel}")
    else:
        print("Avtaleboken er tom!\n")

def kategori_bok():
    if len(Avtale.kategorier) != 0:
        print("Skriver ut liste for kategoriene du har opprettet:")
        for i in range(len(Avtale.kategorier)):
            print(f"{i}.: {Avtale.kategorier[0+i].navn}")
    else:
        print("Du har ikke opprettet noen kategorier.")

#h: Skriver lister til tekstfil i printet format (som ved bruk av __str__ funksjon)
def lag_fil():
    if len(Avtale.avtaler) != 0:
        svar = input("Hva vil du kalle filen?: ")+".txt"
        with open(svar, 'w') as f:
            for line in Avtale.avtaler:
                f.write(f"{line}\n")
        print(f"Filen er lagret som {svar}")
    else:
        print("Du har ingen avtaler å skrive til fil.\n")

def lag_fil_kategorier():
    if len(Avtale.kategorier) != 0:
        svar = input("Hva vil du kalle filen?: ")+".txt"
        with open(svar, 'w') as f:
            for line in Avtale.kategorier:
                f.write(f"{line}\n")
        print(f"Filen er lagret som {svar}")
    else:
        print("Du har ikke opprettet noen kategorier.\n")


#i: Leser fil og printer ut til terminal
def les_fil():
    filnavn = input("Skriv navnet på filen: ")+".txt"
    with open(filnavn, 'r') as f:
        for line in f:
            print(line)
            Avtale.avtaler.append(line)


#j: Printer ut liste av avtaler på bestemt dato
def dato_sjekk():
    if len(Avtale.avtaler) != 0:
        svar = datetime.fromisoformat(input("Skriv inn datoen du har lyst å sjekke: (ÅÅÅÅ-MM-DD) ")).date()
        for dato in range(len(Avtale.avtaler)):
            if svar == (Avtale.avtaler[dato].starttidspunkt.date()):
                print("\nFølgende avtale(r) er funnet: ")
                print(Avtale.avtaler[dato])
            else:
                print("Finner ingen avtale med forespurt dato.")
                break
    else:
        print(" ")
        print("Avtaleboken er tom!\n")


#k: Søker etter titler på avtaler. Oppgaven tolkes som man ikke skal kunne søke etter sted.
def tittel_sjekk():
    if len(Avtale.avtaler) != 0:
        svar = input("Skriv tittel på avtalen du har lyst å sjekke: ").lower()
        for tittel in range(len(Avtale.avtaler)):
            if svar == (Avtale.avtaler[tittel].tittel.lower()):
                print("\nFølgende avtale(r) er funnet: ")
                print(Avtale.avtaler[tittel])
            else:
                print("Finner ingen avtale med forespurt tittel.")
                break
    else:
        print(" ")
        print("Avtaleboken er tom!\n")

#m: Lar bruker slette avtale
def slett_avtale():
    i = 0
    if len(Avtale.avtaler) != 0:
        for i in range(len(Avtale.avtaler)):
            print(f"{i}. {Avtale.avtaler[i].tittel}")
        svar = int(input("Hvilken avtale vil du slette?: "))
        del Avtale.avtaler[svar]
        print("Avtalen er slettet. Disse avtalene gjenstår: ")
        for i in range(len(Avtale.avtaler)):
            print(f"{i}. {Avtale.avtaler[0+i].tittel}")
        print("Du tas tilbake til menyen.\n")
    else:
        print("Avtaleboken er tom!\n")
        
#n: Lar bruker redigere verdiene til valgt avtale
def rediger_avtale():
    
    i = 0
    if len(Avtale.avtaler) != 0:
        for i in range(len(Avtale.avtaler)):
            print(f"{i}. {Avtale.avtaler[i].tittel}")
        svar = int(input("Hvilken avtale vil du endre?: "))
        print(f"\n1. Tittel: {Avtale.avtaler[svar].tittel}")
        print(f"2. Sted: {Avtale.avtaler[svar].sted}")
        print(f"3. Dato: {Avtale.avtaler[svar].starttidspunkt}")
        print(f"4. Varighet: {Avtale.avtaler[svar].varighet} minutter\n")
        svar2 = int(input("Hva ønsker du å endre?: (1-4) "))
        if svar2 == 1:
            print(f"\nForeløpig lokasjon er: {Avtale.avtaler[svar].tittel}")
            svar3 = input("Hva ønsker du å endre tittelen til?: ")
            Avtale.avtaler[svar].tittel = svar3
            print(f"Tittelen er endret til {svar3}\n")
        elif svar2 == 2:
            print(f"\nForeløpig lokasjon er: {Avtale.avtaler[svar].sted}")
            svar4 = input("Hva ønsker du å endre lokasjonen til?: ")
            Avtale.avtaler[svar].sted = svar4
            print(f"Lokasjon er endret til {svar4}\n")
        elif svar2 == 3:
            print(f"\nForeløpig dato og tid er satt til: {Avtale.avtaler[svar].starttidspunkt}")
            svar5 = input("Hva ønsker du å endre tidspunktet til?: ")
            Avtale.avtaler[svar].starttidspunkt = svar5
            print(f"Tidspunktet er endret til {svar5}\n")
        elif svar2 == 4:
            print(f"\nForeløpig varighet er satt til: {Avtale.avtaler[svar].varighet} minutter")
            svar6 = input("Hva ønsker du å endre varigheten til?: ")
            Avtale.avtaler[svar].varighet = svar6
            print(f"Varigheten er endret til {svar6} minutter\n")
        else:
            print("Ugyldig svar. Du tas tilbake til menyen.\n")
            pass
    else:
        print("Avtaleboken er tom!\n")



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
        elif valg2 == 3:
            exit()

#l: Menysystem
def meny():
    menyvalg = ["Lag ny avtale", "Les inn fil med avtaler", "Skriv avtaler til ny fil", "Se alle avtaler", "Slett avtale", "Rediger avtale", "Søk etter avtale", "Gå til hovedmeny", "Avslutt program"]
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
            avtale_bok()
            continue
        elif valg == 5:
            slett_avtale()
            continue
        elif valg == 6:
            rediger_avtale()
            continue
        elif valg == 7:
            sokemeny()
        elif valg == 8:
            hovedmeny()
        elif valg == 9:
            print("Programmet avsluttes.")
            exit()
        else:
            print("\nOBS! Skriv et tall mellom 1 og 9.")
            continue


def sokemeny():
    menyvalg = ["Søk etter tittel", "Søk etter sted", "Gå tilbake til avtalemeny"]
    i = 0
    while True:
        for i in range(len(menyvalg)):
            print(f"{i+1}. {menyvalg[i]}")
        valg = int(input("Velg et alternativ: "))
        if valg == 1:
            tittel_sjekk()
            continue
        elif valg == 2:
            dato_sjekk()
            continue
        elif valg == 3:
            print(" ")
            meny()
        else:
            print("\nOBS! Skriv et tall mellom 1 og 3.")
            continue


def kategorimeny():
    menyvalg3 = ["Lag ny kategori", "Les inn fil med kategorier", "Vis alle kategorier", "Skriv kategorier til ny fil", "Gå til hovedmeny", "Avslutt program"]
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
            kategori_bok()
            continue
        elif valg3 == 5:
            hovedmeny()
        elif valg3 == 6:
            print("Programmet avsluttes.")
            break
        else:
            print("\nOBS! Skriv et tall mellom 1 og 6.")
            continue



if __name__ == "__main__":
    hovedmeny()
#    ny_kategori()