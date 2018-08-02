from rest_framework import serializers

from .models import Feedback


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'text', 'created_date')