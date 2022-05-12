from rest_framework.viewsets import ViewSet, ModelViewSet

from grading.models import TestTemplate
from grading.serializers import TestTemplateSerializer


class TestTemplateView(ModelViewSet):
    queryset = TestTemplate.objects.all()
    serializer_class = TestTemplateSerializer
