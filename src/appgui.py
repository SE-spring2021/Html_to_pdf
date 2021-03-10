
import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from kivy.uix.widget import Widget


class ContainerGrid(GridLayout):
    pass


class AppGui(App):
    def build(self):
        Window.size = (600,250)
        container = ContainerGrid()
        return container
        # return Button(text='Hello World',)

AppGui().run()