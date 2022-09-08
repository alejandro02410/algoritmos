from django.db import models

# Create your models here.

class endNum(models.Model):

    net = models.IntegerField(blank=True, null=True)

    net2 = models.IntegerField(blank=True, null=True)

    net3 = models.IntegerField(blank=True, null=True)

    flop = models.FloatField(blank=True, null=True)

    def __str__(self):

        return str(self.net)