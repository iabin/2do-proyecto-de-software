from django.db import models


class User(models.Model):
    name      = models.CharField(max_length=50)
    email     = models.CharField(max_length=30)
    password  = models.CharField(max_length=100)
    language  = models.CharField(max_length=30)
    birthdate = models.DateField()


class Course(models.Model):
    teacher     = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=50)
    description = models.TextField()
    level       = models.CharField(max_length=30)


class Take(models.Model):
    student     = models.ForeignKey(User, on_delete=models.CASCADE)
    course     = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_rating = models.IntegerField()
    teacher_rating = models.IntegerField()
