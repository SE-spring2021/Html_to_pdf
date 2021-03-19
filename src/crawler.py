from bs4 import BeautifulSoup
import requests
import re


class Crawler():
    
    def get_contents(self, url:str):
        return requests.get(url)

    def get_links(self, url:str):
        links = set()
        respons = requests.get(url)
        soup = BeautifulSoup(respons.content, 'html.parser')
        for link in soup.find_all('a', attrs={'href': re.compile("^http(s)*://")}):
            links.add(link.get('href'))
        return links

    def get_links_by_level(self, url, level):
        pass

def main():
    crwl = Crawler()
    links = crwl.get_links("https://www.w3schools.com/java/")
    for link in links:
        print(link)

    

if __name__ == "__main__":
        main()  