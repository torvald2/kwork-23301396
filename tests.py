from datetime import datetime
import unittest

from adaptors.parser import ItemPage
from adaptors.internalDb import Db

class TestParser(unittest.TestCase):
    def testParser(self):
        with open("testPage.html") as f:
            data = f.read()
            item = ItemPage(data)
            prises = item.prices
            self.assertEqual(prises[0], 1480.0)
            self.assertEqual(prises[1], 1451.0)

class TestInnerDb(unittest.TestCase):
    def testData(self):
        parsedDate = datetime.now()
        db = Db("testData.db")
        db.setItem(parsedDate,"1",123.0,124.0)
        rows = db.records
        self.assertEqual(rows[0][0],f'{parsedDate}')
        self.assertEqual(rows[0][1],1)
        self.assertEqual(rows[0][2],123.0)
        self.assertEqual(rows[0][3],124.0)
        db.clearData()
        db.disconect()



if __name__ == '__main__':
    unittest.main()