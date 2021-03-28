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
        links = set()
        links_visited = set()
        links.add(url)
        index = 0
        while len(links) > 0 and index < level:
            url = links.pop()
            links.update(self.get_links(url))
            links_visited.add(url)
            # index += 1

        return links_visited
        

def main():
    crwl = Crawler()
    crwl.get_links_by_level("https://www.google.com",2)
    # links = crwl.get_links("https://www.w3schools.com/java/")
    # for link in links:
    #     print(link)

if __name__ == "__main__":
        main()  