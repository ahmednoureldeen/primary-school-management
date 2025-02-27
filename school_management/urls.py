"""
URL configuration for school_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from homework.viewsets import HomeworkViewSet
from homework.urls import urlpatterns as homework_urlpatterns

from base.viewsets import StudentGroupViewSet, StudentViewSet, GuardianViewSet, GuardianStudentViewSet

# API Routing
router = DefaultRouter()

router.register(r'homework', HomeworkViewSet)
router.register(r'student', StudentViewSet)
router.register(r'group', StudentGroupViewSet)
router.register(r'guardian', GuardianViewSet)
router.register(r'guardian_student', GuardianStudentViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('homework/', include(homework_urlpatterns)),
]
