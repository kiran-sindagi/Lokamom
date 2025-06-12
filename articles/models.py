from django.db import models # type: ignore
from django.urls import reverse # type: ignore
 # type: ignore
from django.utils.timezone import now # type: ignore
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    question = models.TextField()
    owner = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.body


    