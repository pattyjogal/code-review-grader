# pylint: disable=missing-docstring,too-few-public-methods
from rest_framework import serializers
from .models import Assignment, RubricField, AssignmentSubmission


class AssignmentSerializer(serializers.ModelSerializer):
    assignment_submissions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=AssignmentSubmission.objects.all())

    class Meta:
        model = Assignment
        fields = ('created_at', 'updated_at', 'name', 'description')
