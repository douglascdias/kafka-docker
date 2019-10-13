import requests
from bs4 import BeautifulSoup
import datetime
import re

def URIPage(_uri, _page):
    print(_uri + _page)
    _response = requests.get(_uri + _page)
    _soup = BeautifulSoup(_response.content, 'html.parser')
    return _response, _soup


def CardParse(cards):
    data = []
    for card in cards:
        date = card.find(class_="-gray _float-l _max-w-75-pct").get_text()

        date = date.replace('\n', ' ').lstrip().rstrip()

        date1 = date

        minTemp = card.find(class_="min-temp").get_text()
        maxTemp = card.find(class_="max-temp").get_text()

        date2 = date1
        match = re.search('\d{2}/\\d{2}', date2)
        date2 = str(match.group()) + '/2019'

        date2 = datetime.datetime.strptime(date2, '%d/%m/%Y').date().strftime("%Y-%m-%d")

        ts = datetime.datetime.now()

        item = {"ts": str(ts), "data1": date1, "data2": date2, "TempoMin": minTemp, "TempoMax": maxTemp}
        data.append(item)
    return data