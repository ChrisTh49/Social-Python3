# Generated by Django 3.1.5 on 2021-01-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='batman.png', upload_to=''),
        ),
    ]
