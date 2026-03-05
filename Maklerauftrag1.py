# leere Liste, wo später die Räume gespeichert werden, die eingegeben werden
raeume = []
# Variable für Flächenberechnung, wird später mit den Eingaben des Users addiert
gesamtflaeche= 0.0
"""erster Versuch"""

# Hauptschleife des Programms
while True:

# Variable, um den Input des Users zu speichern
    raum_name =input("Raumname oder ende: ")

# Eingabe wird in Kleinbuchstaben umgewandelt, falls im Input mind. ein Großbuchstabe drin ist; falls Input übereinstimmt
# mit "ende" soll die Schleife unterbrochen werden 
    if raum_name.lower() == "ende":
        break

# try except: Probiere alles im Try-Block aus; alles andere, was Fehler auswirft, soll mit dem Except aufgefangen werden (Programm soll nicht angehalten werden)
    try:
        # Input ist ein String, daher wird er in einen Float umgewandelt, User soll Länge & Breite des Raums eingeben, wird in Variablen gespeichert
        laenge = float(input(f"Länge {raum_name}: "))
        breite = float(input(f"Breite {raum_name}: "))

        # Berechnung der Fläche des Raums
        flaeche = laenge * breite

        # Eingaben werden in ein Dictionary gespeichert
        raum_daten = {"name" : raum_name, "quadratmeter": flaeche}

        # Dictionary wird hinzugefügt zur Liste raeume
        raeume.append(raum_daten)

        #Ausgabe des Raum-Namens & der Fläche, gerundet auf zwei Nachkomma-Stellen
        print(f" Raum: {raum_name} mit {flaeche: .2f} qm2.")
    
        # fängt Fehler ab, User soll neu eintippen
    except ValueError:
        print("Bitte gib nur Zahlen (mit Punkt statt Komma) ein! \n")

# For-Schleife, um alle Einträge (Dictionarys) in der raeume-Liste durchzugehen
for raum in raeume: 
    # greife auf den Value (z.B. Wohnzimmer oder 4(Meter)) des Dictionarys zu, mit Zugriff auf Key
    name = raum["name"]
    qm2 = raum["quadratmeter"]

    # Ausgabe des Dictionarys mit jedem Durchlauf in der For-Schleife
    print(f"{name} Quadratmeter: {qm2}")

    # addiert die gespeicherten Einträge zur Gesamtfläche der Wohnung
    gesamtflaeche += qm2


    print(f"Räume: {raum}, Fläche: {qm2}")

print(f"Gesamtfläche: {gesamtflaeche}qm2")


