import dearpygui.dearpygui as dpg

from windows.gen_train import gen_window, train_window

def print_me(sender):
    print(f"Menu Item: {sender}")

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=900, height=700)

def push_gen():
    dpg.delete_item("container", children_only=True)
    gen_window(dpg.group(parent="container"))

def push_model():
    dpg.delete_item("container", children_only=True)
    train_window(dpg.group(parent="container"))


with dpg.window(tag="PW"):
    dpg.add_spacer(height=8)
    with dpg.group(tag="container"):
        pass

dpg.set_primary_window("PW", True)

with dpg.viewport_menu_bar():
    dpg.add_spacer(height=1)
    dpg.add_button(label="Generator", callback=push_gen)
    dpg.add_button(label="Model", callback=push_model)
    dpg.add_button(label="Analysis")
    with dpg.menu(label="About"):
        dpg.add_menu_item(label="Save", callback=print_me)
        dpg.add_menu_item(label="Save As", callback=print_me)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()