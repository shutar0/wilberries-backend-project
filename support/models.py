from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)