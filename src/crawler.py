import re
import threading

from models.htmlModel import HtmlModel
from helper import Helper



class Crawler():

    def __init__(self,baseUrl, sameDomain=True):
        self.rootPage = HtmlModel(0,baseUrl)
        self.domain = Helper.getDomain(baseUrl)
        self.sameDomain = sameDomain
        self.links_visited = set()

    def download_pages(self, level:int):
        pages = set()
        pages.add(self.rootPage)

        threads = set()
        while pages:
            page = pages.pop()

            for link in page.links:
                if(self.valid_link(link)):
                    linkPage = HtmlModel(page.level+1,link)
                    page.children.add(linkPage)
                    # th = threading.Thread(target=HtmlModel, args=(htmlPage.level+1, link))
                    # threads.add(th)
                    # th.start()
                    # links_visited.add(link)
                    if(linkPage.level<level):
                        pages.add(linkPage)

                else:
                    pass
                    # print(link)
            # for th in threads:
            #     th.join()
                # print(th.name)
            # print(self.rootPage)
        return self.rootPage

    def valid_link(self, link:str):
        if(link in self.links_visited):
            return False
        self.links_visited.add(link)
        if(self.sameDomain):
            return bool(re.match("^http(s)?:\/\/\w*.*({}){{1}}".format(self.domain), link))
        return True

        

def main():
    # crwl = Crawler("https://www.google.com")
    # crwl = Crawler("https://andersonsunflowers.com")
    # crwl = Crawler("https://www.shanelynn.ie/")
    pages = crwl.download_pages(2)
    with open("CrawledHTML.html", "w") as f:
            f.write(str(pages.htmlContent))

if __name__ == "__main__":
        main()  