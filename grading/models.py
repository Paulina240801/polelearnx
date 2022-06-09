from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.TextField()
    last_name = models.TextField()


class Student(User):
    pass


class Teacher(User):
    students = models.ManyToManyField(Student, blank=True)


class TestTemplate(models.Model):
    name = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Test(models.Model):
    test_template = models.ForeignKey(TestTemplate, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class QuestionTemplate(models.Model):
    test_template = models.ForeignKey(TestTemplate, on_delete=models.CASCADE)
    text = models.TextField()
    expected_value = models.TextField()


class Question(models.Model):
    test_template = models.ForeignKey(QuestionTemplate, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)


class Answer(models.Model):
    value = models.TextField()
    answer = models.OneToOneField(Question, on_delete=models.CASCADE, null=True, blank=True)

