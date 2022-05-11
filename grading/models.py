from django.db import models


class TestTemplate(models.Model):
    name = models.TextField()


class Test(models.Model):
    test = models.ForeignKey(TestTemplate, on_delete=models.CASCADE)


class Question(models.Model):
    test = models.ForeignKey(TestTemplate, on_delete=models.CASCADE)
    expected_value = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.TextField()
