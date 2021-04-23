import pdfrw
import os

class PageService():

    def __init__(self,baseUrl,pdfDict):
        self.baseUrl=baseUrl
        self.pdfDict=pdfDict
        self.translateBasePDF()
  
    def translateBasePDF(self):
        try:
            print("Inside Page Service")
            dataDir="documents\\"
            # print(self.baseUrl)
            baseFolder=self.baseUrl.replace("/","")
            baseFolder = baseFolder.replace("\\","")
            baseFolder = baseFolder.replace(":","")
            baseFolder = baseFolder.replace(".","")
            pdfList=os.listdir(dataDir+baseFolder)
            # print(pdfList)
            # print(baseFolder)
            # print(self.pdfDict)

            pdf = pdfrw.PdfReader(dataDir+baseFolder+"\\"+self.pdfDict[self.baseUrl]+".pdf")
            new_pdf = pdfrw.PdfWriter()
            # print("Reader, Writer Initialized")
            # print(list(self.pdfDict.keys()))
            for page in pdf.pages: 
                for annot in page.Annots or []:
                    # print("Reading Annotation")
                    # if("/A" in list(annot.keys())):
                    #     if("/URI" in list(annot.A.keys())):
                    #         old_url = annot.A.URI
                    #         key=annot.A.URI
                    # elif("/Dest" in list(annot.keys())):
                    #     old_url=annot.Dest
                    #     key=annot.Dest
                    # else:
                    #     continue
                    old_url = annot.A.URI
                    old_url=old_url.replace("(","")
                    old_url=old_url.replace(")","")
                    
                    # print("oldurl",old_url)
                    if(old_url in list(self.pdfDict.keys())):
                        
                        if(self.pdfDict[old_url]+".pdf" in pdfList):
                            outUrl="("+self.pdfDict[old_url]+".pdf)"
                            # print("outurl",outUrl)
                            new_url = pdfrw.objects.pdfstring.PdfString(outUrl)
                            annot.A.URI= new_url

                new_pdf.addpage(page)    

            new_pdf.write(dataDir+baseFolder+"\\"+self.pdfDict[self.baseUrl]+".pdf")

            if(self.translatePDFs(dataDir+baseFolder+"\\",pdfList)):
                return True
            else:
                return False
            return self.translatePDFs(dataDir+baseFolder+"\\",pdfList)
        except Exception as ex:
            # print(ex)
            pass

    def translatePDFs(self,dataDir,pdfList):
        try:
            print("Inside translatePDFs")
            base=self.baseUrl.replace("https://","")
            base=base.replace("http://","")
            base=base.replace("www.","")
            base=base[:-1]
            for url,title in self.pdfDict.items():
                # url=url.replace("https://","")
                # url=url.replace("http://","")
                # url=url.replace("www.","")
                
                # if(url!=base and title+".pdf" in pdfList):
                if(title!=self.pdfDict[self.baseUrl]):
                    pdf = pdfrw.PdfReader(dataDir+title+".pdf")
                    new_pdf = pdfrw.PdfWriter()
                    print("url,title,base",url,title,self.pdfDict[self.baseUrl])
                    print("Reader, Writer Initialized")

                    for page in pdf.pages: 
                        for annot in page.Annots or []:
                            if("/A" in list(annot.keys())):
                                if("/URI" in list(annot.A.keys())):
                                    old_url = annot.A.URI
                            elif("/Dest" in list(annot.keys())):
                                old_url=annot.Dest
                            else:
                                continue
                            old_url=old_url.replace("(","")
                            old_url=old_url.replace(")","")
                            if(old_url[-1]=="/"):
                                old_url=old_url[:-1]
                            if(old_url in list(self.pdfDict.keys())):
                                if(self.pdfDict[old_url]+".pdf" in pdfList):
                                    outUrl="("+self.pdfDict[old_url]+".pdf)"
                                    new_url = pdfrw.objects.pdfstring.PdfString(outUrl)

                                    if("/A" in list(annot.keys())):
                                        if("/URI" in list(annot.A.keys())):
                                            annot.A.URI=new_url
                                    elif("/Dest" in list(annot.keys())):
                                        annot.Dest=new_url

                                    print("pdf modified",dataDir+title+".pdf")
                                    print("new url added",new_url)

                        new_pdf.addpage(page)    
                    
                    new_pdf.write(dataDir+title+".pdf")
            return True
        except Exception as ex:
            # print("Exception caught")
            # print(ex)
            pass        
# if __name__=="__main__":
#     dictTest={'https://martinfowler.com': 'martinfowlercom', 'https://thoughtworks.com/careers': 'US Careers  ThoughtWorks  ThoughtWorks', 'https://martinfowler.com/articles/202101-lies-and-democracy.html': 'The Lies that can Undermine Democracy', 'http://www.thoughtworks.com/privacy-policy': 'Privacy Policy  ThoughtWorks', 'https://thoughtworks.com': 'ThoughtWorks A Global Software Consultancy  ThoughtWorks', 'https://martinfowler.com/bliki/RefinementCodeReview.html': 'RefinementCodeReview', 'https://martinfowler.com/articles/developer-effectiveness.html': 'Maximizing Developer Effectiveness', 'https://thoughtworks.com/products': '404-page  ThoughtWorks', 'https://martinfowler.com/articles/bitemporal-history.html': 'Bitemporal History', 'https://martinfowler.com/bliki/PullRequest.html': 'PullRequest', 'https://refactoring.com': 'Refactoring', 'https://martinfowler.com/articles/patterns-of-distributed-systems/': 'Patterns of Distributed Systems', 'https://www.twitter.com/martinfowler': 'NoTitle18', 'http://www.thoughtworks.com': 'ThoughtWorks A Global Software Consultancy  ThoughtWorks', 'https://thoughtworks.com/insights': 'Insights  ThoughtWorks  ThoughtWorks', 'https://www.thoughtworks.com': 'ThoughtWorks A Global Software Consultancy  ThoughtWorks', 'https://www.martinfowler.com/': 'martinfowlercom'}
#     pageServiceHelper=PageService("https://www.martinfowler.com/",dictTest)
