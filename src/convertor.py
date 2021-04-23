import pdfkit
import requests
import random
from bs4 import BeautifulSoup
import os

class Convertor():


    def convertToPdf(self, html:str,url:str):
        abc = True
        try:
            folder = url.replace("/","")
            folder = folder.replace("\\","")
            folder = folder.replace(":","")
            folder = folder.replace(".","")
            fil = "NoTitle"+str(random.randint(0,100))
            reqs = requests.get(html)
            soup = BeautifulSoup(reqs.text, 'html.parser')
            for title in soup.find_all('title'):
                fil = title.get_text()
                break

            fil = fil.replace("/","")
            fil = fil.replace(":","")
            fil = fil.replace("|","")
            config = pdfkit.configuration(wkhtmltopdf= "wkhtmltopdf.exe")
            if not os.path.exists('documents'+'/'+folder):
                os.makedirs('documents'+'/'+folder)
            pdfkit.from_url(html,'\\documents\\'+folder+'/'+fil+'.pdf', configuration=config)
            abc = False
        except Exception as e:
            print(e)
            abc = True
        return abc,fil


def main():
    conv = Convertor()
    conv.convertToPdf("https://www.martinfowler.com/")

if __name__ == "__main__":
        main()
