from django.db import models


class Testhome(models.Model):
    title = models.CharField("标题",max_length=48)
    tid = models.IntegerField(1)
    tdate = models.DateField()
    tdata = models.TextField()