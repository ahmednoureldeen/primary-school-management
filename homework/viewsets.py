from rest_framework import serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from base.models import Guardian, Staff
from base.viewsets import IsGuardianOrStaff, IsStaff
from .models import Homework

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsStaff]
        else:
            self.permission_classes = [IsGuardianOrStaff]
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        if Staff.objects.filter(user=user).exists():
            return Homework.objects.all()        
        if Guardian.objects.filter(user=user).exists():
            return Homework.objects.filter(student_group__students__guardianstudent__guardian=user.guardian_profile).all()
        return Homework.objects.none()
