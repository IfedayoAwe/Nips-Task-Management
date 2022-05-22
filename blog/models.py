from django.db import models
from django.utils import timezone
from users.models import User

class Post(models.Model):
    task = models.CharField(max_length=50)
    details = models.TextField(max_length=5000)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_from = models.DateField("Time From(yyyy-mm-dd)", auto_now_add=False, auto_now=False)
    time_to = models.DateField("Time To(yyyy-mm-dd)", auto_now_add=False, auto_now=False)

    def __str__(self):
        return f'{self.task}'