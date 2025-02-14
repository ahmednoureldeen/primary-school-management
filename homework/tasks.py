from celery import shared_task
from django.core.mail import send_mail
from base.models import Guardian

@shared_task
def notify_guardians(homework_id):
    from .models import Homework
    print(f'Sending homework notification{homework_id}')
    homework = Homework.objects.get(id=homework_id)
    students = homework.student_group.students.all()    
    
    for student in students:
        for guardian in student.guardians.all():
            print(
                    f'New Homework Assigned: {homework.title}\
                    Homework Description: {homework.description}\
                    Assigned to: {student.first_name} {student.last_name}\
                    To guardian: {guardian.user.username}'
                )
