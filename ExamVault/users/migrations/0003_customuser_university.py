# Generated by Django 4.2.2 on 2023-06-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='university',
            field=models.CharField(default='None', max_length=50),
        ),
    ]