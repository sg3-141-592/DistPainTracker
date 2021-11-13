from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Label, Pain, Vote, Comment

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return LabelSerializer
        elif self.action == 'create':
            return CreateLabelSerializer
        else:
            return DetailLabelSerializer

class PainViewSet(viewsets.ModelViewSet):
    queryset = Pain.objects.all()
    serializer_class = DetailPainSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreatePainSerializer
        return DetailPainSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateVoteSerializer
        return VoteSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pain']

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCommentSerializer
        return CommentSerializer
