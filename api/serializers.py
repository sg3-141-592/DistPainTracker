from rest_framework import serializers
from .models import Label, Pain

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name']

class PainSerializer(serializers.ModelSerializer):

    labels = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset = Label.objects.all(),
        slug_field='name')

    class Meta:
        model = Pain
        fields = ['title', 'description', 'labels', 'created']
