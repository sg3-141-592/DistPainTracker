from django.db import models
from django.contrib.auth.models import User

class Label(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Pain(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    labels = models.ManyToManyField(Label, blank=True, related_name='pain')
    created = models.DateTimeField(auto_now_add=True)

    @property
    def vote_count(self):
        return Vote.objects.filter(pain__id=self.id).count()

    def __str__(self):
        return self.title

class Vote(models.Model):
    user = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)
    pain =  models.ForeignKey(Pain, related_name='votes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'pain')
    
    def __str__(self):
        return str(self.user) + " : " + str(self.pain)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    pain =  models.ForeignKey(Pain, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pain.title) + " : " + str(self.user) + " : " + self.created.strftime("%m/%d/%Y, %H:%M:%S")
