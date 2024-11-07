# Generated by Django 3.1.4 on 2020-12-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modelTest',
            fields=[
                ('dates', models.CharField(max_length=10)),
                ('SID1s', models.IntegerField()),
                ('SID2s', models.IntegerField()),
                ('titles', models.TextField(max_length=20)),
                ('CONTENT', models.TextField()),
                ('URL', models.TextField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'testtable1',
                'managed': False,
            },
        ),
    ]