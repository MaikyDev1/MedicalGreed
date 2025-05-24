import webbrowser
import pandas as pd
from windows.analyze import *

import dearpygui.dearpygui as dpg
from generator import generator
from windows.gen_train import gen_window

dpg.create_context()

def callback(sender, app_data):
    print('OK was clicked.')
    print("Sender: ", sender)
    print("App Data: ", app_data)



def open_github_url(sender, data):
    webbrowser.open("https://www.google.com")

dpg.add_file_dialog(
    directory_selector=True, show=False, callback=callback, tag="file_dialog_id", width=700 ,height=400)

analyze_gui(dpg)

gen_window()

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

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

dpg.destroy_context()