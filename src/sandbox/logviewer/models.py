from django.db import models

# Create your models here.

class Changeset(models.Model):
    revision = models.IntegerField()
    committer = models.CharField(max_length=200)
    commit_date = models.DateTimeField()
