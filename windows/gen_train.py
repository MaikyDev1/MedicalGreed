import pandas as pd

import dearpygui.dearpygui as dpg
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

import matplotlib.pyplot as plt

from generator.generator import generate_csv, columns

def new_generate_callback():
    print(f'INFO | Generating a new dataset.csv')
    learn_size = dpg.get_value('learn_cvs_size')
    test_size = dpg.get_value('test_cvs_size')
    df, test_df = generate_csv(learn_size, test_size)
    load_data(df)

def load_data(df):
    if df is None:
        try:
            df = pd.read_csv('dataset-train.csv')
        except:
            new_generate_callback()
            return

    for i in range(0, 5):
        dpg.delete_item(f"preview_item_{i}")
        with dpg.table_row(id=f"preview_item_{i}", parent="preview"):
            dpg.add_text(df.iloc[i, 0])
            dpg.add_text(df.iloc[i, 1])
            dpg.add_text(df.iloc[i, 3])
            dpg.add_text("")
            dpg.add_text(df.iloc[i, 10])
            dpg.add_text(df.iloc[i, 11])
            dpg.add_text(df.iloc[i, 12])
            dpg.add_text(df.iloc[i, 13])
            dpg.add_text(df.iloc[i, 14])
            dpg.add_text(df.iloc[i, 15])

def gen_window(this):
    with this:
        dpg.add_text("This script generates random data, for training and testing.")
        dpg.add_slider_int(label="Learning CSV", tag="learn_cvs_size", default_value=500, min_value=300, max_value=1000)
        dpg.add_slider_int(label="Testing CSV", tag="test_cvs_size", default_value=200, min_value=100, max_value=1000)
        dpg.add_combo(label="Alege un model de date", items=["Medicale"], default_value="Medicale")
        dpg.add_button(label="Generate Data", callback=new_generate_callback)
        dpg.add_spacer(height=10)
        dpg.add_text("----  Current Data Example  ----")
        with dpg.table(tag="preview", header_row=True, row_background=True, resizable=False):
            dpg.add_table_column(label="Sex", width_fixed=True, width=0)
            dpg.add_table_column(label="Nume", width_fixed=True)
            dpg.add_table_column(label="CNP", width_fixed=True)
            dpg.add_table_column(label="...", width_fixed=True, width=0)
            dpg.add_table_column(label="Colesterol", width_fixed=True)
            dpg.add_table_column(label="Job Periculos", width_fixed=True)
            dpg.add_table_column(label="Vacinari", width_fixed=True)
            dpg.add_table_column(label="Adhearance", width_fixed=True)
            dpg.add_table_column(label="Neurolo...", width_fixed=True)
            dpg.add_table_column(label="TRUST", width_fixed=True)
    load_data(None)

model = None
def start_model(this):
    try:
        train_df = pd.read_csv('dataset-train.csv')
        test_df = pd.read_csv('dataset-test.csv')
    except:
        with this:
            dpg.add_text("-- Data is not generated (File dose not exists) --", parent="info_train");
        return
    train_df['TRUST INDEX'].value_counts(normalize=True).plot(kind='bar')
    plt.title("Class Distribution")
    plt.xlabel("Class")
    plt.ylabel("Proportion")
    plt.show()
    label_encoders = {}
    for col in columns:
        le = LabelEncoder()
        train_df[col] = le.fit_transform(train_df[col])
        test_df[col] = le.fit_transform(test_df[col])
        label_encoders[col] = le

    train_df.head()
    train_df.info()
    train_df.describe()


    # Features and labels
    X_train = train_df.drop("TRUST INDEX", axis=1)
    X_test = test_df.drop("TRUST INDEX", axis=1)
    y_train = train_df["TRUST INDEX"]
    y_test = test_df["TRUST INDEX"]

    # Train-test split
    # Train classifier
    global model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    dpg.add_text(f"-- Data was trained -- {model}", parent="info_train")
    dpg.add_group(parent="info_train", tag="put_acuracy")
    with dpg.table(tag="preview", parent="info_train", header_row=True, row_background=True, resizable=False):
        dpg.add_table_column(label="Index", width_fixed=True, width=0)
        dpg.add_table_column(label="Prediction", width_fixed=True, width=0)
        dpg.add_table_column(label="Real", width_fixed=True, width=0)
        dpg.add_table_column(label="Correct", width_fixed=True, width=0)

    y_pred = model.predict(X_test)
    to_print = 10
    wrong_amount = 0
    for i in range(len(y_pred)):
        if y_pred[i] != y_test[i]:
            wrong_amount += 1
        if to_print >= 0:
            with dpg.table_row(id=f"preview_item_{i}", parent="preview"):
                dpg.add_text(f"{i}")
                dpg.add_text(y_pred[i])
                dpg.add_text(y_test[i])
                if y_pred[i] == y_test[i]:
                    dpg.add_text(f"CORRECT")
                else:
                    dpg.add_text(f"WRONG")
                to_print -= 1
    dpg.add_text(f"Model accuracy: {wrong_amount}/{len(y_pred)}", parent="put_acuracy")

def train_window(this):
    with this:
        dpg.add_text("After we are sure that we like our data, lets train a model")
        dpg.add_button(label="Train", callback=start_model)
        with dpg.group(tag="info_train"):
            pass

