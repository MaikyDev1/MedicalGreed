import pandas as pd

from generator import generator
import dearpygui.dearpygui as dpg

def new_generate_callback():
    print(f'INFO | Generating a new dataset.csv')
    learn_size = dpg.get_value('learn_cvs_size')
    test_size = dpg.get_value('test_cvs_size')
    df, test_df = generator.generate_csv(learn_size, test_size)
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
            dpg.add_text(df.iloc[i, 2])
            dpg.add_text(df.iloc[i, 3])
            dpg.add_text(df.iloc[i, 4])
            dpg.add_text("")
            dpg.add_text(df.iloc[i, 7])
            dpg.add_text(df.iloc[i, 8])
            dpg.add_text(df.iloc[i, 10])
            dpg.add_text(df.iloc[i, 11])
            dpg.add_text(df.iloc[i, 12])

def gen_window():
    with dpg.window(label="Generate Random Data", width=800, height=300, no_resize=True, no_close=True, no_move=True):
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
            dpg.add_table_column(label="Prenume", width_fixed=True)
            dpg.add_table_column(label="CNP", width_fixed=True)
            dpg.add_table_column(label="An", width_fixed=True, width=0)
            dpg.add_table_column(label="...", width_fixed=True, width=0)
            dpg.add_table_column(label="Judet", width_fixed=True)
            dpg.add_table_column(label="Oras", width_fixed=True)
            dpg.add_table_column(label="Asigurat", width_fixed=True)
            dpg.add_table_column(label="Boli", width_fixed=True)
            dpg.add_table_column(label="Vacinari", width_fixed=True)
    load_data(None)

