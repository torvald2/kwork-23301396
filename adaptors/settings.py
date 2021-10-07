import sys

class Settings:
    def __init__(self) -> None:
        try:
            self.dbName = sys.argv[1]
        except IndexError:
            self.dbName = "main.db"
        try:
            self.loginingMode = sys.argv[4]
        except IndexError:
            self.loginingMode = "info"
        try:
            self.excelPath = sys.argv[2]
        except IndexError:
            self.excelPath= 'articles.xlsx'
        try:
            self.outputPath = sys.argv[3]
        except:
            self.outputPath = "./output"
            