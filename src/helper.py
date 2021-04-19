from models.htmlModel import HtmlModel
import re


class Helper():

    @staticmethod
    def printPagesTitles(root:HtmlModel):
        result=""
        pages = set()
        pages.add(root)
        while pages:
            page = pages.pop()
            result += page.title+"\t("+ page.url +")" + "\n"
            for p in page.children:
                pages.add(p)
        return result
    
    # TODO: it needs to cover all root domain
    @staticmethod
    def getDomain(url):    
        parts = re.split("\/", url)
        match = re.match("([\w\-]+\.)*([\w\-]+\.\w{2,6}$)", parts[2]) 
        if match != None:
            if re.search("\.uk", parts[2]):
                match = re.match("([\w\-]+\.)*([\w\-]+\.[\w\-]+\.\w{2,6}$)", parts[2])
            return match.group(2)
        else: return '' 