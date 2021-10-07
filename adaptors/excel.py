import os
import pandas as pd

class SettingsData:
    def __init__(self,pathToFile):
        data = pd.read_excel(pathToFile,sheet_name="Лист2")
        self.__articles=data.to_dict('records')
    @property
    def articles(self):
        return self.__articles
    @staticmethod
    def write_to_excel( pathToFile, data):
        df = pd.DataFrame.from_dict(data)
        if os.path.isfile(pathToFile):
            print("EXCEL")
            oldData = pd.read_excel(pathToFile,sheet_name="Sheet1")
            df = pd.concat([oldData,df])
        df.to_excel(pathToFile, index=False)


        