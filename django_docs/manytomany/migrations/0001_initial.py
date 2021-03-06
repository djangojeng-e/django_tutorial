# Generated by Django 3.0.5 on 2020-04-20 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manytomany.Group')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manytomany.Person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='manytomany.Membership', to='manytomany.Person'),
        ),
    ]
