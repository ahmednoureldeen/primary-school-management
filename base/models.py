from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')


class Guardian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='guardian_profile')


GRADES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'))

# StudentGroup model is representing the class of the student.
class StudentGroup(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, choices=GRADES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    group = models.ForeignKey(StudentGroup, null=False, blank=False, on_delete=models.PROTECT)
    date_of_birth = models.DateField(null=False, blank=False)
    guardians = models.ManyToManyField(Guardian, through='GuardianStudent')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GuardianStudent(models.Model):
    guardian = models.ForeignKey(Guardian, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    # Relationship of the guardian with the student could be father, mother, uncle, etc.
    relationship = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
