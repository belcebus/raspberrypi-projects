from cgitb import text
import kivy

kivy.require("2.1.0")

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text="Hola Mundo!")


if __name__ == "__main__":
    MyApp().run()
