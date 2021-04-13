from bs4 import BeautifulSoup
import requests
import re

class HtmlModel():
    def __init__(self,level, url):

        self.id = ""
        self.title = ""
        self.level = level
        self.url = url
        self.htmlContent = ""
        self.styles = ""
        self.links = set()
        self.children = set()
        self.__getcontent__()

    def __getcontent__(self):
        respons = requests.get(self.url)
        soup = BeautifulSoup(respons.content, 'html.parser')
        for link in soup.find_all('a', attrs={'href': re.compile("^http(s)?://")}):
            self.links.add(link.get('href'))
        print(self.url)