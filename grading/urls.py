from django.urls import path, include
from rest_framework import routers

from .views import TestTemplateView

router = routers.DefaultRouter()
router.register('test-templates', TestTemplateView, basename='templates')

urlpatterns = [
    path('templates/', include((router.urls, 'templates')))
]
