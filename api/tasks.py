from .models import Label
from celery import shared_task

# Delete all unused labels
# unreferencedObjects = Label.objects.filter(pain=None).delete()

@shared_task
def clearUpLabels():
    print("Cleaning up labels")
