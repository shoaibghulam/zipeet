# Generated by Django 3.1 on 2020-08-25 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_auto_20200825_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Product_Quantity',
            field=models.CharField(default=0, max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]
