# Generated by Django 3.2.2 on 2021-05-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albamon_app', '0014_auto_20210522_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='applier',
            field=models.IntegerField(),
        ),
    ]
