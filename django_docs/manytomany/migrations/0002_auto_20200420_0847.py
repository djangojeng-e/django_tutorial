# Generated by Django 3.0.5 on 2020-04-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manytomany', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]