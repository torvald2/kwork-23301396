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
        db = Db("testData.db")



if __name__ == '__main__':
    unittest.main()