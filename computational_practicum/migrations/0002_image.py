# Generated by Django 2.1.1 on 2018-10-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computational_practicum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('euler', models.ImageField(upload_to='')),
                ('improved_euler', models.ImageField(upload_to='')),
                ('runge_kutta', models.ImageField(upload_to='')),
            ],
        ),
    ]