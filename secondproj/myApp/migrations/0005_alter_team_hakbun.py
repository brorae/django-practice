# Generated by Django 3.2.2 on 2021-05-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20210512_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='hakbun',
            field=models.CharField(max_length=10),
        ),
    ]
