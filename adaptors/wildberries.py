import requests

class GetDataException(Exception):
    pass

def getData(itemId):
    url = f'https://www.wildberries.ru/catalog/{itemId}/detail.aspx?targetUrl=MI'
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    else:
        raise GetDataException(f"Ошибка получения данных. Код ответа {resp.status_code}")