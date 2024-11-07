from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class modelTest(models.Model):
    date = models.CharField(max_length=10, null=False)
    SID1 = models.IntegerField(null=False)
    SID2 = models.IntegerField(null=False)
    title = models.TextField(max_length=20)
    CONTENT = models.TextField(null=False)
    URL = models.TextField(null=False, unique=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'testtable1'


