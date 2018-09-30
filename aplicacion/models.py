from django.db import models


class User(models.Model):
    name      = models.CharField(max_length=50)
    email     = models.EmailField(max_length=30,unique= True)
    password  = models.CharField(max_length=100)
    language  = models.CharField(max_length=30)
    birthdate = models.DateField()
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics', default='profile_pics/no-image.jpg')

    def __str__(self):
        return self.name


class Course(models.Model):
    teacher     = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=50)
    description = models.TextField()
    level       = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Take(models.Model):
    student     = models.ForeignKey(User, on_delete=models.CASCADE)
    course     = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_rating = models.IntegerField()
    teacher_rating = models.IntegerField()

    def __str__(self):
        return self.course.title + " - " + self.student.name
