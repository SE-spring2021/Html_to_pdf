import pdfrw
import os

class PageService():

    def __init__(self,baseUrl,pdfDict):
        self.baseUrl=baseUrl
        self.pdfDict=pdfDict
        self.translateBasePDF()
  
    def translateBasePDF(self):
        try:
<<<<<<< Updated upstream
=======
            print("Inside Page Service")
>>>>>>> Stashed changes
            dataDir="documents\\"
            pdfList=os.listdir(dataDir+self.pdfDict[self.baseUrl])
            print(pdfList)

            pdf = pdfrw.PdfReader(dataDir+self.pdfDict[self.baseUrl]+".pdf")
            new_pdf = pdfrw.PdfWriter()

            for page in pdf.pages: 
                for annot in page.Annots or []:
                    old_url = annot.A.URI
                    old_url=old_url.replace("(","")
                    old_url=old_url.replace(")","")
                    if(self.pdfDict[old_url]+".pdf" in pdfList):
                        outUrl="("+self.pdfDict[old_url]+".pdf)"
                        new_url = pdfrw.objects.pdfstring.PdfString("("+self.pdfDict[old_url]+")")
                        annot.A.URI = new_url

                new_pdf.addpage(page)    

            new_pdf.write(dataDir+self.pdfDict[self.baseUrl]+".pdf")
            if(self.translatePDFs(dataDir,pdfList)):
                return True
            else:
                return False
        except Exception as ex:
            print(ex)
            pass

    def translatePDFs(self,dataDir,pdfList):
        try:
            for url,title in self.pdfDict.items():
                if(title!=self.pdfDict[self.baseUrl] and title in pdfList):
                    pdf = pdfrw.PdfReader(dataDir+title+".pdf")
                    new_pdf = pdfrw.PdfWriter()

                    for page in pdf.pages: 
                        for annot in page.Annots or []:
                            old_url = annot.A.URI
                            old_url=old_url.replace("(","")
                            old_url=old_url.replace(")","")
                            if(self.pdfDict[old_url]+".pdf" in pdfList):
                                outUrl="("+self.pdfDict[old_url]+".pdf)"
                                new_url = pdfrw.objects.pdfstring.PdfString("("+self.pdfDict[old_url]+")")
                                annot.A.URI = new_url

                        new_pdf.addpage(page)    

                    new_pdf.write(dataDir+title+".pdf")
            return True
        except Exception as ex:
            print(ex)
            pass        
# if __name__=="__main__":
#     pageServiceHelper=PageService("http://tinman.cs.gsu.edu/~raj/")
