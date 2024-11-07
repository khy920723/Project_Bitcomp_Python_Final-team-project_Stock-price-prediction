from django.db import models

# Create your models here.
class modelTest(models.Model):
    DATE = models.TextField(max_length=10, null=False)
    SID1 = models.IntegerField(null=False)
    SID2 = models.IntegerField(null=False)
    TITLE = models.TextField(max_length=20)
    CONTENT = models.TextField(null=False)
    URL = models.TextField(null=False, unique=True, primary_key=True)

    # class Meta:
    #     managed = False
    #     db_table = 'samsung_table'
    class Meta:
        managed = False
        db_table = 'testtable1'