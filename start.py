import dearpygui.dearpygui as dpg

from windows.analyze import analyze_gui
from windows.gen_train import gen_window, train_window

model = None

def get_model():
    global model
    return model

def set_model(m):
    global model
    model = m

dpg.create_context()
dpg.create_viewport(title='proiect', width=900, height=500)

def push_gen():
    dpg.delete_item("container", children_only=True)
    gen_window(dpg.group(parent="container"))

def push_model():
    dpg.delete_item("container", children_only=True)
    train_window(dpg.group(parent="container"))

def push_analysis():
    dpg.delete_item("container", children_only=True)
    analyze_gui(dpg.group(parent="container"))

with dpg.window(tag="PW"):
    dpg.add_spacer(height=8)
    with dpg.group(tag="container"):
        pass

dpg.set_primary_window("PW", True)

with dpg.viewport_menu_bar():
    dpg.add_spacer(height=1)
    dpg.add_button(label="Generator", callback=push_gen)
    dpg.add_button(label="Model", callback=push_model)
    dpg.add_button(label="Analysis", callback=push_analysis)
    with dpg.menu(label="About"):
        dpg.add_menu_item(label="Save")
        dpg.add_menu_item(label="Save As")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()