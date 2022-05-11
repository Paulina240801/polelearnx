from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Teacher(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_teacher = models.BooleanField(default=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.user.username


class TestTemplate(models.Model):
    name = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Test(models.Model):
    test_template = models.ForeignKey(TestTemplate, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Question(models.Model):
    test = models.ForeignKey(TestTemplate, on_delete=models.CASCADE)
    expected_value = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.TextField()
