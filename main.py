import sys
import logging
import datetime
from adaptors.excel import SettingsData
from adaptors.internalDb import Db
from adaptors.parser import ItemPage, ParsingError
from adaptors.wildberries import getData, GetDataException

LEVEL = sys.argv[3]

if LEVEL == "debug":
    LOG_LEVEL = logging.DEBUG
else:
    LOG_LEVEL = logging.ERROR

logging.basicConfig(filename='app.log', level=LOG_LEVEL, format='%(asctime)s %(levelname)s %(message)s')


def processData():
    db = Db(sys.argv[1])
    items = SettingsData(sys.argv[2])
    parsedDate = datetime.datetime.now()

    for item in items.articles:
        try:
            data = getData(item["Артикул WB"])
            page = ItemPage(data,item["Артикул WB"])
            prices = page.prices
            db.setItem(f'{parsedDate}',item["Артикул WB"],prices[0],prices[1])
            logging.debug(f'PARSED Item {item["Артикул WB"]} Цена {prices[0]}')
        except GetDataException as e:
            logging.error(e)
        except ParsingError as e:
            logging.error(e)
    db.disconect()


if __name__ == "__main__":
    try:
        processData()
    except Exception as e:
        logging.error(f"===ОШИБКА ЗАПУСКА ПРОГРАММЫ {e}")

        
        
        


