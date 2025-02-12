import pytest
import django
from django.conf import settings

def pytest_configure():
    # Override only the database settings for testing
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test.db',
        }
    }

    django.setup()
