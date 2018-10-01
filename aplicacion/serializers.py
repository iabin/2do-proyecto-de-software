from django.contrib.auth.models import User
from aplicacion.models import Course,Take
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','teacher','title','description','level')

class TakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Take
        fields = ('id','student','course','teacher_rating','student_rating')
