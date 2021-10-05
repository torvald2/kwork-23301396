import re
from bs4 import BeautifulSoup

class ParsingError(Exception):
    pass


class ItemPage:
    COMMISION_PRICE_SELECTOR = '#infoBlockProductCard > div.same-part-kt__price-block.hide-mobile > div > div > p.price-block__commission-wrap > span:nth-child(1)'
    FREE_PRICE_SELECTOR = '#infoBlockProductCard > div.same-part-kt__price-block.hide-mobile > div > div > p.price-block__commission-wrap > span.price-block__price-commission.price-block__price-commission--free > span.price-block__free-commission'
    def __init__(self, itemData,itemId):
        self.page = BeautifulSoup(itemData,'html.parser')
        self.itemId = itemId
        self.__parse()
        
    def __parse(self):
        commisionPriceRaw = self.page.select_one(self.COMMISION_PRICE_SELECTOR)
        freePriceRaw = self.page.select_one(self.FREE_PRICE_SELECTOR)
        try:
            self.__comisionPrice =float(re.sub('[^\d\.]', '', commisionPriceRaw.string))
            self.__freePrice = float(re.sub('[^\d\.]', '', freePriceRaw.string))
        except Exception as e:
            raise ParsingError(f"Не удалось спарсить товар.{self.itemId} Ошибка {e}")

    @property
    def prices(self):
        return (self.__comisionPrice, self.__freePrice)
