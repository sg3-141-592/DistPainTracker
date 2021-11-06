from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Label, Pain, Vote

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return LabelSerializer
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
