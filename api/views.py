from rest_framework import viewsets

from .serializers import LabelSerializer, PainSerializer
from .models import Label, Pain

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class PainViewSet(viewsets.ModelViewSet):
    queryset = Pain.objects.all()
    serializer_class = PainSerializer
