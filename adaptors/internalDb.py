import sqlite3
import datetime

class Db:
    def __init__(self,dbName):
        self.__con = sqlite3.connect(dbName)
        self.__con.execute('''CREATE TABLE IF NOT EXISTS data (
                       date string, 
                       article string,
                       commisionPrice real, 
                       freePrice real
                       )''')
        self.__con.commit()
    def setItem(self, arcticle, commisionPrice,freePrice):
        self.__con.execute(f''' INSERT INTO data VALUES(
                              {datetime.datetime.now()}
                              {arcticle},
                              {commisionPrice},
                              {freePrice} 
                               )
                              
                         ''')
        self.__con.commit()
    
    @property
    def records(self):
        return [row for row in self.__con.execute('SELECT * FROM data')]

    def clearData(self):
        self.__con.execute("DELETE FROM data")
    
    def disconect(self):
        self.__con.close()

