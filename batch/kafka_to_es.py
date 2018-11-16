from kafka import KafkaConsumer
from kafka.common import NodeNotReadyError
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(['es'])

def add_listing(listing):
    es.index(index='listing_index',
             doc_type='listing',
             id=listing['id'],
             body=listing
             )
    es.indices.refresh(index='listing_index')

kafka_starting = True
while kafka_starting:
    try:
        consumer = KafkaConsumer('new-listings-topic', group_id='listing_indexer', bootstrap_servers=['kafka:9092'])
        kafka_starting = False
    except NodeNotReadyError:
        kafka_starting = True

for message in consumer:
    listing = json.loads((message.value).decode('utf-8'))
    add_listing(listing)
