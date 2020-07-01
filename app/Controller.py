from tkinter import *

from data.Model import Model
from UI.FrameFormulario import FrameFormulario
from UI.MenuBar import MenuBar


class Controller:

    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.view = FrameFormulario(self, self.root)
        self.menu = MenuBar(self.root, self)

        self.user_id = self.view.id_variable.get()
        self.name = self.view.nombre_variable.get()
        self.last_name = self.view.apellido_variable.get()
        self.password = self.view.password_variable.get()

        self.root.config(menu=self.menu)
        self.root.mainloop()

    def clean_form(self):
        self.view.id_variable.set("")
        self.view.nombre_variable.set("")
        self.view.apellido_variable.set("")
        self.view.password_variable.set("")

    def show_item(self, user_id):
        user = self.model.read_item(user_id)
        for dato in user:
            self.view.nombre_variable.set(dato[1])
            self.view.apellido_variable.set(dato[2])
            self.view.password_variable.set(dato[3])

    def insert_item(self, name, last_name, password, comments=None):
        self.model.create_item(name, last_name, password, comments)
        self.clean_form()

    def update_item(self, user_id, name, last_name, password, comments=None):
        self.model.update_item(user_id, name, last_name, password, comments)
        self.clean_form()

    def delete_item(self, user_id):
        self.model.delete_item(user_id)
        self.clean_form()
