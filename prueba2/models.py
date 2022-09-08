from django.db import models
#from django.db import settings
#from django.db import timezone

# Create your models here.

class endNum(models.Model):

    #net = models.IntegerField(blank=True, null=True)

    #net2 = models.IntegerField(blank=True, null=True)

    #net3 = models.IntegerField(blank=True, null=True)

    #flop = models.FloatField(blank=True, null=True)
    x1  = models.FloatField(blank=True, null=True)
    x2  = models.FloatField(blank=True, null=True)
    x3  = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.x1, self.x2, self.x3)