# Generated by Django 3.1 on 2020-08-25 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_remove_order_comapnay_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='Company_Account_Id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company_account'),
        ),
        migrations.AddField(
            model_name='order',
            name='Product_Quantity',
            field=models.CharField(default=0, max_length=120),
        ),
        migrations.AddField(
            model_name='order',
            name='Product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]