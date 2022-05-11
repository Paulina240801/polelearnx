from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Student(User):
    pass


class Teacher(User):
    students = models.ManyToManyField(Student)


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
