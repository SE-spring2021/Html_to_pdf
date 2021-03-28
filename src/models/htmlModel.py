class HtmlModel():
    def __init__(self,level, url):

        self.id = ""
        self.title = ""
        self.level = level
        self.url = url
        self.htmlContent = ""
        self.styles = ""
        self.links = set()