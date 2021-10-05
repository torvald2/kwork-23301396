import re
from bs4 import BeautifulSoup

class ItemPage:
    COMMISION_PRICE_SELECTOR = '#infoBlockProductCard > div.same-part-kt__price-block.hide-mobile > div > div > p.price-block__commission-wrap > span:nth-child(1)'
    FREE_PRICE_SELECTOR = '#infoBlockProductCard > div.same-part-kt__price-block.hide-mobile > div > div > p.price-block__commission-wrap > span.price-block__price-commission.price-block__price-commission--free > span.price-block__free-commission'
    def __init__(self, itemData):
        self.page = BeautifulSoup(itemData,'html.parser')
        self.__parse()
        
    def __parse(self):
        commisionPriceRaw = self.page.select_one(self.COMMISION_PRICE_SELECTOR)
        freePriceRaw = self.page.select_one(self.FREE_PRICE_SELECTOR)
        self.__comisionPrice =float(re.sub('[^\d\.]', '', commisionPriceRaw.string))
        self.__freePrice = float(re.sub('[^\d\.]', '', freePriceRaw.string))

    @property
    def prices(self):
        return (self.__comisionPrice, self.__freePrice)
