from django.db import models
import uuid

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1(), editable=False,null=False)
    name = models.CharField(max_length=6,null=False)
    age = models.IntegerField()
    time = models.DateField(auto_now=True,null=False)