import datetime
from haystack import indexes
from .models import Pain, Label
import datetime

class PainIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Pain
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class LabelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    title = indexes.CharField(model_attr='name')

    def get_model(self):
        return Label
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
