raeume = []
gesamtflaeche= 0.0
"""erster Versuch"""

while True:
    raum_name =input("Raumname oder ende: ")
    
    if raum_name.lower() == "ende":
        break

    try:
        laenge = float(input(f"Länge {raum_name}: "))
        breite = float(input(f"Breite {raum_name}: "))

        flaeche = laenge * breite

        raum_daten = {"name" : raum_name, "quadratmeter": flaeche}

        raeume.append(raum_daten)
        print(f" Raum: {raum_name} mit {flaeche: .2f} qm2.")
    
    except ValueError:
        print("Bitte gib nur Zahlen (mit Punkt statt Komma) ein! \n")

for raum in raeume: 
    name = raum["name"]
    qm2 = raum["quadratmeter"]

    print(f"{name} Quadratmeter: {qm2}")

    gesamtflaeche += qm2

print(f"Gesamtfläche: {gesamtflaeche}qm2, Raumbezeichnung: {raum}")


