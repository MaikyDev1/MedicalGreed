import random
import pandas as pd
from configs.generator_parameters import *

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Lets do magic with some random values
columns=["Sex", "Nume", "Prenume", "CNP", "Nastere", "Judet", "Localitate", "Nationalitate",
                 "Diabet", "Fumator", "Colesterol", "Job Periculos", "Vacinari", "Aderenta La Tratament",
                 "Neurological Status", "TRUST INDEX"]
def generate_csv(learn_size, test_size):
    data_frame = pd.DataFrame(
        columns=columns)

    for i in range(learn_size + test_size):
        TRUST = 500
        gen = random.choice(["M", "F"])
        cnp = []
        # Let's make a random birthdate
        nastere = {
            "an": random.randint(1950, 2024),
            "luna": random.randint(1, 12),
            "zi": random.randint(1, 30),
        }
        TRUST -= age_trust(nastere["an"])
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
        # Lets generate one or two names for our fictive person.
        prenume = random.choice(prenume_masculin if judet == "M" else prenume_feminin)
        second_prenume = random.choice(prenume_masculin if judet == "M" else prenume_feminin)
        if random.random() <= 0.1:
            prenume = f"{prenume}-{second_prenume}"
        # BOALA GENERATOR
        boala = "NIMIC"
        if random.random() <= 0.2:
            chosen = random.randint(0, len(boli["names"]) - 1)
            boala = boli["names"][chosen]
            TRUST -= boli["bad_level"][chosen]
        # NEURO PROBLEMS
        neuro = 00000
        if random.random() <= 0.1:
            chosen = random.randint(0, len(neurological_problems["codes"]) - 1)
            neuro = neurological_problems["codes"][chosen]
            TRUST -= neurological_problems["bad_level"][chosen] * 2
        # DIABET
        diabet = random.choices(["DA", "NU"], weights=[35, 65], k=1)[0]
        if diabet == "DA":
            TRUST -= 60
        # JOBS
        job = random.choices(["DA", "NU"], weights=[30, 70], k=1)[0]
        if job == "DA":
            TRUST -= 46
        # VACCINE
        vaccine = random.choices(list(range(11)), weights=[1, 1, 1, 1, 1, 1, 7, 5, 2, 2, 1], k=1)[0]
        TRUST -= 80 - (vaccine * 10)
        # JOBS
        smoker = random.choices(["DA", "NU"])[0]
        if smoker == "DA":
            TRUST -= 50
        # CHOLESTEROL
        cholesterol = random.randint(150, 240)
        TRUST -= cholesterol_trust(gen, nastere["an"], cholesterol)
        # Aderenta la tratament
        tratament = 0 + (random.random() * ((2025 - nastere["an"]) / 10)/10)

        rand = {
            "Sex": gen,
            "Nume": random.choice(nume_de_familie),
            "Prenume": prenume,
            "CNP": "".join(cnp),
            "Nastere": f'{nastere["an"]}/{nastere["luna"]}/{nastere["zi"]}',
            "Judet": judet,
            "Localitate": oras,
            "Nationalitate": random.choices(["Romana", "Maghiara", "Roma"], weights=[84, 9, 7], k=1)[0],
            "Diabet": diabet,
            "Fumator": smoker,
            "Colesterol": cholesterol,
            "Job Periculos": job,
            "Vacinari": vaccine,
            "Aderenta La Tratament": tratament,
            "Neurological Status": neuro,
            "TRUST INDEX": trust_convert(TRUST),
        }
        data_frame = pd.concat([data_frame, pd.DataFrame([rand])], ignore_index=True)

    # Conversie la DataFrame
    train_df = data_frame.iloc[:learn_size]
    test_df = data_frame.iloc[learn_size:learn_size + test_size]
    train_df.to_csv("dataset-train.csv", index=False, encoding='utf-8')
    test_df.to_csv("dataset-test.csv", index=False, encoding='utf-8')
    return train_df, test_df

def cholesterol_trust(sex, year, cholesterol):
    age = 2025 - year
    if age <= 19:
        if cholesterol < 200:
            return 1
        else:
            return 40
    if age > 19:
        if cholesterol < 200:
            return 4
        else:
            return 60

def age_trust(year):
    age = 2025 - year
    if age < 13:
        return 25
    if age >= 13 & age <= 32:
        return 10
    if age < 50:
        return 30
    if age < 70:
        return 60
    if age > 70:
        return 100
    return 0

def trust_convert(trust):
    if trust <= 320:
        return "LOW"
    if trust <= 450:
        return "MEDIUM"
    return "HIGH"

# df = pd.read_csv("dataset-train.csv")
#
# label_encoders = {}
# for col in columns:
#     le = LabelEncoder()
#     df[col] = le.fit_transform(df[col])
#     label_encoders[col] = le
#
# # Features and labels
# X = df.drop("TRUST INDEX", axis=1)
# y = df["TRUST INDEX"]
#
# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
#
# # Train classifier
# model = RandomForestClassifier()
# model.fit(X_train, y_train)
#
# # Evaluate
# y_pred = model.predict(X_test)
# print(classification_report(y_test, y_pred, target_names=label_encoders["TRUST INDEX"].classes_))
# print(y_test)
# print(y_pred)