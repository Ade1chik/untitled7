# Generated by Django 3.2 on 2021-05-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0018_delete_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='CLASS',
            field=models.CharField(default='10', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='info',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
