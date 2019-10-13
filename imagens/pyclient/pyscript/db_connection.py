import json

import Config
from kafka import KafkaProducer


def getConnKafkaProducer():
    connection = KafkaProducer(bootstrap_servers=Config.KAFKA_CONFIG["Server"]
                               ,value_serializer=lambda m: json.dumps(m).encode('ascii'))
    return connection
