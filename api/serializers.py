from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Label, Pain, Vote

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
    can_vote = serializers.SerializerMethodField()

    def get_can_vote(self, obj):
        # Query to see if the user has a vote against the current object id
        currentUserId = self.context['request'].user.id
        painId = obj.id
        try:
            result = Vote.objects.get(pain=painId, user=currentUserId)
            return result.id
        except Vote.DoesNotExist:
            return -1

    class Meta:
        model = Pain
        fields = ['title', 'description', 'labels', 'created', 'id', 'vote_count','can_vote']
    
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

class CreateVoteSerializer(serializers.ModelSerializer):
    
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Vote
        fields = ['user', 'pain']

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ['id', 'user', 'pain']
