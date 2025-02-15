from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from .models import Homework

# Define the Elasticsearch index
homework_index = Index('homework')

# Define the settings for the index
homework_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
class HomeworkDocument(Document):
    class Index:
        name = 'homework'

    class Django:
        model = Homework
        fields = [ 'title','description']

    def get_queryset(self):
        return super(HomeworkDocument, self).get_queryset()

@receiver(post_save, sender=Homework)
def update_homework_document(sender, instance, created, **kwargs):
    HomeworkDocument().update(instance)

@receiver(post_delete, sender=Homework)
def delete_homework_document(sender, instance, **kwargs):
    HomeworkDocument().delete(instance)