from django.contrib import admin
from .models import Pain, Label, Vote, Comment

admin.site.register(Pain)
admin.site.register(Label)
admin.site.register(Vote)
admin.site.register(Comment)
