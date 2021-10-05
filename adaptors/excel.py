import pandas as pd

class SettingsData:
    def __init__(self,pathToFile):
        data = pd.read_excel(pathToFile,sheet_name="Лист2")
        self.__articles=data.to_dict('records')
    @property
    def articles(self):
        return self.__articles

        