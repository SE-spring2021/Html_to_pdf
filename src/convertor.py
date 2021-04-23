import pdfkit
import requests
import random
from bs4 import BeautifulSoup
import os

CWD =  os.getcwd()

class Convertor():


    def convertToPdf(self, html:str):
        abc = True
        try:
   
            fil = "NoTitle"+str(random.randint(0,100))
            # making requests instance
            reqs = requests.get(html)
            # using the BeaitifulSoup module
            soup = BeautifulSoup(reqs.text, 'html.parser')
            for title in soup.find_all('title'):
                fil = title.get_text()
                break
            config = pdfkit.configuration(wkhtmltopdf= CWD + "\\src\\wkhtmltopdf.exe")
            pdfkit.from_url(html,CWD+'\\documents\\'+fil+'.pdf', configuration=config)
            abc = False
        except Exception as e:
            print('error')
            abc = True
        return abc

def main():
    conv = Convertor()
    conv.convertToPdf("https://www.martinfowler.com/")

if __name__ == "__main__":
        main()