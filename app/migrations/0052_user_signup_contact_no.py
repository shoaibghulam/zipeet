# Generated by Django 3.1 on 2020-08-30 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_auto_20200828_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_signup',
            name='Contact_No',
            field=models.CharField(default='0', max_length=120),
        ),
    ]
