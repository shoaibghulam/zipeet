# Generated by Django 3.1 on 2020-08-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20200822_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_account',
            name='password',
            field=models.CharField(default='password', max_length=100),
        ),
    ]
