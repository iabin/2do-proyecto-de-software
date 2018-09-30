from aplicacion.models import User,Course,Take
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email','password','language','birthdate','profile_pic')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','teacher','title','description','level')

class TakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Take
        fields = ('id','student','course','teacher_rating','student_rating')
