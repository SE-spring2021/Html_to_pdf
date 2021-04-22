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
        self.styles = set()
        self.links = set()
        self.children = set()
        self.__getcontent__()

    def __getcontent__(self):
        try:
            respons = requests.get(self.url)
            soup = BeautifulSoup(respons.content, 'html.parser')
            if soup.title:
                self.title = soup.title.text
            # self.styles = soup("style")
            # self.htmlContent = soup("html")
            for link in soup.find_all('a', attrs={'href': re.compile("^http(s)?://")}):
                self.links.add(link.get('href'))
        except:
            pass
        print(self.url)