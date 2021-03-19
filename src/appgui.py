
import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from crawler import Crawler



class ContainerGrid(GridLayout):
    digLevel = ObjectProperty(None)
    baseUrl = ObjectProperty(None)
    txtResults = ObjectProperty(None)
    crwl = Crawler()
    
    def callback(self, instance):
        result = "Links:\n"
        links = self.crwl.get_links(self.baseUrl.text)
        for link in links:
            result+=link+"\n"

        self.txtResults.text = result
        


class AppGui(App):
    def build(self):
        Window.size = (600,500)
        container = ContainerGrid()
        return container
        # return Button(text='Hello World',)

AppGui().run()