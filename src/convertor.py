import pdfkit
import requests
import random
from bs4 import BeautifulSoup

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
            config = pdfkit.configuration(wkhtmltopdf="wkhtmltopdf.exe")
            pdfkit.from_url(html,'documents'+'/'+fil+'.pdf', configuration=config)
            abc = False
        except Exception as e:
            print('error')
            abc = True
        return abc