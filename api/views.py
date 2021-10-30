from rest_framework import viewsets

from .serializers import LabelSerializer, DetailPainSerializer, DetailLabelSerializer
from .models import Label, Pain

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
