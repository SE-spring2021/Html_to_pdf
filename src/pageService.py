import PyPDF2

class PageService():
  
    def translateLinks(self):
        PDFFile = open("Raj Sunderraman's Home Page.pdf",'rb')

        PDF = PyPDF2.PdfFileReader(PDFFile)
        pages = PDF.getNumPages()
        key = '/Annots'
        uri = '/URI'
        ank = '/A'

        for page in range(pages):
            print("Current Page: {}".format(page))
            pageSliced = PDF.getPage(page)
            pageObject = pageSliced.getObject()
            if key in pageObject.keys():
                ann = pageObject[key]
                for a in ann:
                    # print(a)
                    u = a.getObject()
                    print(u)
                    # if uri in u[ank].keys():
                    #     print(u[ank][uri])

if __name__=="__main__":
    pageServiceHelper=PageService()
    pageServiceHelper.translateLinks()
