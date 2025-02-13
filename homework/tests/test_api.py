import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.urls import reverse
from base.models import GuardianStudent, Staff, Guardian, Student, StudentGroup
from ..models import Homework
from datetime import date

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def _create_user(username, password, is_staff=False):
        user = User.objects.create_user(username=username, password=password, is_staff=is_staff)
        if is_staff:
            Staff.objects.create(user=user)
        else:
            Guardian.objects.create(user=user)
        return user
    return _create_user

@pytest.fixture
def create_homework():
    def _create_homework(title, description):
        student_group = StudentGroup.objects.create(name="Test Group")
        return Homework.objects.create(title=title, description=description, student_group=student_group, due_date=date.today())
    return _create_homework

@pytest.fixture
def get_token():
    def _get_token(user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    return _get_token

@pytest.mark.django_db
class TestHomeworkAPI:
    def test_homework_list(self, api_client, create_user, get_token):
        user = create_user('guardian', 'password')
        token = get_token(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        url = reverse('homework-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_homework_create(self, api_client, create_user, get_token):
        user = create_user('staff', 'password', is_staff=True)
        token = get_token(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        student_group = StudentGroup.objects.create(name="Test Group")
        data = {'title': 'Test Homework', 'description': 'Test Description', 'due_date': str(date.today()), 'student_group': student_group.id}
        url = reverse('homework-list')
        response = api_client.post(url, data)
        assert response.status_code == 201
        assert response.data['title'] == 'Test Homework'
        assert response.data['description'] == 'Test Description'
        # assert response.data['due_date'] == str(date.today().isoformat())
        assert response.data['student_group'] == student_group.id

    def test_homework_create_invalid_data(self, api_client, create_user, get_token):
        user = create_user('staff', 'password', is_staff=True)
        token = get_token(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        data = {'title': '', 'description': 'Test Description', 'due_date': str(date.today())}
        url = reverse('homework-list')
        response = api_client.post(url, data)
        assert response.status_code == 400

    def test_homework_update(self, api_client, create_user, create_homework, get_token):
        user = create_user('staff', 'password', is_staff=True)
        token = get_token(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        homework = create_homework('Old Title', 'Old Description')
        data = {'title': 'Updated Title', 'description': 'Updated Description', 
                'due_date': str(date.today()), 'student_group': homework.student_group.id}
        url = reverse('homework-detail', args=[homework.id])
        response = api_client.put(url, data)
        assert response.status_code == 200
        assert response.data['title'] == 'Updated Title'
        assert response.data['description'] == 'Updated Description'        
        assert response.data['student_group'] == homework.student_group.id

    def test_homework_update_invalid_data(self, api_client, create_user, create_homework, get_token):
        user = create_user('staff', 'password', is_staff=True)
        token = get_token(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        homework = create_homework('Old Title', 'Old Description')
        data = {'title': '', 'description': 'Updated Description', 'due_date': str(date.today())}
        url = reverse('homework-detail', args=[homework.id])
        response = api_client.put(url, data)
        assert response.status_code == 400

    def test_homework_delete(self, api_client, create_user, create_homework, get_token):
        user = create_user('staff', 'password', is_staff=True)
        token = get_token(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        homework = create_homework('Title', 'Description')
        url = reverse('homework-detail', args=[homework.id])
        response = api_client.delete(url)
        assert response.status_code == 204

    def test_homework_retrieve(self, api_client, create_user, create_homework, get_token):
        user = create_user('guardian', 'password')
        token = get_token(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        homework = create_homework('Title', 'Description')
        student = Student.objects.create(first_name="Ahmed", last_name="Nour", date_of_birth=str(date.today()), group=homework.student_group)
        GuardianStudent.objects.create(guardian=user.guardian_profile, student=student, relationship="Father")
        url = reverse('homework-detail', args=[homework.id])
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data['title'] == 'Title'
        assert response.data['description'] == 'Description'        
        assert response.data['student_group'] == homework.student_group.id
