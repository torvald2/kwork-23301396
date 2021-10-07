import time
import logging
import datetime
from adaptors.excel import SettingsData
from adaptors.internalDb import Db
from adaptors.parser import ItemPage, ParsingError
from adaptors.wildberries import getData, GetDataException
from adaptors.settings import Settings

appSettings = Settings()


if appSettings.loginingMode == "debug":
    LOG_LEVEL = logging.DEBUG
else:
    LOG_LEVEL = logging.INFO

logging.basicConfig(filename='app.log', level=LOG_LEVEL, format='%(asctime)s %(levelname)s %(message)s')


def processData():
    db = Db(appSettings.dbName)
    items = SettingsData(appSettings.excelPath)
    parsedDate = datetime.datetime.now()
    res = []

    for item in items.articles:
        time.sleep(4)
        try:
            data = getData(item["Артикул WB"])
            page = ItemPage(data,item["Артикул WB"])
            prices = page.prices
            db.setItem(f'{parsedDate}',item["Артикул WB"],prices[0],prices[1])
            item["Текущая цена ВБ"] = prices[1]
            item['дата; время'] = parsedDate.strftime("%m-%d-%Y, %H:%M:%S")
            res.append(item)
            logging.debug(f'PARSED Item {item["Артикул WB"]} Цена {prices[1]}')
        except GetDataException as e:
            logging.error(e)
        except ParsingError as e:
            logging.error(e)
    SettingsData.write_to_excel(appSettings.outputPath,res)
    db.disconect()


if __name__ == "__main__":
    try:
        processData()
    except Exception as e:
        logging.error(f"===ОШИБКА ЗАПУСКА ПРОГРАММЫ {e}")

        
        
        


