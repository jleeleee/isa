from django.core.management.base import BaseCommand
from ...listings.models import Listing
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

def get_fixtures(index, doc_type):
    all_listings = [lst.indexing() for lst in Listing.objects.all()]
    for lsting in all_listings:
        print(lsting)
        yield {
            '_index': index,
            '_type': doc_type,
            '_id': lsting['id'],
            'doc': lsting
        }

def init_index():
    es = Elasticsearch(['es'])
    all_listings = [lst.get_dict() for lst in Listing.objects.all()]
    for listing in all_listings:
        es.index(index='listing_index',
                 doc_type='listing',
                 id=listing['id'],
                 body=listing
                 )
    # bulk(es, get_fixtures('listing_index', 'listing'))
    es.indices.refresh(index='listing_index')

class Command(BaseCommand):
    def handle(self, **options):
        init_index()
        print("done")
