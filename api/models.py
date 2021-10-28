from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Pain(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    labels = models.ManyToManyField(Label)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

