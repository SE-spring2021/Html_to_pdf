from bs4 import BeautifulSoup
import requests
import re


class Crawler():
    
    def get_contents(self, url:str):
        return requests.get(url)


def main():
    print("Hello World!")
    crwl = Crawler()
    respons = crwl.get_contents("https://www.w3schools.com/java/")

    soup = BeautifulSoup(respons.content, 'html.parser')

    for link in soup.find_all('a', attrs={'href': re.compile("^http(s)*://")}):
        print(link.get('href'))

    

if __name__ == "__main__":
        main()  