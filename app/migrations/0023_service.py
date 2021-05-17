# Generated by Django 3.1 on 2020-08-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20200819_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('Service_id', models.AutoField(primary_key=True, serialize=False)),
                ('Service_Name', models.CharField(default='Name', max_length=200)),
                ('Service_Description', models.TextField(default='Desc')),
                ('Service_Image', models.ImageField(default='mypic', upload_to='Sevice/')),
                ('Service_Date', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.CharField(choices=[('daily', 'Daily'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], default='product', max_length=120)),
            ],
        ),
    ]