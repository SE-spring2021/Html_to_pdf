import pdfrw
import os

class PageService():

    def __init__(self,baseUrl):
        self.baseUrl=baseUrl
        self.translateLinks()
  
    def translateLinks(self):
        checkUrl=self.baseUrl.replace("/","")
        checkUrl=checkUrl.replace(":","")
        print(checkUrl)

        dataDir="..\\output\\"
        pdfList=os.listdir(dataDir)
        print(pdfList)

        pdf = pdfrw.PdfReader(dataDir+checkUrl+".pdf")
        new_pdf = pdfrw.PdfWriter()

        for page in pdf.pages: 
            for annot in page.Annots or []:
                old_url = annot.A.URI
                
                checkOldUrl=old_url.replace("/","")
                checkOldUrl=checkOldUrl.replace(":","")
                checkOldUrl=checkOldUrl.replace("(","")
                checkOldUrl=checkOldUrl.replace(")","")
                checkOldUrl=checkOldUrl.replace("httpwww.","")
                print(checkOldUrl)
                if(checkOldUrl+".pdf" in pdfList):
                    print("Inside")
                    print(checkOldUrl+".pdf")
                    
                    outUrl="("+checkOldUrl+".pdf)"
                    new_url = pdfrw.objects.pdfstring.PdfString("(gsu.pdf)")
                    annot.A.URI = new_url

            new_pdf.addpage(page)    

        new_pdf.write(dataDir+checkUrl+".pdf")
        
if __name__=="__main__":
    pageServiceHelper=PageService("http://tinman.cs.gsu.edu/~raj/")
