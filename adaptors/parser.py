import re
from bs4 import BeautifulSoup

class ParsingError(Exception):
    pass


class ItemPage:
    COMMISION_PRICE_SELECTOR = '#root > div > div.main-layout_content__cg0Zt > div > div > div.page_content__3N2rR > div.page_priceContainer__3LDLr > div > div > div.prices_priceBox__2mpG1 > div > div > div > div > div.prices_finalPrice__1ShwA.prices_accent__FfE9q'
    FREE_PRICE_SELECTOR = 'body > div.popper-wrapper_root__1IWrR.tooltip_tooltip__1bzTK.prices_tooltipPopper__bj1hd.prices_rewrite__3e3l0.popper-wrapper_rewrite__lCpWS > div > div:nth-child(3) > div.prices_value__1Xvkd'
    def __init__(self, itemData,itemId):
        self.page = BeautifulSoup(itemData,'html.parser')
        self.itemId = itemId
        self.__parse()
        self.__comisionPrice = 0
        
    def __parse(self):
        freePriceRaw = self.page.find_all("span", {"class": "price-block__price-free-commission"})
        try:
            self.__freePrice = float(re.sub('[^\d\.]', '', freePriceRaw[0].string))
        except Exception as e:
            raise ParsingError(f"Не удалось спарсить товар.{self.itemId} Ошибка {e}")

    @property
    def prices(self):
        return (self.__comisionPrice, self.__freePrice)
