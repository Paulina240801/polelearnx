from django.urls import path, include
from rest_framework import routers

from grading import views

router = routers.DefaultRouter()
router.register('test-template', views.TestTemplateView, basename='test-template')
router.register('test', views.TestView, basename='test')
router.register('teacher', views.TeacherView, basename='teacher')
router.register('student', views.StudentView, basename='student')
router.register('question', views.QuestionView, basename='question')
router.register('question-template', views.QuestionTemplateView, basename='question-template')
router.register('answer', views.AnswerView, basename='answer')

urlpatterns = [
    path('', include((router.urls)))
]
