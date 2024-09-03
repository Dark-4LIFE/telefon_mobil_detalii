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




# Funcție pentru a afișa informațiile generale ale telefonului
def afiseaza_informatii_generale(telefon):
    print(f"Telefon mobil: {telefon.get('nume', 'Necunoscut')}")
    print(f"Preț: {telefon.get('pret', 'Necunoscut')}")
    print("---\n")

# Funcție pentru a afișa specificațiile telefonului
def afiseaza_specificatii(specificatii):
    for cheie, valoare in specificatii.items():
        if isinstance(valoare, list):
            print(f"{cheie.capitalize()}: {', '.join(valoare)}")
        else:
            print(f"{cheie.capitalize()}: {valoare}")
    print("---\n")

# Apelarea funcțiilor pentru a afișa informațiile
afiseaza_informatii_generale(telefon_mobil)
afiseaza_specificatii(telefon_mobil["specificatii"])