# Generated by Django 3.0.5 on 2020-04-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onetomany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(default='소나타', max_length=40, verbose_name='자동차모델'),
            preserve_default=False,
        ),
    ]
