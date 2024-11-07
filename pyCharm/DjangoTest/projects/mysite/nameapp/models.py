from django.db import models

# Create your models here.
class KospiPredict(models.Model):
    date = models.DateField(max_length=10, null=False, unique=True)
    close = models.IntegerField(null=True)
    open = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'jebal'

class KospiPredict2(models.Model):
    date = models.DateField(max_length=10, null=False, unique=True)
    close = models.IntegerField(null=True)
    open = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'jestest'
