from django.core.management.base import BaseCommand
from ...partex.apps.listings.models import Listing
from elasticsearch import Elasticsearch

def get_fixtures(index, doc_type):
    all_listings = [lst.indexing() for lst in Listing.objects.all()]
    for lsting in all_listings:
        yield: {
            '_index': index,
            '_type': doc_type,
            '_id': lsting['id'],
            'doc': lsting
        }

def init_index():
    es = Elasticsearch(['es'])
    bulk(es, get_fixtures('listing_index', 'listing')

class Command(BaseCommand):
    def handle(self, **options):
        init_index()
