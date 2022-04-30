# Generated by Django 4.0.4 on 2022-04-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_messsge_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('tname', models.CharField(max_length=30)),
                ('date', models.DateField(auto_now_add=True)),
                ('duration', models.FloatField(default=0)),
                ('img', models.FileField(default='default-course.jpg', upload_to='courses')),
            ],
        ),
    ]