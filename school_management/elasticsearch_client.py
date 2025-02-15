from elasticsearch import Elasticsearch
from django.conf import settings


es = Elasticsearch(settings.ELASTICSEARCH_DSL['default']['hosts'], http_auth=settings.ELASTICSEARCH_DSL['default']['http_auth'])