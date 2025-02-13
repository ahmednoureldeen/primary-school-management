from rest_framework import serializers, viewsets

from .models import Guardian, GuardianStudent, Student, StudentGroup

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
