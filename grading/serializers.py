from rest_framework import serializers

from grading.models import TestTemplate


class TestTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTemplate
        fields = ['id', 'name', 'teacher']