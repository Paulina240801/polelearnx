from rest_framework.viewsets import ModelViewSet

from grading.models import TestTemplate, Teacher, Question, Answer, Student, QuestionTemplate, Test
from grading.serializers import TestTemplateSerializer, StudentSerializer, QuestionSerializer, AnswerSerializer, \
    TeacherSerializer, QuestionTemplateSerializer, TestSerializer


class TestTemplateView(ModelViewSet):
    queryset = TestTemplate.objects.all()
    serializer_class = TestTemplateSerializer


class TestView(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class QuestionView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionTemplateView(ModelViewSet):
    queryset = QuestionTemplate.objects.all()
    serializer_class = QuestionTemplateSerializer


class AnswerView(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
