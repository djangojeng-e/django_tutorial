# Generated by Django 3.0.5 on 2020-04-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makingqueries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='number_of_comments',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='number_of_pingbacks',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating',
            field=models.IntegerField(blank=True),
        ),
    ]