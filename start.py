import webbrowser
import pandas as pd
import dearpygui.dearpygui as dpg

from generator import generator

dpg.create_context()

def callback(sender, app_data):
    print('OK was clicked.')
    print("Sender: ", sender)
    print("App Data: ", app_data)

def new_generate_callback(sender, app_data):
    print('INFO | Generating a new dataset.csv')
    learn_size = dpg.get_value('learn_cvs_size')
    test_size = dpg.get_value('test_cvs_size')
    generator.generate_csv(learn_size, test_size)

def open_github_url(sender, data):
    webbrowser.open("https://www.google.com")

dpg.add_file_dialog(
    directory_selector=True, show=False, callback=callback, tag="file_dialog_id", width=700 ,height=400)

df = pd.read_csv("dataset.csv")

with dpg.window(label="Generate Random Data", width=800, height=300, no_resize=True, no_close=True, no_move=True):
    dpg.add_text("This script generates random data, for training and testing.")
    dpg.add_slider_int(label="Learning CSV", tag="learn_cvs_size", default_value=500, min_value=300, max_value=1000)
    dpg.add_slider_int(label="Testing CSV", tag="test_cvs_size", default_value=200, min_value=100, max_value=1000)
    dpg.add_combo(label="Alege un model de date", items=["Medicale"], default_value="Medicale")
    dpg.add_button(label="Generate Data", callback=new_generate_callback)
    dpg.add_spacer(height=10)
    dpg.add_text("----  Current Data Example  ----")
    with dpg.table(header_row=True, row_background=True, resizable=False):
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
        for i in range(0, 5):
            with dpg.table_row():
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

with dpg.viewport_menu_bar():
    with dpg.menu(label="Themes"):
        dpg.add_menu_item(label="Dark")
        dpg.add_menu_item(label="Light")
        dpg.add_menu_item(label="Classic")
    with dpg.menu(label="Themes"):
        dpg.add_menu_item(label="Dark")
        dpg.add_menu_item(label="Light")
        dpg.add_menu_item(label="Classic")
    with dpg.menu(label="GitHub"):
        dpg.add_button(label="Go to my GitHub", callback=open_github_url)
dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()