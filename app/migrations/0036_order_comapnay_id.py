# Generated by Django 3.1 on 2020-08-23 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20200823_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Comapnay_Id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company_account'),
        ),
    ]
