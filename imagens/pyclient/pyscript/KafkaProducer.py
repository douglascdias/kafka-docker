import db_connection as conn
import ReqCT as Req2
import json
from time import sleep


ErroConn = True

while ErroConn:
    try:
        topicName = 'test'
        producer = conn.getConnKafkaProducer()
        ErroConn = False
    except:
        print("Erro de conexao")
        sleep(10)

uri = 'https://www.climatempo.com.br'
page = '/previsao-do-tempo/15-dias/cidade/558/saopaulo-sp'

response, soup = Req2.URIPage(uri, page)

cards = soup.find_all('div', id=lambda x: x and x.startswith('wrapperForecastCard1'))

while True:
    data = []
    if response.status_code == 200:
        data = Req2.CardParse(cards)

    data_json = json.dumps(data)

    producer.send(topicName, data_json)
    producer.flush()

    #producer.close()

    sleep(10)
