
import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from crawler import Crawler
from helper import Helper
from convertor import Convertor
from pageService import PageService

class ContainerGrid(GridLayout):
    digLevel = ObjectProperty(None)
    baseUrl = ObjectProperty(None)
    txtResults = ObjectProperty(None)
    chbSameDomain = ObjectProperty(None)
    crwl : Crawler
    Conve = Convertor()
    
    def callback(self, instance):
        pdfDict={}
        self.crwl = Crawler(self.baseUrl.text, self.chbSameDomain.active)
        result = "Links:\n"
        rootPage = self.crwl.download_pages(int(self.digLevel.text))
        print(rootPage)
        for page in rootPage.links:
            check,title = self.Conve.convertToPdf(str(page),self.baseUrl.text)
            pdfDict[str(page)]=title
        check,title = self.Conve.convertToPdf(str(rootPage.url),self.baseUrl.text)
        pdfDict[str(rootPage.url)]=title
        # print(pdfDict)
        pageServiceHelper=PageService(self.baseUrl.text,pdfDict)

        
        self.txtResults.text = "Downloaded Pages:\n\n" + Helper.printPagesTitles(rootPage)
        


class AppGui(App):
    def build(self):
        Window.size = (600,500)
        self.title = "HTML To PDF Converter"
        container = ContainerGrid()
        return container
        # return Button(text='Hello World',)

AppGui().run()