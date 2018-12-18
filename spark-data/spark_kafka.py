from kafka import KafkaConsumer
from kafka.common import NodeNotReadyError
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(['es'])

with open("/app/access.log", "a") as log:
    log.write("\n{}\t{}".format(1,1))
    kafka_starting = True
    while kafka_starting:
        try:
            consumer = KafkaConsumer('recommendations', group_id='rec_index', bootstrap_servers=['kafka:9092'])
            kafka_starting = False
        except NodeNotReadyError:
            kafka_starting = True

    for message in consumer:
        pair = json.loads((message.value).decode('utf-8'))
        log.write("\n{}\t{}".format(pair["user_id"], pair["item_id"]))
        log.flush()
