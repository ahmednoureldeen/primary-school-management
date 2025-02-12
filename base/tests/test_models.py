import pytest
from django.contrib.auth.models import User
from ..models import Staff, Guardian, StudentGroup, Student, GuardianStudent

@pytest.mark.django_db
class TestModels:
    def test_create_staff(self):
        user = User.objects.create_user(
            username='Ahmed',
            password='testpass123'
        )
        staff = Staff.objects.create(user=user)
        staff.refresh_from_db() 
        assert staff.user.username == 'Ahmed'

    def test_create_guardian(self):
        user = User.objects.create_user(
            username='Omar',
            password='testpass123'
        )
        guardian = Guardian.objects.create(user=user)
        guardian.refresh_from_db()
        assert guardian.user.username == 'Omar'

    def test_create_student(self):
        group = StudentGroup.objects.create(name='1')
        student = Student.objects.create(
            first_name='Mohammed',
            last_name='Al-Sayed',
            group=group,
            date_of_birth='2015-01-01'
        )
        student.refresh_from_db()
        assert student.first_name == 'Mohammed'
        assert student.last_name == 'Al-Sayed'
        assert student.group == group

    def test_create_multiple_students(self):
        group = StudentGroup.objects.create(name='2')
        students_data = [
            ('Yusuf', 'Abdullah'),
            ('Fatima', 'Al-Rahman'),
            ('Zainab', 'Ibrahim')
        ]
        
        for first_name, last_name in students_data:
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                group=group,
                date_of_birth='2015-01-01'
            )
            student.refresh_from_db()
            assert student.first_name == first_name
            assert student.last_name == last_name

    def test_create_guardian_student_relationship(self):
        user = User.objects.create_user(
            username='khalid',
            password='testpass123'
        )
        guardian = Guardian.objects.create(user=user)
        group = StudentGroup.objects.create(name='3')
        student = Student.objects.create(
            first_name='Sara',
            last_name='Khalid',
            group=group,
            date_of_birth='2015-01-01'
        )

        guardian_student = GuardianStudent.objects.create(
            guardian=guardian,
            student=student,
            relationship='father'
        )
        guardian_student.refresh_from_db()
        assert guardian_student.relationship == 'father'

    def test_multiple_guardians_for_student(self):
        group = StudentGroup.objects.create(name='4')
        student = Student.objects.create(
            first_name='Layla',
            last_name='Al-Rashid',
            group=group,
            date_of_birth='2015-01-01'
        )
        
        guardian_data = [
            ('rashid', 'father'),
            ('maryam', 'mother'),
            ('ahmad', 'uncle')
        ]
        
        for username, relationship in guardian_data:
            user = User.objects.create_user(
                username=username,
                password='testpass123'
            )
            guardian = Guardian.objects.create(user=user)
            guardian_student = GuardianStudent.objects.create(
                guardian=guardian,
                student=student,
                relationship=relationship
            )
            guardian_student.refresh_from_db()
            assert guardian_student.relationship == relationship
