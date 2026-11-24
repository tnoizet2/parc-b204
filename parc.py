parc = [
    {"nom": "PC01", "ram": 8, "en_panne": False},
    {"nom": "PC02", "ram": 16, "en_panne": True},
    {"nom": "PC03", "ram": 4, "en_panne": False},
    {"nom": "PC04", "ram": 32, "en_panne": False},
    {"nom": "PC05", "ram": 8, "en_panne": True},
]

def nb_en_panne(parc):
    compteur_panne = 0
    for pc in parc:
        if pc["en_panne"] == True:
            compteur_panne += 1
    return(compteur_panne)

def ram_moyenne(parc):
    for pc in parc:
        ram_total += pc ["ram"]
    moyenne_ram = ram_total / len(parc)
    return(moyenne_ram)