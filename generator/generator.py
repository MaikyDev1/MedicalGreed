import random
import pandas as pd
from configs.generator_parameters import *

# Lets do magic with some random values

def generate_csv(learn_size, test_size):
    data_frame = pd.DataFrame(
        columns=["Sex", "Nume", "Prenume", "CNP", "An", "Luna", "Zi", "Judet", "Oras", "Nationalitate",
                 "Boli", "Fumator", "Vacinari", "Asigurat", "Job Periculos", "Statut Social", "Credite",
                 "Asistat-Social", "Educatie", "TRUST-INDEX"])

    for i in range(learn_size + test_size):
        gen = random.choice(["M", "F"])
        cnp = []
        # Let's make a random birthdate
        nastere = {
            "an": random.randint(1950, 2024),
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
            "Boli": boala,
            "Vacinari": random.choices(["COMPLET", "PARTIAL", "NU"], weights=[70, 20, 10], k=1)[0],
            "Asigurat": random.choices(["CNAS", "NU"], weights=[70, 20], k=1)[0],
            "Job Periculos": random.choices(["DA", "MEDIU", "NU"], weights=[20, 30, 50], k=1)[0]
        }
        data_frame = pd.concat([data_frame, pd.DataFrame([rand])], ignore_index=True)

    # Conversie la DataFrame

    data_frame.to_csv("dataset.csv", index=False, encoding='utf-8')