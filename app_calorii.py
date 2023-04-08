


print("Bun venit la calculatorul de calorii zilnice!")
sex = input("Introduceti sexul (M/F): ")
varsta = int(input("Introduceti varsta: "))
inaltime = float(input("Introduceti inaltimea (cm): "))
greutate = float(input("Introduceti greutatea (kg): "))


# Lista de alimente și valorile calorice
alimente = {
    "avocado": 160,
    "banane": 89,
    "broccoli": 34,
    "cartofi": 86,
    "cereale integrale": 350,
    "ciocolata neagra": 174,
    "fasole": 333,
    "grapefruit": 42,
    "iaurt": 60,
    "lapte": 58,
    "mar": 52,
    "morcovi": 41,
    "nuci": 550,
    "ovaz": 389,
    "paine": 250,
    "pepene verde": 30,
    "porumb dulce": 86,
    "pui": 165, 
    "ridichi": 16, 
    "rosii": 18, 
    "sfecla rosie": 43, 
    "somon": 206, 
    "spanac": 23, 
    "tofu": 76, 
    "ulei de masline": 884, 
    "usturoi": 149, 
    "vin": 85,
    "somon": 127               
}


# Functia pentru calcularea valorii calorice pentru un aliment
def calculeaza_calorii(aliment, cantitate):
    if aliment in alimente:
        calorii = alimente[aliment] * cantitate / 100
        return calorii
    else:
        return None

# Functia pentru calcularea valorii calorice pentru o lista de alimente
def calculeaza_total_calorii(lista_alimente):
    total_calorii = 0
    for aliment, cantitate in lista_alimente:
        calorii = calculeaza_calorii(aliment, cantitate)
        if calorii:
            total_calorii += calorii
    return total_calorii

# Solicita alimentele și cantitățile utilizatorului și afișează totalul de calorii
lista_alimente = []
while True:
    aliment = input("Introduceți un aliment sau apăsați ENTER pentru a finaliza: ")
    if not aliment:
        break
    cantitate = float(input("Introduceți cantitatea în grame: "))
    lista_alimente.append((aliment, cantitate))

total_calorii = calculeaza_total_calorii(lista_alimente)
print("Total calorii:", total_calorii)
