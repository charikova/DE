# Generated by Django 2.1.1 on 2018-10-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computational_practicum', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='euler',
            field=models.ImageField(upload_to='get_solution'),
        ),
        migrations.AlterField(
            model_name='image',
            name='improved_euler',
            field=models.ImageField(upload_to='get_solution'),
        ),
        migrations.AlterField(
            model_name='image',
            name='runge_kutta',
            field=models.ImageField(upload_to='get_solution'),
        ),
    ]
