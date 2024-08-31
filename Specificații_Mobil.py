# Dictionar cubinformatiile desore telefon.
telefon_mobil = {
    "nume": "Samsung Galaxy A55",
    "pret": "1779 lei",
    "specificatii": {
          "tip telefon": "Smartphone",
          "sloturi sim": "Hybrid SIM",
          "tip sim": "Nano SIM",
          "sistem de operare": "Android",
          "conectivitate": ["Bluetooth", "Wi-fi", "GPS", "NFC"],
          "versiune bluetooth": "v5.3",
          "numar nuclee": 8,
          "frecventa procesor": ["2Ghz", "2.7Ghz"],
          "senzori": ["Accelerometru", "Giroscop", "Amprenta", "Senzor de proximitate", "Senzor geomagnetic"],
          "continut pachet": ["Telefon", "Cheie SIM", "Cablu de date USB Type-C"],
          "culoare": "Ice Blue",
          "dimensiuni": "77.4×8.2×161.1mm",
          "greutate": "213 g",
          "SAR": ["Cap 0.684", "Corp 1.037"],
          "an aparitie": 2024,
          "altele": ["Glonass", "Galileo", "Beidou", "QZSS"],
          "tehnologie": ["2G", "4G", "3G", "5G"],
          "ro alert": "Da",
          "dimensiune ecran": "6.6 inch",
          "tip display": "Super AMOLED",
          "rezolutie": "1080×2340",
          "functii display": ["16M adancime de culoare", "Refresh rate 120Hz"],
          "memorie interna": "256 GB",
          "memorie RAM": "8 GB",
          "slot card memorie": "MicroSD",
          "standard wi-fi": "802.11 ax",
          "porturi": "USB Type C",
          "numar camere": 3,
          "rezolutie camera principala": ["12MP Ultrawide", "5MP Macro", "50MP Wide"],
          "rezolutie camera frontala": "32Mpx",
          "rezolutie video": "4k",
          "caracteristici foto video": ["Auto focus", "Slow motion", "Zoom digital"],
          "blit": "Da",
          "capacitate baterie": "5000 mAh",
     }
}



# Afisarea informatiilor folosind f-string
print(f"Telefon mobil: {telefon_mobil['nume']}")
print(f"Pret: {telefon_mobil['pret']}")
print("---")




# Accesam si afisam fiecare specificatie folosind f-string
print(f"Tip telefon: {telefon_mobil['specificatii']['tip telefon']}")
print(f"Sloturi sim: {telefon_mobil['specificatii']['sloturi sim']}")
print(f"Tip sim: {telefon_mobil['specificatii']['tip sim']}")
print(f"Sistem de operare: {telefon_mobil['specificatii']['sistem de operare']}")
print(f"Conectivitate: {','.join(telefon_mobil['specificatii']['conectivitate'])}")
print(f"Versiune bluetooth: {telefon_mobil['specificatii']['versiune bluetooth']}")
print(f"Numar nuclee: {telefon_mobil['specificatii']['numar nuclee']}")
print(f"Frecventa procesor: {','.join(telefon_mobil['specificatii']['frecventa procesor'])}")
print(f"Senzori: {','.join(telefon_mobil['specificatii']['senzori'])}")
print(f"Continut pachet: {','.join(telefon_mobil['specificatii']['continut pachet'])}")
print(f"Culoare: {telefon_mobil['specificatii']['culoare']}")
print(f"Dimensiuni: {telefon_mobil['specificatii']['dimensiuni']}")
print(f"Greutate: {telefon_mobil['specificatii']['greutate']}")
print(f"SAR: {','.join(telefon_mobil['specificatii']['SAR'])}")
print(f"An aparitie: {telefon_mobil['specificatii']['an aparitie']}")
print(f"Altele: {','.join(telefon_mobil['specificatii']['altele'])}")
print(f"Tehnologie: {','.join(telefon_mobil['specificatii']['tehnologie'])}")
print(f"Ro Alert: {telefon_mobil['specificatii']['ro alert']}")
print(f"Dimensiune ecran: {telefon_mobil['specificatii']['dimensiune ecran']}")
print(f"Tip display: {telefon_mobil['specificatii']['tip display']}")
print(f"Rezolutie: {telefon_mobil['specificatii']['rezolutie']}")
print(f"Functii display: {','.join(telefon_mobil['specificatii']['functii display'])}")
print(f"Memorie interna: {telefon_mobil['specificatii']['memorie interna']}")
print(f"Memorie RAM: {telefon_mobil['specificatii']['memorie RAM']}")
print(f"Slot card memorie: {telefon_mobil['specificatii']['slot card memorie']}")
print(f"Standard Wi-fi: {telefon_mobil['specificatii']['standard wi-fi']}")
print(f"Porturi: {telefon_mobil['specificatii']['porturi']}")
print(f"Numar camere: {telefon_mobil['specificatii']['numar camere']}")
print(f"Rezolutie camera principala: {','.join(telefon_mobil['specificatii']['rezolutie camera principala'])}")
print(f"Rezolutie camera frontala: {telefon_mobil['specificatii']['rezolutie camera frontala']}")
print(f"Rezolutie video: {telefon_mobil['specificatii']['rezolutie video']}")
print(f"Caracteristici foto video: {','.join(telefon_mobil['specificatii']['caracteristici foto video'])}")
print(f"Blit: {telefon_mobil['specificatii']['blit']}")
print(f"Capacitate baterie: {telefon_mobil['specificatii']['capacitate baterie']}")