from rest_framework import serializers, viewsets
from rest_framework.permissions import BasePermission

from .models import Guardian, GuardianStudent, Student, StudentGroup, Staff

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'  


class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'

class GurdianStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardianStudent
        fields = '__all__'


class IsStaff(BasePermission):
    def has_permission(self, request, view):   
        return request.user.is_authenticated and Staff.objects.filter(user=request.user).exists()

class IsGuardianOrStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if Staff.objects.filter(user=request.user).exists():
            return True
        guardian = request.user.guardian_profile
        return guardian and obj.student_group.students.filter(guardianstudent__guardian=guardian).exists()


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer

class GuardianViewSet(viewsets.ModelViewSet):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer

class GuardianStudentViewSet(viewsets.ModelViewSet):
    queryset = GuardianStudent.objects.all()
    serializer_class = GurdianStudentSerializer
