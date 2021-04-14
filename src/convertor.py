from weasyprint import HTML, CSS

class Convertor():


    def convertToPdf(self, html:str):

        html = HTML(string='<h1>Header</h1>')
        pdf = html.write_pdf()
        open('google.pdf', 'wb').write(pdf)

if __name__ == "__main__":
        c = Convertor()
        c.convertToPdf("")