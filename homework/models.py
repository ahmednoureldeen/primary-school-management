from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from base.models import StudentGroup
from .tasks import notify_guardians


class Homework(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    student_group = models.ForeignKey(StudentGroup, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=Homework)
def send_homework_notification(sender, instance, created, **kwargs):
    if created:
        notify_guardians.delay(instance.id)
