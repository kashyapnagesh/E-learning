# Generated by Django 4.0.4 on 2022-04-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.FileField(blank=True, default='avtar.png', null=True, upload_to='profile'),
        ),
    ]
