# Generated by Django 3.2.2 on 2021-05-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('information', models.TextField()),
                ('place', models.CharField(max_length=100)),
                ('pay', models.IntegerField(default=8520)),
                ('work', models.TextField(max_length=100)),
                ('applier', models.IntegerField(default=0)),
            ],
        ),
    ]
