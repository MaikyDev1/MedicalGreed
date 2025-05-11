import random
import pandas as pd

# Lets do magic with some random values

prenume_masculin = [
    "Andrei", "Ion", "Alexandru", "George", "Stefan", "Vlad", "Mihai", "Radu",
    "Florin", "Dan", "Sorin", "Tudor", "Cristian", "Paul", "Iulian", "Bogdan", "Valentin"
    "Ciprian", "Dorian", "Nikolas", "Silviu", "Bogdan", "Dragos", "Laurentiu", "Narcis",
    "Madalin", "Catalin", "Razvan", "Cosmin", "Rares", "Robert", "Ruben"
]

prenume_feminin = [
    "Maria", "Elena", "Ana", "Ioana", "Gabriela", "Cristina", "Roxana", "Laura",
    "Diana", "Bianca", "Alina", "Daniela", "Irina", "Simona", "Alexandra", "Anca",
    "Georgiana", "Denisa", "Corina", "Selena", "Catalina", "Anda", "Florentina", "Julia",
    "Carla", "Teodora", "Miruna", "Narcisa", "Oana", "Paula", "Raisa", "Simina", "Tania",
    "Violeta", "Iustina", "Carmen", "Andreea", "Diana", "Olga", "Viorica"
]

nume_de_familie = [
    "Popescu", "Ionescu", "Stan", "Dumitrescu", "Georgescu", "Marin", "Voicu",
    "Munteanu", "Petrescu", "Toma", "Stoica", "Preda", "Enache", "Matei", "Dragomir",
    "Lupu", "Barbu", "Ilie", "Neagu", "Avram", "Eminescu", "Stanciu", "Pop", "Antonecu"
    "Basescu", "Ciolacu", "Sadoveanu", "Ardeleanu", "Ciubota", "Bordura", "Budeanu",
    "Calin", "Coman", "Dancila", "Salam", "Vionea", "Bucur", "Nistor", "Acatrinei",
    "Nicusor"
]

boli_naspa = [
    "Obezitate", "Anemie", "Depresie", "Meningita", "Otita", "Ciuma", "Ulcer", "Diaree",
    "Hipertenisune", "Endometrioza", "HIV", "HPV", "Rujeola", "Variola", "TBC", "Holera",
    "ASTM", "Diabet", "Hepatita", "Insuficienta Cardiaca", "Bronsita", "Ciroza"
]

boli_ok = [
    "Raceala", "Gripa", "COVID", "Picior-Rupt"
]

locatii = {
    "vrancea": {
        "cod": "39",
        "orase": [
            "Panciu", "Focsani", "Cotesti", "Vidra", "Adjud", "Manastirestii", "Petresti"
        ],
        "sanse": [
            10, 50, 5, 10, 10, 5, 10
        ]
    },
    "Iasi": {
        "cod": "22",
        "orase": [
            "Socola", "Clopotari", "Iasi", "Pascani"
        ],
        "sanse": [
            10, 10, 65, 15
        ]
    },
    "Neamt": {
        "cod": "27",
        "orase": [
            "Bicaz", "Piatra-Neamt", "Roznov"
        ],
        "sanse": [
            10, 80,10
        ]
    },
    "Gorj": {
        "cod": "18",
        "orase": [
            "Motru", "Tg. Jiu", "Stejari"
        ],
        "sanse": [
            10, 70, 20
        ]
    },
    "Buzau": {
        "cod": "10",
        "orase": [
            "Focsanei", "Rm. Sarat", "Buzau", "Beceni", "Patarlagele"
        ],
        "sanse": [
            5, 25, 50, 10, 10
        ]
    },
    "Maramures": {
        "cod": "24",
        "orase": [
            "Sigetul-Marmatiei", "Ulmeni"
        ],
        "sanse": [
            70, 30
        ]
    },
    "Constanta": {
        "cod": "13",
        "orase": [
            "Murfatlar", "Mamaia", "Navodari", "Constanta", "Costinesti", "Mangalia"
        ],
        "sanse": [
            10, 10, 10, 50, 10, 10
        ]
    },
    "Satu Mare": {
        "cod": "30",
        "orase": [
            "Tasnad", "Livada", "Satu Mare"
        ],
        "sanse": [
            10, 10, 80
        ]
    },
    "Bihor": {
        "cod": "05",
        "orase": [
            "Beius", "Oradea"
        ],
        "sanse": [
            10, 90
        ]
    },
    "Ilfov": {
        "cod": "23",
        "orase": [
            "Popesti-Leordeni", "Chiajna", "Jilava", "Pantelimon", "Berceni", "Afumati"
        ],
        "sanse": [
            10, 15, 5, 30, 20, 20
        ]
    },
    "Bucuresti": {
        "cod": "40",
        "orase": [
            "Bucuresti"
        ],
        "sanse": [
            100
        ]
    }
}

def generate_csv(learn_size, test_size):
    data_frame = pd.DataFrame(
        columns=["Sex", "Nume", "Prenume", "CNP", "An", "Luna", "Zi", "Judet", "Oras", "Nationalitate", "Asigurat",
                 "Boli", "Vacinari", "Job Periculos"])

    nume_generate = []
    for i in range(learn_size + test_size):
        gen = random.choice(["M", "F"])
        cnp = []
        # Let's make a random birthdate
        nastere = {
            "an": random.randint(1940, 2024),
            "luna": random.randint(1, 12),
            "zi": random.randint(1, 30),
        }
        # Let's get a random city with a judet.
        judet = random.choice(list(locatii.keys()))
        oras = random.choices(locatii[judet]["orase"], weights=locatii[judet]["sanse"], k=1)[0]
        # now get a random name and make the cnp, this is sex oriented
        if nastere["an"] >= 2000:
            cnp.append("6" if gen == "M" else "5")
        else:
            cnp.append("1" if gen == "M" else "2")
        cnp.append(f"{nastere['an'] % 100:02d}")
        cnp.append(f"{nastere['luna']:02d}")
        cnp.append(f"{nastere['zi']:02d}")
        cnp.append(locatii[judet]["cod"])
        cnp.append(f"{random.randint(1342, 9999)}")
        prenume = random.choice(prenume_masculin if judet == "M" else prenume_feminin)
        second_prenume = random.choice(prenume_masculin if judet == "M" else prenume_feminin)
        if random.random() <= 0.1:
            prenume = f"{prenume}-{second_prenume}"
        boala = "NIMIC"
        if random.random() <= 0.1:
            boala = random.choice(boli_naspa)
        elif random.random() <= 0.3:
            boala = random.choice(boli_ok)
        rand = {
            "Sex": gen,
            "Nume": random.choice(nume_de_familie),
            "Prenume": prenume,
            "CNP": "".join(cnp),
            "An": nastere["an"],
            "Luna": nastere["luna"],
            "Zi": nastere["zi"],
            "Judet": judet,
            "Oras": oras,
            "Nationalitate": random.choices(["Romana", "Maghiara", "Roma"], weights=[84, 9, 7], k=1)[0],
            "Asigurat": random.choices(["CNAS", "Privata", "NU"], weights=[70, 20, 10], k=1)[0],
            "Boli": boala,
            "Vacinari": random.choices(["COMPLET", "PARTIAL", "NU"], weights=[70, 20, 10], k=1)[0],
            "Job Periculos": random.choices(["DA", "MEDIU", "NU"], weights=[20, 30, 50], k=1)[0]
        }
        data_frame = pd.concat([data_frame, pd.DataFrame([rand])], ignore_index=True)

    # Conversie la DataFrame

    data_frame.to_csv("dataset.csv", index=False, encoding='utf-8')