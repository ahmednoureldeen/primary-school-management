import pytest
import django
from django.conf import settings

@pytest.fixture(autouse=True)
def mock_celery_delay(mocker):
    mocker.patch("celery.app.task.Task.delay", return_value=1)


@pytest.fixture(autouse=True)
def mock_homework_document(mocker):
    mocker.patch("homework.documents.HomeworkDocument.update", return_value=None)
    mocker.patch("homework.documents.HomeworkDocument.delete", return_value=None)

def pytest_configure():
    # Override only the database settings for testing
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test.db',
        }
    }
    

    django.setup()
