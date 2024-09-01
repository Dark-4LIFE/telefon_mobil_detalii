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




print(f"Telefon mobil: {telefon_mobil.get('nume', 'N/A')}")
print(f"Pret: {telefon_mobil.get('pret', 'N/A')}")
print("---\n")






print(f"Tip telefon: {telefon_mobil['specificatii'].get('tip telefon', 'N/A')}\n"
      f"Sloturi SIM: {telefon_mobil['specificatii'].get('sloturi sim', 'N/A')}\n"
      f"Tip SIM: {telefon_mobil['specificatii'].get('tip sim', 'N/A')}\n"
      f"Sistem de operare: {telefon_mobil['specificatii'].get('sistem de operare', 'N/A')}\n"
      f"Conectivitate: {','.join(telefon_mobil['specificatii'].get('conectivitate', []))}\n"
      f"Versiune bluetooth: {telefon_mobil['specificatii'].get('versiune bluetooth', 'N/A')}\n"
      f"Numar nuclee: {telefon_mobil['specificatii'].get('numar nuclee', 'N/A')}\n"
      f"Frecventa procesor: {','.join(telefon_mobil['specificatii'].get('frecventa procesor', []))}\n"
      f"Senzori: {','.join(telefon_mobil['specificatii'].get('senzori', []))}\n"
      f"Continut pachet: {','.join(telefon_mobil['specificatii'].get('continut pachet', []))}\n"
      f"Culoare: {telefon_mobil['specificatii'].get('culoare', 'N/A')}\n"
      f"Dimensiuni: {telefon_mobil['specificatii'].get('dimensiuni', 'N/A')}\n"
      f"Greutate: {telefon_mobil['specificatii'].get('greutate', 'N/A')}\n"
      f"SAR: {telefon_mobil['specificatii'].get('SAR', 'N/A')}\n"
      f"An aparitie: {telefon_mobil['specificatii'].get('an aparitie', 'N/A')}\n"
      f"Altele: {','.join(telefon_mobil['specificatii'].get('altele', []))}\n"
      f"Tehnologie: {','.join(telefon_mobil['specificatii'].get('tehnologie', []))}\n"
      f"Ro Alert: {telefon_mobil['specificatii'].get('ro alert', 'N/A')}\n"
      f"Dimensiune ecran: {telefon_mobil['specificatii'].get('dimensiune ecran', 'N/A')}\n"
      f"Tip display: {telefon_mobil['specificatii'].get('tip display', 'N/A')}\n"
      f"Rezolutie: {telefon_mobil['specificatii'].get('rezolutie', 'N/A')}\n"
      f"Functii display: {','.join(telefon_mobil['specificatii'].get('functii display', []))}\n"
      f"Memorie interna: {telefon_mobil['specificatii'].get('memorie interna', 'N/A')}\n"
      f"Memorie RAM: {telefon_mobil['specificatii'].get('memorie RAM', 'N/A')}\n"
      f"Slot card memorie: {telefon_mobil['specificatii'].get('slot card memorie', 'N/A')}\n"
      f"Standard Wi-fi: {telefon_mobil['specificatii'].get('standard wi-fi', 'N/A')}\n"
      f"Porturi: {telefon_mobil['specificatii'].get('porturi', 'N/A')}\n"
      f"Numar camere: {telefon_mobil['specificatii'].get('numar camere', 'N/A')}\n"
      f"Rezolutie camera principala: {','.join(telefon_mobil['specificatii'].get('rezolutie camera principala', []))}\n"
      f"Rezolutie camera frontala: {telefon_mobil['specificatii'].get('rezolutie camera frontala', 'N/A')}\n"
      f"Rezolutie video: {telefon_mobil['specificatii'].get('rezolutie video', 'N/A')}\n"
      f"Caracteristici foto video: {','.join(telefon_mobil['specificatii'].get('caracteristici foto video', []))}\n"
      f"Blit: {telefon_mobil['specificatii'].get('blit', 'N/A')}\n"
      f"Capacitate baterie: {telefon_mobil['specificatii'].get('capacitate baterie', 'N/A')}\n")
