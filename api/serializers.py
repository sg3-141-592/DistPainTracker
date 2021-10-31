from rest_framework import serializers
from .models import Label, Pain

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name']

class PainLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pain
        fields = ['id', 'title']

class DetailLabelSerializer(serializers.ModelSerializer):

    pain = PainLabelSerializer(many=True)

    class Meta:
        model = Label
        fields = ['id', 'name', 'pain']

class DetailPainSerializer(serializers.ModelSerializer):

    labels = LabelSerializer(many=True)

    class Meta:
        model = Pain
        fields = ['title', 'description', 'labels', 'created', 'id']
    
    def create(self, validated_data):
        newPain = Pain(
            title= validated_data['title'],
            description= validated_data['description']
        )
        newPain.save()
        return newPain

class CreatePainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pain
        fields = ['title', 'description', 'labels', 'id']
